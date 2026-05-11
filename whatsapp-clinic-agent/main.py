"""
Ponto de entrada principal do WhatsApp Clinic Agent
"""

from whatsapp_agent import WhatsAppClinicAgent


def main():
    """Função principal que inicia o agente"""
    print("\n" + "="*60)
    print("  🏥 WHATSAPP CLINIC AGENT")
    print("  Sistema de Atendimento Automático para Clínicas")
    print("="*60 + "\n")
    
    # Cria e executa o agente
    agent = WhatsAppClinicAgent()
    agent.run()


if __name__ == "__main__":
    main()
