# /------------------------------------------------\ #
# | Gerenciamento do consumo de água e faturamento | #
# \------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.db import models # Necessário para criação de classes
from usuarios.models import Usuario # Importa a classe "Usuario" criada no model do app "usuarios"

# -------------------------------------------------------------------------------------------------------------------------------
# CLASSES
class Consumo(models.Model): # Classe criada a partir do padrão django "models.Model"
    litros = models.BigIntegerField() # "models.BigIntegerField" é utilizado para grandes dados numéricos
    data = models.DateTimeField() # "models.DateTimeField" é utilizado para armazenar data e hora
    #ligar ao usuario

class FaturaAgua(models.Model): # Classe criada a partir do padrão django "models.Model"
    valor = models.FloatField() # Determina o valor em R$
    consumo = models.OneToOneField(Consumo, on_delete=models.CASCADE) # "Consumo, on_delete=models.CASCADE" significa que a fatura de água correspondente ao Consumo será apagado caso o Consumo seja removido
    periodo = models.DateField()
    dataDeEmissao = models.DateField()
    dataDeVencimento = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='faturas') # "Usuario, on_delete=models.CASCADE" significa que a fatura de água correspondente ao usuário será apagado caso o usuário seja removido

#não armazena este tipo de informação, se calcula!!!
class RelatorioDeConsumo(models.Model): # Classe criada a partir do padrão django "models.Model"
    periodo = models.DurationField() # "models.DurationField" determina um intervalo de tempo
    modelo = models.CharField(max_length=255)
    consumo = models.ForeignKey(Consumo, on_delete=models.CASCADE, related_name='relatorios') # "Consumo, on_delete=models.CASCADE" significa que o Relatório de Consumo correspondente ao Consumo será apagado caso o Consumo seja removido

class ControleDeIrrigacao(models.Model): # Classe criada a partir do padrão django "models.Model"
    periodo = models.DurationField() # "models.DurationField" determina um intervalo de tempo
    tolerancia_litros = models.BigIntegerField() # "models.BigIntegerField" é utilizado para grandes dados numéricos
    tolerancia_tempo = models.BigIntegerField() # ~ ~ ~ ~ ~ ~
    consumo = models.ForeignKey(Consumo, on_delete=models.CASCADE, related_name='controle') # "Consumo, on_delete=models.CASCADE" significa que o Controle de Irrigação correspondente ao Consumo será apagado caso o Consumo seja removido