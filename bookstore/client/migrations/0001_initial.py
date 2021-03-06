# Generated by Django 3.1.7 on 2021-03-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('phone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('address', models.CharField(max_length=255, verbose_name='Endereço')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
        ),
    ]
