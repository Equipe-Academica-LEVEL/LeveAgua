# Generated by Django 5.0.7 on 2024-08-06 04:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumo_agua', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControleDeIrrigacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.DurationField()),
                ('tolerancia_litros', models.BigIntegerField()),
                ('tolerancia_tempo', models.BigIntegerField()),
                ('consumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controle', to='consumo_agua.consumo')),
            ],
        ),
    ]
