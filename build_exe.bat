@echo off
echo Instalando dependencias necessarias...
pip install pyinstaller -q

echo Compilando o sistema para EXE...
pyinstaller --onefile --windowed --name "CopaBets_Bares" copa_bets_system.py

echo.
echo ==========================================
echo Compilacao finalizada!
echo O arquivo EXE esta na pasta 'dist'
echo ==========================================
pause
