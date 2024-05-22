
from django.forms import ModelForm
from .models import app


class appForm(ModelForm):
    
    class Meta:
        model = app  # Usando a classe Ap do arquivo models.py
        fields = "__all__"
