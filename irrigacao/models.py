# /----------------------------------------\ #
# | Gerenciamento do controle da irrigação | #
# \----------------------------------- ----/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.db import models # Necessário para criação de classes
from consumo_agua.models import Consumo # Importa a classe "Consumo" criada no model do app "consumo_agua"

# -------------------------------------------------------------------------------------------------------------------------------
# CLASSES
class ControleDeIrrigacao(models.Model): # Classe criada a partir do padrão django "models.Model"
    periodo = models.DurationField() # "models.DurationField" determina um intervalo de tempo
    tolerancia_litros = models.BigIntegerField() # "models.BigIntegerField" é utilizado para grandes dados numéricos
    tolerancia_tempo = models.BigIntegerField() # ~ ~ ~ ~ ~ ~
    consumo = models.ForeignKey(Consumo, on_delete=models.CASCADE, related_name='controle') # "Consumo, on_delete=models.CASCADE" significa que o Controle de Irrigação correspondente ao Consumo será apagado caso o Consumo seja removido