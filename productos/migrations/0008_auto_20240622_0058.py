# Generated by Django 3.2.8 on 2024-06-22 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_alter_producto_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='costo_flete',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='iva',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='porcentaje_ganancia',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_venta',
            field=models.IntegerField(default=0),
        ),
    ]