# Generated by Django 4.1.2 on 2023-05-16 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0003_delete_autoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sicadfull',
            options={'permissions': [('BOP', 'Modificar dados relacionados ao BOP'), ('Autor', 'Modificar dados relacionados ao autor'), ('Vitima', 'Modificar dados relacionados à vitima'), ('Modus', 'Modificar dados relacionados ao Modus operandi')]},
        ),
    ]
