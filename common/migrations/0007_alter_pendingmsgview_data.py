# Generated by Django 4.2.5 on 2023-11-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_remove_pendingmsgview_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingmsgview',
            name='data',
            field=models.JSONField(blank=True, max_length=500),
        ),
    ]
