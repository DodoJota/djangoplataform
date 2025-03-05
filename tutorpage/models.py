from django.db import models
    
class NotaAula(models.Model):
    aula = models.CharField(max_length=255, unique=True)  # Identificador único da aula
    notas = models.TextField()