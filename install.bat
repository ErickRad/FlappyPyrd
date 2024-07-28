@echo off

:: Verificar se Chocolatey está instalado
choco -v >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Instalando Chocolatey...
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
)

:: Verificar se o Chocolatey está instalado corretamente
choco -v >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Falha na instalação do Chocolatey! Verifique se o script foi executado com permissões de administrador.
    exit /b 1
)

:: Instalar Python usando Chocolatey
choco install python --version 3.12.4 -y

:: Verificar se Python foi instalado corretamente
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Falha na instalação do Python! Saindo...
    exit /b 1
)

:: Instalar Pygame usando pip
python -m pip install pygame

:: Exibir mensagem de sucesso e arte ASCII
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
echo FlappyPyrd foi instalado com sucesso! Aproveite!
echo Para rodar: Clique duplo no arquivo run.bat
echo Para jogar: Pressione ENTER
echo.

pause
