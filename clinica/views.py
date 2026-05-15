from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Medico, Consulta
from .forms import ConsultaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def excluir_consulta(request, pk):
    # Buscamos a consulta ou retornamos erro 404 se não existir
    consulta = get_object_or_404(Consulta, pk=pk)
    
    if request.method == 'POST':
        # Se o usuário confirmou (clicou no botão do formulário)
        nome_paciente = consulta.paciente_nome
        consulta.delete()
        messages.success(request, f'Agendamento de {nome_paciente} cancelado com sucesso.')
        return redirect('agenda')
        
    # Se for um acesso via GET (abrir a página), mostramos a confirmação
    return render(request, 'clinica/confirmar_exclusao.html', {'consulta': consulta})

@login_required
def editar_consulta(request, pk):
    # Buscamos a consulta pelo ID (pk = Primary Key) ou retornamos erro 404
    consulta = get_object_or_404(Consulta, pk=pk)
    
    if request.method == 'POST':
        # Aqui passamos o 'instance=consulta', que diz ao Django:
        # "Não crie uma nova, salve por cima desta que já existe!"
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, f'Consulta de {consulta.paciente_nome}, autorizada com sucesso!' )
            return redirect('agenda')
    else:
        # Carregamos o formulário já preenchido com os dados da consulta
        form = ConsultaForm(instance=consulta)
    
    return render(request, 'clinica/novo_agendamento.html', {'form': form, 'editando': True})

def listar_medicos(request):
    # Buscamos todos os médicos no banco de dados
    medicos = Medico.objects.all()
    
    # Enviamos esses dados para um arquivo HTML (Template)
    return render(request, 'clinica/medicos.html', {'medicos': medicos})

@login_required
def agenda_clinica(request): 
    # Pegamos a data/hora exata de agora
    agora = timezone.now()
    
    # Filtramos: consultas onde a data_hora é maior ou igual a "agora"
    # E ordenamos para a mais próxima aparecer primeiro
    proximas_consultas = Consulta.objects.filter(data_hora__gte=agora).order_by('data_hora')

    
    return render(request, 'clinica/agenda.html', {'consultas': proximas_consultas})
@login_required
def novo_agendamento(request):
    #Tentar pegar o ID do médico da URL
    medico_id = request.GET.get('medico')

    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save() # Salva no banco de dados
            return redirect('agenda') # Volta para a lista de consultas
    else:
        #Se houver um ID na URL, já iniciamos o formulario com esse médico
        initial_data = {}
        if medico_id:
            initial_data['medico'] = medico_id
        form = ConsultaForm(initial=initial_data)
    
    return render(request, 'clinica/novo_agendamento.html', {'form': form})

def index(request):
    total_medicos = Medico.objects.count()
    total_consultas = Consulta.objects.count()

    contexto = {
        'qtd_medicos': total_medicos,
        'qtd_consultas': total_consultas,
    }

    return render(request, 'clinica/index.html', contexto)