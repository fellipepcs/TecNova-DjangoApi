# Generated by Django 3.2.9 on 2021-11-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='eletrodomesticoCliente',
            new_name='eletrodomestico',
        ),
        migrations.AlterField(
            model_name='clientes',
            name='enderecoCliente',
            field=models.CharField(max_length=80),
        ),
    ]
