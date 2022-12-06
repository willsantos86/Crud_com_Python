from django.forms import ModelForm
from app.models import Dados

class DadosForm(ModelForm):
    class Meta:
        model = Dados
        fields = ['nome', 'email', 'telefone', 'cpf', 'data_nascimento']