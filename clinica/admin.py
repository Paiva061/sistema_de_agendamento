from django.contrib import admin
from .models import Especialidade, Medico, Consulta

@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    # O que aparece na listagem principal
    list_display = ('nome', 'crm', 'especialidade')
    # Filtros laterais para facilitar a navegação
    list_filter = ('especialidade',)
    # Barra de busca por nome ou CRM
    search_fields = ('nome', 'crm')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente_nome', 'medico', 'data_hora', 'duracao_minutos')
    list_filter = ('medico', 'data_hora')
    search_fields = ('paciente_nome',)
    
    # Isso aqui organiza o formulário de criação em "caixas"
    fieldsets = (
        ('Informações do Paciente', {
            'fields': ('paciente_nome',)
        }),
        ('Detalhes do Agendamento', {
            'fields': ('medico', 'data_hora', 'duracao_minutos')
        }),
        ('Notas Médicas', {
            'fields': ('observacoes',),
            'classes': ('collapse',) # Deixa essa parte recolhida para limpar o visual
        }),
    )
