@echo off
echo Ejecutando migraciones para objetivos...
cd EcoSmart
python manage.py migrate Planes_app 0003_objetivo_creador
python manage.py migrate Planes_app 0004_populate_objetivo_creador
python manage.py migrate Planes_app 0005_alter_objetivo_creador
echo Migraciones completadas!
pause