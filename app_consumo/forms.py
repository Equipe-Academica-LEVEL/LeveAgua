# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django import forms
from .models import Consumo, FaturaAgua, RelatorioDeConsumo, ControleDeIrrigacao, Manutencao
from datetime import time, timedelta

# -------------------------------------------------------------------------------------------------------------------------------
# FORMULARIOS

# Formulário para o Model Consumo
class ConsumoForm(forms.ModelForm):
    class Meta:
        model = Consumo
        fields = ['litros', 'data', 'endereco']
        labels = {
            'litros': 'Litros',
            'data': 'Data de Consumo',
            'endereco': 'Endereço',
        }
    
    def __init__(self, *args, **kwargs):
        super(ConsumoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'label-form'


# Formulário para o Model FaturaAgua
class FaturaAguaForm(forms.ModelForm):
    class Meta:
        model = FaturaAgua
        fields = ['valor', 'periodo', 'dataDeVencimento', 'dataDeEmissao', 'endereco', 'consumo']
        labels = {
            'valor': 'Valor',
            'periodo': 'Período',
            'dataDeVencimento': 'Data de Vencimento',
            'dataDeEmissao': 'Data de Emissão',
            'endereco': 'Endereço',
            'consumo': 'Consumo',
        }
    
    def __init__(self, *args, **kwargs):
        super(FaturaAguaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'label-form'


# Formulário para o Model RelatorioDeConsumo
class RelatorioDeConsumoForm(forms.ModelForm):
    class Meta:
        model = RelatorioDeConsumo
        fields = ['periodo', 'modelo', 'data', 'endereco']
        labels = {
            'periodo': 'Período',
            'modelo': 'Modelo de Relatório',
            'data': 'Data',
            'endereco': 'Endereço',
        }
    
    def __init__(self, *args, **kwargs):
        super(RelatorioDeConsumoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'label-form'


# Formulário para o Model ControleDeIrrigacao
class ControleDeIrrigacaoForm(forms.ModelForm):
    # Define os selects diretamente no forms.py
    inicio_periodo = forms.ChoiceField(
        choices=[(f'{h:02d}:00', f'{h:02d}:00') for h in range(24)],
        label='Início do Período',
        widget=forms.Select(attrs={'class': 'label-form'})
    )
    fim_periodo = forms.ChoiceField(
        choices=[(f'{h:02d}:00', f'{h:02d}:00') for h in range(24)],
        label='Fim do Período',
        widget=forms.Select(attrs={'class': 'label-form'})
    )

    class Meta:
        model = ControleDeIrrigacao
        fields = ['tolerancia_litros', 'endereco']  # Exibir apenas tolerância em litros e endereço
        labels = {
            'tolerancia_litros': 'Tolerância em Litros',
            'endereco': 'Endereço',
        }
    
    def __init__(self, *args, **kwargs):
        super(ControleDeIrrigacaoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'label-form'

        # Reordena os campos para a ordem desejada
        self.fields['inicio_periodo'].widget.attrs['class'] = 'label-form'
        self.fields['fim_periodo'].widget.attrs['class'] = 'label-form'
        self.fields = {
            'inicio_periodo': self.fields['inicio_periodo'],
            'fim_periodo': self.fields['fim_periodo'],
            'tolerancia_litros': self.fields['tolerancia_litros'],
            'endereco': self.fields['endereco'],
        }

    def save(self, commit=True):
        # Pega os valores dos horários de início e fim
        inicio_horario = self.cleaned_data['inicio_periodo']
        fim_horario = self.cleaned_data['fim_periodo']

        # Converte os horários para o tipo `time`
        inicio_time = time(int(inicio_horario.split(':')[0]), 0)
        fim_time = time(int(fim_horario.split(':')[0]), 0)

        # Calcula o período em horas
        periodo_horas = timedelta(hours=fim_time.hour - inicio_time.hour)

        # Cria o objeto Controle de Irrigação com o valor do período
        controle_irrigacao = super().save(commit=False)
        controle_irrigacao.periodo = periodo_horas

        if commit:
            controle_irrigacao.save()

        return controle_irrigacao



# Formulário para o Model Manutencao
class ManutencaoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['motivo', 'data', 'endereco']
        labels = {
            'motivo': 'Motivo',
            'data': 'Data',
            'endereco': 'Endereço',
        }
    
    def __init__(self, *args, **kwargs):
        super(ManutencaoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'label-form'

