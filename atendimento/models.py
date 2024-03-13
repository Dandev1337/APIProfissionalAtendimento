from django.db import models
from profissional.models import Profissional

class Atendimento(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    cliente = models.CharField(max_length=255, default = '')
    obs = models.TextField()
    
    def __str__(self):
        return f'Cliente: {self.cliente} | Profissional: {self.profissional}'
