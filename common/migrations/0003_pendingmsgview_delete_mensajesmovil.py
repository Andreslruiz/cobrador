# Generated by Django 4.2.5 on 2023-10-21 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_clienteprofile_company'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0002_mensajesmovil'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingMsgView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('error_code', models.CharField(blank=True, max_length=300)),
                ('fecha_creación', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.clienteprofile')),
                ('creado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='MensajesMovil',
        ),
    ]
