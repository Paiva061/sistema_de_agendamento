from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=200)
    crm = models.CharField(max_length=20, unique=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"Dr(a). {self.nome} - {self.crm}"

class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='consultas')
    paciente_nome = models.CharField(max_length=200)
    data_hora = models.DateTimeField()
    duracao_minutos = models.PositiveIntegerField(default=30)
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['data_hora']

    def clean(self):
        # Lógica de "Alto Padrão": Evitar sobreposição de horários
        fim_consulta = self.data_hora + timezone.timedelta(minutes=self.duracao_minutos)
        
        conflitos = Consulta.objects.filter(
            medico=self.medico,
            data_hora__lt=fim_consulta,
            data_hora__gte=self.data_hora
        ).exclude(pk=self.pk)

        if conflitos.exists():
            raise ValidationError('Este médico já possui uma consulta agendada para este horário.')

    def __str__(self):
        return f"{self.paciente_nome} com {self.medico} em {self.data_hora}"
