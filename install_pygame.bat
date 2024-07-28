@echo off 
set "PATH=C:\Users\erick\AppData\Local\Programs\Python\Python39\Scripts;C:\Users\erick\AppData\Local\Programs\Python\Python39;%PATH%" 
python --version >nul 2>&1 
IF 0 NEQ 0 (echo Python não encontrado. Verifique a instalação e o PATH.& exit /b 1) 
pip --version >nul 2>&1 
IF 0 NEQ 0 (echo pip não encontrado. Instalando pip...& python -m ensurepip --upgrade& python -m pip install --upgrade pip) 
echo Instalando Pygame... 
python -m pip install pygame 
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
