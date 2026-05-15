from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['medico', 'paciente_nome', 'data_hora', 'duracao_minutos', 'observacoes']
        # Adicionando um calendário visual no campo de data
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'rounded p-2 border'}),
        }
