# Generated by Django 5.1.2 on 2024-11-29 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Endereço', 'verbose_name_plural': 'Endereços'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Cidade', 'verbose_name_plural': 'Cidades'},
        ),
    ]