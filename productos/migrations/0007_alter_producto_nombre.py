# Generated by Django 4.2.5 on 2023-11-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_remove_producto_cantidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
