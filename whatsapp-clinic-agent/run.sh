#!/bin/bash

echo "============================================"
echo "  WhatsApp Clinic Agent - Iniciando..."
echo "============================================"
echo ""

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "[ERRO] Python3 não encontrado!"
    echo "Instale o Python3 antes de continuar."
    exit 1
fi

# Cria ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativa ambiente virtual
source venv/bin/activate

# Instala dependências
echo "Instalando/atualizando dependências..."
pip install -r requirements.txt -q

# Executa o agente
echo ""
echo "Iniciando sistema..."
echo ""
python main.py
