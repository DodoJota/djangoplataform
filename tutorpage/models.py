from django.db import models

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email  # Retorna o email ao imprimir o objeto
    
class NotaAula(models.Model):
    aula = models.CharField(max_length=255, unique=True)  # Identificador único da aula
    notas = models.TextField()