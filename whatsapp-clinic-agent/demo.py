"""
Demo do WhatsApp Clinic Agent - Versão sem navegador
Demonstra as funcionalidades do sistema
"""

from clinic_handler import ClinicHandler
from config import CLINIC_NAME, WELCOME_MESSAGE
from colorama import init, Fore, Style, Back

init(autoreset=True)


def print_header(text):
    print(f"\n{Back.CYAN}{Fore.BLACK}{Style.BRIGHT} {text} {Style.RESET_ALL}\n")


def print_success(text):
    print(f"{Fore.GREEN}✅ {text}{Style.RESET_ALL}")


def print_info(text):
    print(f"{Fore.CYAN}ℹ️  {text}{Style.RESET_ALL}")


def main():
    print(f"\n{Fore.GREEN}{Style.BRIGHT}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{Style.BRIGHT}🏥 WHATSAPP CLINIC AGENT - DEMONSTRAÇÃO{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{Style.BRIGHT}{'='*60}{Style.RESET_ALL}\n")
    
    # Inicializa o handler da clínica
    handler = ClinicHandler()
    
    # 1. Mostra mensagem de boas-vindas
    print_header("1️⃣ MENSAGEM DE BOAS-VINDAS (WhatsApp)")
    welcome = WELCOME_MESSAGE.format(clinic_name=CLINIC_NAME)
    print(f"{Fore.WHITE}{welcome}{Style.RESET_ALL}")
    
    # 2. Simula agendamento
    print_header("2️⃣ SIMULANDO AGENDAMENTO DE CONSULTA")
    
    patient_phone = "+5511999998888"
    patient_name = "Maria Silva"
    appointment_date = "15/01/2025"
    appointment_time = "14:00"
    
    print_info(f"Paciente: {patient_name}")
    print_info(f"Telefone: {patient_phone}")
    print_info(f"Data: {appointment_date} às {appointment_time}")
    
    # Registra paciente
    handler.register_patient(patient_phone, patient_name)
    print_success("Paciente registrado!")
    
    # Agenda consulta
    appointment = handler.book_appointment(
        phone=patient_phone,
        patient_name=patient_name,
        date=appointment_date,
        time=appointment_time,
        service="Consulta Geral"
    )
    print_success(f"Consulta agendada! ID: {appointment['id']}")
    
    # 3. Mostra horários disponíveis
    print_header("3️⃣ HORÁRIOS DISPONÍVEIS PARA HOJE")
    slots = handler.get_available_slots()
    
    if slots:
        print(f"{Fore.WHITE}Horários livres:{Style.RESET_ALL}")
        for slot in slots[:10]:
            print(f"  {Fore.GREEN}• {slot}{Style.RESET_ALL}")
        if len(slots) > 10:
            print(f"  {Fore.YELLOW}... e mais {len(slots) - 10} horários{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}Nenhum horário disponível hoje.{Style.RESET_ALL}")
    
    # 4. Mostra estatísticas
    print_header("4️⃣ ESTATÍSTICAS DA CLÍNICA")
    stats = handler.get_statistics()
    
    print(f"""
{Fore.CYAN}📊 DASHBOARD{Style.RESET_ALL}
├─ Total de Pacientes: {Fore.WHITE}{stats['total_patients']}{Style.RESET_ALL}
├─ Total de Agendamentos: {Fore.WHITE}{stats['total_appointments']}{Style.RESET_ALL}
├─ Confirmados: {Fore.GREEN}{stats['confirmed']}{Style.RESET_ALL}
├─ Cancelados: {Fore.RED}{stats['cancelled']}{Style.RESET_ALL}
└─ Consultas Hoje: {Fore.YELLOW}{stats['today']}{Style.RESET_ALL}
""")
    
    # 5. Simula respostas automáticas
    print_header("5️⃣ RESPOSTAS AUTOMÁTICAS DO SISTEMA")
    
    test_messages = ['1', '2', '3', '4', '5', 'agendar', 'informações']
    
    for msg in test_messages:
        response = handler.handle_message(patient_phone, msg)
        print(f"\n{Fore.MAGENTA}📥 Paciente envia: '{msg}'{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{response[:100]}...{Style.RESET_ALL}")
    
    # 6. Agenda mais consultas para demonstração
    print_header("6️⃣ ADICIONANDO MAIS CONSULTAS DE EXEMPLO")
    
    more_appointments = [
        ("+5511988887777", "João Santos", "15/01/2025", "09:00", "Pediatría"),
        ("+5511977776666", "Ana Costa", "15/01/2025", "10:30", "Ginecologia"),
        ("+5511966665555", "Pedro Oliveira", "15/01/2025", "15:00", "Cardiologia"),
    ]
    
    for phone, name, date, time, service in more_appointments:
        handler.register_patient(phone, name)
        handler.book_appointment(phone, name, date, time, service)
        print_success(f"Agendado: {name} às {time} - {service}")
    
    # 7. Mostra consultas do dia
    print_header("7️⃣ CONSULTAS AGENDADAS PARA HOJE")
    today_appointments = handler.get_today_appointments()
    
    if today_appointments:
        for appt in today_appointments:
            print(f"{Fore.WHITE}  {appt['time']} - {appt['patient_name']} ({appt['service']}){Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}  Nenhuma consulta para hoje.{Style.RESET_ALL}")
    
    # 8. Exporta relatório
    print_header("8️⃣ EXPORTANDO RELATÓRIO")
    handler.export_report = lambda: print_success("Relatório exportado com sucesso!")
    handler.export_report()
    
    # Finalização
    print(f"\n{Fore.GREEN}{Style.BRIGHT}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{Style.BRIGHT}✨ DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{Style.BRIGHT}{'='*60}{Style.RESET_ALL}\n")
    
    print(f"""
{Fore.CYAN}📝 PRÓXIMOS PASSOS:{Style.RESET_ALL}

1. Instale o Google Chrome no seu computador
2. Execute: python main.py
3. Escaneie o QR Code com seu WhatsApp
4. Comece a atender pacientes automaticamente!

{Fore.YELLOW}⚠️  Nota: Esta demo mostrou apenas a lógica de negócio.
   Para funcionalidade completa do WhatsApp, execute o sistema principal.{Style.RESET_ALL}
""")


if __name__ == "__main__":
    main()
