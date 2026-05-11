"""
Agente WhatsApp para Clínicas
Gerencia conexão WhatsApp e painel de controle
"""

import time
import threading
from datetime import datetime
from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    SELENIUM_AVAILABLE = True
except ImportError as e:
    SELENIUM_AVAILABLE = False
    print(f"{Fore.YELLOW}Selenium ou webdriver-manager não instalado. Execute: pip install selenium webdriver-manager{Style.RESET_ALL}")

from config import CLINIC_NAME, WHATSAPP_SESSION_NAME, COLORS, PANEL_REFRESH_RATE
from clinic_handler import ClinicHandler


class WhatsAppClinicAgent:
    def __init__(self):
        self.clinic_handler = ClinicHandler()
        self.driver = None
        self.is_connected = False
        self.running = False
        self.user_states = {}  # Armazena estado de cada usuário
        
    def setup_browser(self):
        """Configura o navegador Chrome"""
        if not SELENIUM_AVAILABLE:
            print(f"{Fore.RED}Selenium não disponível. Instale com: pip install selenium webdriver-manager{Style.RESET_ALL}")
            return False
        
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=./chrome_profile")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        try:
            # Usa webdriver-manager para gerenciar automaticamente o ChromeDriver
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.get("https://web.whatsapp.com")
            return True
        except Exception as e:
            print(f"{Fore.RED}Erro ao iniciar navegador: {e}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Certifique-se de ter o Google Chrome instalado.{Style.RESET_ALL}")
            return False
    
    def wait_for_qr_scan(self):
        """Aguarda escaneamento do QR Code"""
        print(f"\n{Fore.CYAN}╔════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Fore.WHITE}  📱 Aguardando escaneamento do QR Code  {Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚════════════════════════════════════════╝{Style.RESET_ALL}\n")
        
        max_wait = 60  # segundos
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            try:
                # Verifica se está conectado (procura elemento específico do WhatsApp Web)
                search_box = self.driver.find_elements(By.CSS_SELECTOR, 'div[title="Caixa de pesquisa"]')
                if search_box:
                    print(f"\n{Fore.GREEN}✅ Conexão estabelecida com sucesso!{Style.RESET_ALL}")
                    self.is_connected = True
                    return True
                
                # Tenta encontrar QR Code
                qr_element = self.driver.find_elements(By.CSS_SELECTOR, 'canvas')
                if qr_element:
                    print(f"{Fore.YELLOW}⏳ QR Code exibido. Escaneie com seu WhatsApp...{Style.RESET_ALL}")
                
                time.sleep(2)
            except Exception as e:
                time.sleep(2)
        
        print(f"{Fore.RED}❌ Tempo esgotado para escanear QR Code.{Style.RESET_ALL}")
        return False
    
    def display_panel(self):
        """Exibe painel de controle no terminal"""
        while self.running:
            try:
                # Limpa tela (funciona em Linux/Mac e Windows)
                print("\033[2J\033[H", end="")
                
                stats = self.clinic_handler.get_statistics()
                today_appointments = self.clinic_handler.get_today_appointments()
                
                print(f"\n{Fore.GREEN}{Style.BRIGHT}{'='*60}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}{Style.BRIGHT}🏥  PAINEL DE CONTROLE - {CLINIC_NAME}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}{Style.BRIGHT}{'='*60}{Style.RESET_ALL}")
                
                print(f"\n{Fore.CYAN}📊 ESTATÍSTICAS GERAIS:{Style.RESET_ALL}")
                print(f"   • Total de Pacientes: {Fore.WHITE}{stats['total_patients']}{Style.RESET_ALL}")
                print(f"   • Total de Agendamentos: {Fore.WHITE}{stats['total_appointments']}{Style.RESET_ALL}")
                print(f"   • Confirmados: {Fore.GREEN}{stats['confirmed']}{Style.RESET_ALL}")
                print(f"   • Cancelados: {Fore.RED}{stats['cancelled']}{Style.RESET_ALL}")
                print(f"   • Consultas Hoje: {Fore.YELLOW}{stats['today']}{Style.RESET_ALL}")
                
                print(f"\n{Fore.CYAN}📅 CONSULTAS DE HOJE:{Style.RESET_ALL}")
                if today_appointments:
                    for appt in today_appointments[:5]:
                        print(f"   {Fore.WHITE}• {appt['time']} - {appt['patient_name']} ({appt['service']}){Style.RESET_ALL}")
                    if len(today_appointments) > 5:
                        print(f"   {Fore.YELLOW}... e mais {len(today_appointments) - 5} consultas{Style.RESET_ALL}")
                else:
                    print(f"   {Fore.YELLOW}Nenhuma consulta agendada para hoje.{Style.RESET_ALL}")
                
                print(f"\n{Fore.CYAN}🔧 COMANDOS DISPONÍVEIS:{Style.RESET_ALL}")
                print(f"   {Fore.WHITE}[1]{Style.RESET_ALL} Ver todas as consultas de hoje")
                print(f"   {Fore.WHITE}[2]{Style.RESET_ALL} Ver estatísticas detalhadas")
                print(f"   {Fore.WHITE}[3]{Style.RESET_ALL} Exportar relatório")
                print(f"   {Fore.WHITE}[q]{Style.RESET_ALL} Sair do sistema")
                
                print(f"\n{Fore.GREEN}{'='*60}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Status: {Fore.GREEN}● Online{Style.RESET_ALL} | Atualizando a cada {PANEL_REFRESH_RATE}s")
                print(f"{Fore.YELLOW}Pressione 'q' e Enter para sair{Style.RESET_ALL}")
                
                time.sleep(PANEL_REFRESH_RATE)
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"{Fore.RED}Erro no painel: {e}{Style.RESET_ALL}")
                time.sleep(5)
    
    def check_new_messages(self):
        """Verifica novas mensagens (simulação para demonstração)"""
        # Em produção, isso usaria a API real do WhatsApp Web via Selenium
        # ou uma biblioteca como whatsapp-web.js
        
        print(f"\n{Fore.BLUE}ℹ️  Sistema pronto para receber mensagens...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Nota: Esta é uma versão de demonstração.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Para funcionalidade completa, integre com a API oficial do WhatsApp Business.{Style.RESET_ALL}")
        
        while self.running and self.is_connected:
            try:
                # Simulação de recebimento de mensagens
                # Em produção, aqui estaria a lógica real de scraping do WhatsApp Web
                time.sleep(5)
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"{Fore.RED}Erro ao verificar mensagens: {e}{Style.RESET_ALL}")
                time.sleep(5)
    
    def export_report(self):
        """Exporta relatório em formato texto"""
        stats = self.clinic_handler.get_statistics()
        today = datetime.now().strftime('%d/%m/%Y %H:%M')
        
        report = f"""
RELATÓRIO - {CLINIC_NAME}
Gerado em: {today}

{'='*50}
ESTATÍSTICAS GERAIS
{'='*50}
Total de Pacientes: {stats['total_patients']}
Total de Agendamentos: {stats['total_appointments']}
Consultas Confirmadas: {stats['confirmed']}
Consultas Canceladas: {stats['cancelled']}
Consultas Hoje: {stats['today']}

{'='*50}
CONSULTAS DE HOJE
{'='*50}
"""
        
        today_appointments = self.clinic_handler.get_today_appointments()
        if today_appointments:
            for appt in today_appointments:
                report += f"{appt['time']} - {appt['patient_name']} ({appt['service']})\n"
        else:
            report += "Nenhuma consulta agendada.\n"
        
        filename = f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"{Fore.GREEN}✅ Relatório exportado: {filename}{Style.RESET_ALL}")
    
    def run(self):
        """Inicia o agente"""
        print(f"\n{Fore.GREEN}{Style.BRIGHT}╔═══════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}║  🏥 WhatsApp Clinic Agent - Iniciando...  ║{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}╚═══════════════════════════════════════════╝{Style.RESET_ALL}\n")
        
        # Configura navegador
        if not self.setup_browser():
            print(f"\n{Fore.RED}Falha ao configurar navegador. Encerrando.{Style.RESET_ALL}")
            return
        
        # Aguarda QR Code
        if not self.wait_for_qr_scan():
            print(f"\n{Fore.RED}Falha na conexão. Encerrando.{Style.RESET_ALL}")
            if self.driver:
                self.driver.quit()
            return
        
        self.running = True
        
        # Inicia threads
        panel_thread = threading.Thread(target=self.display_panel, daemon=True)
        message_thread = threading.Thread(target=self.check_new_messages, daemon=True)
        
        panel_thread.start()
        message_thread.start()
        
        # Loop principal para comandos do usuário
        print(f"\n{Fore.CYAN}Painel iniciado. Use os comandos numéricos para ações.{Style.RESET_ALL}")
        
        while self.running:
            try:
                command = input(f"\n{Fore.WHITE}Comando: {Style.RESET_ALL}").strip().lower()
                
                if command == 'q':
                    print(f"\n{Fore.YELLOW}Encerrando sistema...{Style.RESET_ALL}")
                    self.running = False
                    break
                elif command == '1':
                    appointments = self.clinic_handler.get_today_appointments()
                    print(f"\n{Fore.CYAN}Todas as consultas de hoje:{Style.RESET_ALL}")
                    for appt in appointments:
                        print(f"  {appt['time']} - {appt['patient_name']} ({appt['service']})")
                elif command == '2':
                    stats = self.clinic_handler.get_statistics()
                    print(f"\n{Fore.CYAN}Estatísticas Detalhadas:{Style.RESET_ALL}")
                    for key, value in stats.items():
                        print(f"  {key}: {value}")
                elif command == '3':
                    self.export_report()
                else:
                    print(f"{Fore.YELLOW}Comando desconhecido. Use 1, 2, 3 ou q.{Style.RESET_ALL}")
                    
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}Interrupto pelo usuário.{Style.RESET_ALL}")
                self.running = False
                break
        
        # Limpeza
        if self.driver:
            self.driver.quit()
        
        print(f"\n{Fore.GREEN}Sistema encerrado. Até logo!{Style.RESET_ALL}\n")


if __name__ == "__main__":
    agent = WhatsAppClinicAgent()
    agent.run()
