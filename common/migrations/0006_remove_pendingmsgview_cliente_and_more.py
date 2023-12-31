# Generated by Django 4.2.5 on 2023-10-27 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_remove_pendingmsgview_creado_por_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendingmsgview',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='pendingmsgview',
            name='text',
        ),
        migrations.RemoveField(
            model_name='pendingmsgview',
            name='to',
        ),
        migrations.AddField(
            model_name='pendingmsgview',
            name='data',
            field=models.JSONField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='pendingmsgview',
            name='headers',
            field=models.JSONField(blank=True, default={}, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pendingmsgview',
            name='type',
            field=models.CharField(choices=[('WS', 'Whatsapp'), ('MSG', 'MSG')], default={}, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pendingmsgview',
            name='url',
            field=models.JSONField(blank=True, default={}, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pendingmsgview',
            name='error_code',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
