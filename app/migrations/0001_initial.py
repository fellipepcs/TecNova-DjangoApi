# Generated by Django 3.2.9 on 2021-11-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCliente', models.CharField(max_length=30)),
                ('telefonteCliente', models.CharField(max_length=30)),
                ('enderecoCliente', models.CharField(max_length=30)),
                ('eletrodomesticoCliente', models.CharField(max_length=30)),
            ],
        ),
    ]
