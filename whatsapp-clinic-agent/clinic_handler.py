"""
Módulo de manipulação de mensagens para clínica
Gerencia agendamentos, cancelamentos e informações
"""

from datetime import datetime, timedelta
import json
import os
from config import CLINIC_NAME, WORKING_SCHEDULE, DEFAULT_APPOINTMENT_DURATION


class ClinicHandler:
    def __init__(self):
        self.appointments_file = "appointments.json"
        self.patients_file = "patients.json"
        self.load_data()
    
    def load_data(self):
        """Carrega dados dos arquivos JSON"""
        if os.path.exists(self.appointments_file):
            with open(self.appointments_file, 'r', encoding='utf-8') as f:
                self.appointments = json.load(f)
        else:
            self.appointments = []
        
        if os.path.exists(self.patients_file):
            with open(self.patients_file, 'r', encoding='utf-8') as f:
                self.patients = json.load(f)
        else:
            self.patients = {}
    
    def save_data(self):
        """Salva dados nos arquivos JSON"""
        with open(self.appointments_file, 'w', encoding='utf-8') as f:
            json.dump(self.appointments, f, indent=2, ensure_ascii=False)
        
        with open(self.patients_file, 'w', encoding='utf-8') as f:
            json.dump(self.patients, f, indent=2, ensure_ascii=False)
    
    def register_patient(self, phone, name=None):
        """Registra ou atualiza paciente"""
        if phone not in self.patients:
            self.patients[phone] = {
                'name': name or 'Não informado',
                'phone': phone,
                'created_at': datetime.now().isoformat(),
                'appointments_count': 0
            }
            self.save_data()
            return True
        return False
    
    def get_available_slots(self, date_str=None):
        """Retorna horários disponíveis para um dia"""
        if not date_str:
            date_obj = datetime.now()
        else:
            try:
                date_obj = datetime.strptime(date_str, '%d/%m/%Y')
            except:
                return []
        
        day_name = date_obj.strftime('%A')
        schedule = WORKING_SCHEDULE.get(day_name)
        
        if not schedule:
            return []  # Clínica fechada
        
        start_time = datetime.strptime(schedule[0], '%H:%M')
        end_time = datetime.strptime(schedule[1], '%H:%M')
        
        slots = []
        current_time = start_time
        
        while current_time + timedelta(minutes=DEFAULT_APPOINTMENT_DURATION) <= end_time:
            slot_time = current_time.strftime('%H:%M')
            
            # Verifica se já está agendado
            is_booked = any(
                appt['date'] == date_obj.strftime('%d/%m/%Y') and 
                appt['time'] == slot_time and
                appt['status'] == 'confirmed'
                for appt in self.appointments
            )
            
            if not is_booked:
                slots.append(slot_time)
            
            current_time += timedelta(minutes=DEFAULT_APPOINTMENT_DURATION)
        
        return slots
    
    def book_appointment(self, phone, patient_name, date, time, service="Consulta Geral"):
        """Agenda uma consulta"""
        appointment = {
            'id': len(self.appointments) + 1,
            'phone': phone,
            'patient_name': patient_name,
            'date': date,
            'time': time,
            'service': service,
            'status': 'confirmed',
            'created_at': datetime.now().isoformat()
        }
        
        self.appointments.append(appointment)
        
        # Atualiza contador do paciente
        if phone in self.patients:
            self.patients[phone]['appointments_count'] += 1
        
        self.save_data()
        return appointment
    
    def cancel_appointment(self, phone, date, time):
        """Cancela uma consulta"""
        for appt in self.appointments:
            if (appt['phone'] == phone and 
                appt['date'] == date and 
                appt['time'] == time):
                appt['status'] = 'cancelled'
                self.save_data()
                return True
        return False
    
    def get_patient_appointments(self, phone):
        """Retorna todas as consultas de um paciente"""
        return [
            appt for appt in self.appointments 
            if appt['phone'] == phone and appt['status'] == 'confirmed'
        ]
    
    def get_today_appointments(self):
        """Retorna consultas do dia"""
        today = datetime.now().strftime('%d/%m/%Y')
        return [
            appt for appt in self.appointments 
            if appt['date'] == today and appt['status'] == 'confirmed'
        ]
    
    def get_statistics(self):
        """Retorna estatísticas da clínica"""
        today = datetime.now().strftime('%d/%m/%Y')
        
        total_appointments = len(self.appointments)
        confirmed = sum(1 for a in self.appointments if a['status'] == 'confirmed')
        cancelled = sum(1 for a in self.appointments if a['status'] == 'cancelled')
        today_count = len(self.get_today_appointments())
        total_patients = len(self.patients)
        
        return {
            'total_appointments': total_appointments,
            'confirmed': confirmed,
            'cancelled': cancelled,
            'today': today_count,
            'total_patients': total_patients
        }
    
    def handle_message(self, phone, message, user_state=None):
        """Processa mensagem e retorna resposta apropriada"""
        message = message.strip().lower()
        
        # Registra paciente se não existir
        self.register_patient(phone)
        
        responses = {
            '1': self._response_schedule_menu(),
            '2': self._response_cancel_menu(),
            '3': self._response_available_slots(),
            '4': self._response_human_attendant(),
            '5': self._response_clinic_info(),
            'agendar': self._response_schedule_menu(),
            'cancelar': self._response_cancel_menu(),
            'horários': self._response_available_slots(),
            'atendente': self._response_human_attendant(),
            'informações': self._response_clinic_info(),
        }
        
        return responses.get(message, self._response_invalid_option())
    
    def _response_schedule_menu(self):
        return """
📅 *Agendamento de Consulta*

Por favor, me informe:
1. Seu nome completo
2. Data desejada (DD/MM/AAAA)
3. Horário preferido

Exemplo: João Silva, 15/01/2025, 14:00
"""
    
    def _response_cancel_menu(self):
        return """
❌ *Cancelar/Remarcar Consulta*

Para cancelar ou remarcar, informe:
1. Seu nome
2. Data da consulta
3. Horário da consulta

Exemplo: João Silva, 15/01/2025, 14:00
"""
    
    def _response_available_slots(self):
        today = datetime.now()
        slots = self.get_available_slots(today.strftime('%d/%m/%Y'))
        
        if slots:
            slots_str = '\n'.join([f"• {s}" for s in slots[:10]])
            return f"""
🕐 *Horários Disponíveis Hoje*

{slots_str}

Para agendar, digite 1
"""
        else:
            return """
😕 Não há horários disponíveis para hoje.

Gostaria de ver horários para outro dia?
Digite a data desejada (DD/MM/AAAA)
"""
    
    def _response_human_attendant(self):
        return """
👤 *Atendimento Humano*

Um de nossos atendentes será direcionado para esta conversa.

Enquanto isso, você pode continuar navegando pelo menu principal.

Tempo médio de espera: 5 minutos
"""
    
    def _response_clinic_info(self):
        from config import CLINIC_ADDRESS, CLINIC_PHONE, CLINIC_WORKING_HOURS
        return f"""
🏥 *{CLINIC_NAME}*

📍 Endereço: {CLINIC_ADDRESS}
📞 Telefone: {CLINIC_PHONE}
⏰ Horário: {CLINIC_WORKING_HOURS}

🩺 Especialidades:
• Clínica Geral
• Pediatria
• Ginecologia
• Cardiologia
• Ortopedia

💳 Aceitamos todos os convênios!
"""
    
    def _response_invalid_option(self):
        return """
😕 Opção não reconhecida.

Por favor, escolha uma das opções do menu:

1️⃣ Agendar Consulta
2️⃣ Cancelar/Remarcar Consulta
3️⃣ Ver Horários Disponíveis
4️⃣ Falar com Atendente Humano
5️⃣ Informações sobre a Clínica
"""
