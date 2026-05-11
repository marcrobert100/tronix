@echo off
echo ============================================
echo   WhatsApp Clinic Agent - Iniciando...
echo ============================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python não encontrado!
    echo Instale o Python em https://python.org
    pause
    exit /b 1
)

REM Cria ambiente virtual se não existir
if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
)

REM Ativa ambiente virtual
call venv\Scripts\activate.bat

REM Instala dependências
echo Instalando atualizando dependências...
pip install -r requirements.txt -q

REM Executa o agente
echo.
echo Iniciando sistema...
echo.
python main.py

pause
