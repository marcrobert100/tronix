"""
Configurações do Agente WhatsApp para Clínicas
"""

# Configurações da Clínica
CLINIC_NAME = "Clínica Saúde & Bem-Estar"
CLINIC_ADDRESS = "Rua das Flores, 123 - Centro"
CLINIC_PHONE = "(11) 99999-9999"
CLINIC_WORKING_HOURS = "Segunda a Sexta: 08:00 - 18:00 | Sábado: 08:00 - 12:00"

# Configurações do WhatsApp
WHATSAPP_SESSION_NAME = "clinic_session"
QR_CODE_REFRESH_INTERVAL = 30  # segundos

# Mensagens Padrão
WELCOME_MESSAGE = """
🏥 *{clinic_name}*
Olá! Sou o assistente virtual da {clinic_name}.

Como posso ajudar você hoje?

1️⃣ Agendar Consulta
2️⃣ Cancelar/Remarcar Consulta
3️⃣ Ver Horários Disponíveis
4️⃣ Falar com Atendente Humano
5️⃣ Informações sobre a Clínica

Digite o número da opção desejada:
"""

# Horários de funcionamento por dia da semana
WORKING_SCHEDULE = {
    'Monday': ['08:00', '18:00'],
    'Tuesday': ['08:00', '18:00'],
    'Wednesday': ['08:00', '18:00'],
    'Thursday': ['08:00', '18:00'],
    'Friday': ['08:00', '18:00'],
    'Saturday': ['08:00', '12:00'],
    'Sunday': None  # Fechado
}

# Duração padrão das consultas (em minutos)
DEFAULT_APPOINTMENT_DURATION = 30

# Configurações do Painel
PANEL_REFRESH_RATE = 5  # segundos
LOG_FILE = "clinic_agent.log"

# Cores para o terminal (usando colorama)
COLORS = {
    'HEADER': '\033[95m',
    'BLUE': '\033[94m',
    'CYAN': '\033[96m',
    'GREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
}
