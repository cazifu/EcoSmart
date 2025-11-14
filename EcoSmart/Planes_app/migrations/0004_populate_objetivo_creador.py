# Generated manually

from django.db import migrations


def populate_creador(apps, schema_editor):
    Objetivo = apps.get_model('Planes_app', 'Objetivo')
    Plan = apps.get_model('Planes_app', 'Plan')
    
    for objetivo in Objetivo.objects.filter(creador__isnull=True):
        # Asignar el creador del plan como creador del objetivo
        objetivo.creador = objetivo.plan.creador
        objetivo.save()


def reverse_populate_creador(apps, schema_editor):
    # No hay necesidad de revertir esta operación
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('Planes_app', '0003_objetivo_creador'),
    ]

    operations = [
        migrations.RunPython(populate_creador, reverse_populate_creador),
    ]