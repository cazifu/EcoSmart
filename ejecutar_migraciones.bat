@echo off
echo Ejecutando migraciones...
cd EcoSmart
python manage.py migrate
echo Migraciones completadas!
echo.
echo Ahora ejecuta aplicar_cambios_objetivos.bat para activar las funcionalidades
pause