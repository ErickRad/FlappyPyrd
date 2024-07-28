@echo off 
if not exist "python-installer.exe" (    echo Baixando o instalador do Python...    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe' -OutFile 'python-installer.exe'") 
echo Instalando Python... 
"python-installer.exe" /quiet InstallAllUsers=1 PrependPath=1 
IF 0 NEQ 0 (echo Falha na instalação do Python! Saindo...& exit /b 1) 
echo Python foi instalado com sucesso! 
echo Feche esta janela e continue com a instalação do Pygame. 
pause 
