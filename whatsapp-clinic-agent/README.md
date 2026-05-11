# WhatsApp Clinic Agent

Agente de WhatsApp automatizado para clínicas com painel de controle via terminal e geração de QR Code.

## 🏥 Funcionalidades

- ✅ Geração automática de QR Code no navegador
- ✅ Painel de controle em tempo real no terminal
- ✅ Respostas automáticas para clínicas
- ✅ Agendamento de consultas
- ✅ Cancelamento/Remarcação de consultas
- ✅ Verificação de horários disponíveis
- ✅ Triagem inicial de pacientes
- ✅ Exportação de relatórios
- ✅ Estatísticas em tempo real

## 📋 Requisitos

- Python 3.8+
- Google Chrome ou Chromium instalado
- Conexão com internet
- WhatsApp Web ativo no celular

## 🚀 Instalação

### Windows

1. Baixe e instale o Python em [python.org](https://python.org)
2. Extraia a pasta do projeto
3. Execute `run.bat` (duplo clique)

Ou manualmente:

```bash
# Cria ambiente virtual
python -m venv venv

# Ativa ambiente virtual
venv\Scripts\activate

# Instala dependências
pip install -r requirements.txt

# Executa o sistema
python main.py
```

### Linux/Mac

```bash
# Dê permissão ao script
chmod +x run.sh

# Execute o script
./run.sh
```

Ou manualmente:

```bash
# Cria ambiente virtual
python3 -m venv venv

# Ativa ambiente virtual
source venv/bin/activate

# Instala dependências
pip install -r requirements.txt

# Executa o sistema
python main.py
```

## 💡 Como Usar

1. **Execute o sistema**: `python main.py` ou use os scripts `run.bat`/`run.sh`

2. **Escaneie o QR Code**: 
   - O navegador abrirá automaticamente no WhatsApp Web
   - Escaneie o QR Code com seu WhatsApp (Menu > Aparelhos Conectados)

3. **Use o Painel**:
   - Visualize estatísticas em tempo real
   - Veja consultas do dia
   - Exporte relatórios
   - Use comandos: `[1]`, `[2]`, `[3]`, `[q]`

4. **Atendimento Automático**:
   - Os pacientes podem enviar mensagens no WhatsApp
   - O sistema responde automaticamente com menu de opções
   - Agendamentos são salvos automaticamente

## 🎯 Comandos do Painel

| Comando | Descrição |
|---------|-----------|
| `1` | Ver todas as consultas de hoje |
| `2` | Ver estatísticas detalhadas |
| `3` | Exportar relatório em TXT |
| `q` | Sair do sistema |

## 📱 Menu do Paciente (WhatsApp)

Os pacientes podem enviar:

- `1` ou "agendar" → Agendar consulta
- `2` ou "cancelar" → Cancelar/remarcar consulta
- `3` ou "horários" → Ver horários disponíveis
- `4` ou "atendente" → Falar com atendente humano
- `5` ou "informações" → Dados da clínica

## ⚙️ Configuração

Edite o arquivo `config.py` para personalizar:

```python
CLINIC_NAME = "Sua Clínica Aqui"
CLINIC_ADDRESS = "Seu Endereço"
CLINIC_PHONE = "(XX) XXXXX-XXXX"
CLINIC_WORKING_HOURS = "Seg-Sex: 08:00-18:00"
```

## 📁 Estrutura do Projeto

```
whatsapp-clinic-agent/
├── main.py              # Ponto de entrada principal
├── whatsapp_agent.py    # Lógica do agente WhatsApp
├── clinic_handler.py    # Manipulador de mensagens
├── config.py            # Configurações personalizáveis
├── requirements.txt     # Dependências Python
├── run.bat             # Script Windows
├── run.sh              # Script Linux/Mac
└── README.md           # Este arquivo
```

## 🔧 Troubleshooting

### Erro: "Chrome não encontrado"
- Instale o Google Chrome: [chrome.com](https://google.com/chrome)
- No Linux: `sudo apt install chromium-browser`

### Erro: "QR Code não aparece"
- Verifique sua conexão com internet
- Reinicie o sistema
- Limpe o cache do navegador

### Erro: "Selenium não disponível"
- Execute: `pip install selenium webdriver-manager`

## 📝 Notas Importantes

⚠️ **Este sistema usa WhatsApp Web via automação**. Para uso comercial/profissional, considere usar a **API Oficial do WhatsApp Business** para evitar bloqueios.

💾 Os dados são salvos localmente em arquivos JSON (`appointments.json`, `patients.json`).

🔒 Mantenha o celular conectado à internet enquanto o sistema estiver em execução.

## 📄 Licença

Projeto desenvolvido para fins educacionais e de demonstração.

---

**Desenvolvido com ❤️ para clínicas e consultórios**
