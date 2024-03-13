from django.db import models

class Profissional(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, default = '')
    email = models.EmailField()
    especialidade = models.CharField(max_length=255,default = '')
    telefone = models.CharField(max_length=15, default = '')
    
    def __str__(self):
        return f'Nome: {self.nome} | Email: {self.email}'

