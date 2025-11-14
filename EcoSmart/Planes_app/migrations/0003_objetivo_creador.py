# Generated manually

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Planes_app', '0002_alter_suscripcion_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='objetivo',
            name='creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='objetivos_creados', to=settings.AUTH_USER_MODEL),
        ),
    ]