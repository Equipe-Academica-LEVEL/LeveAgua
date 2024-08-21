# Generated by Django 5.1 on 2024-08-20 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_usuarios', '0002_alter_endereco_cep_alter_endereco_distrito_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('litros', models.BigIntegerField()),
                ('data', models.DateTimeField()),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumo_endereco', to='app_usuarios.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='ControleDeIrrigacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.DurationField()),
                ('tolerancia_litros', models.BigIntegerField()),
                ('tolerancia_tempo', models.BigIntegerField()),
                ('consumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controleIrrigacao_consumo', to='app_consumo.consumo')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controleIrrigacao_endereco', to='app_usuarios.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='FaturaAgua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('periodo', models.DateField()),
                ('dataDeVencimento', models.DateField()),
                ('dataDeEmissao', models.DateField()),
                ('consumo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_consumo.consumo')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fatura_endereco', to='app_usuarios.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.TextField()),
                ('data', models.DateField()),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manutencao_endereco', to='app_usuarios.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='RelatorioDeConsumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.DurationField()),
                ('modelo', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatorio_endereco', to='app_usuarios.endereco')),
            ],
        ),
    ]
