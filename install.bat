@echo off
:: Baixar o instalador do Python
powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe' -OutFile 'bin/python-installer.exe'"

:: Instalar Python como administrador
:: O comando a seguir deve ser executado com permissões de administrador
bin/python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

:: Verificar se Python foi instalado
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo | Python foi instalado com sucesso!
    exit /b 1
)

:: Instalar Pygame
pip install pygame

echo.              
echo                    ___________
echo                ___/     _/    \_
echo              _/        /       _\_
echo            _/          /      / \ \
echo          _/_________   \_     \_/ /
echo         /           \    \________/_
echo        \            /    _/         \__
echo         \___________/  _/ ____________/
echo           \_           \_           _/
echo             \___         \_________/
echo                 \________/
echo.
echo FlappyBird foi instalado com sucesso! Aproveite!
echo Para rodar: Clique duplo no arquivo run.bat
echo Para jogar: Pressione ENTER
echo.