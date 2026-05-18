from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['medico', 'paciente_nome', 'data_hora', 'duracao_minutos', 'observacoes']
        # Adicionando um calendário visual no campo de data
        widgets = {
            'paciente_nome': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none'}),
            'data_hora': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={
                'type': 'datetime-local', 
                'class': 'w-full p-3 border border-slate-300 rounded-lg'}),
            'medico': forms.Select(attrs={
                'class': 'w-full p-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none'
            }),
            'duracao_minutos': forms.NumberInput(attrs={
                'class': 'w-full p-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none'
            }),
            'observacoes': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full p-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none'
            }),
        }
