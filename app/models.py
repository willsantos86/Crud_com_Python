from django.db import models

# Create your models here.
class Dados(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

