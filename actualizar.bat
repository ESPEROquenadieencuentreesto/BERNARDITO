@echo off
set REPO_DIR=BERNARDITO
set REPO_URL=https://github.com/ESPEROquenadieencuentreesto/BERNARDITO.git

if exist %REPO_DIR% (
    echo Borrando la version anterior w..
    rd /s /q %REPO_DIR%
)

echo Clonando el repo en fa..
git clone %REPO_URL%

cd %REPO_DIR%
echo Instalando dependencias en chinguiza..
py -m pip install -r requirements.txt

echo Ejecutando esta ptm..
py mainbernardin.py

pause
