# Generated by Django 4.1.2 on 2023-05-16 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0002_autoria_delete_authgroup_delete_authgrouppermissions_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autoria',
        ),
    ]