from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=10)

    def __str__(self):
        return self.nome