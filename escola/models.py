from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'

class Cadeira(models.Model):
    cadeira = models.CharField(max_length=30)
    créditos = models.IntegerField()
    lecionada = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name= 'teacher')

    def __str__(self):
        return f'{self.cadeira}: {self.créditos}ETCs'

class Curso(models.Model):
    nome = models.CharField(max_length=40)
    id_curso = models.IntegerField()
    cadeiras = models.ManyToManyField(Cadeira)

    def __str__(self):
        return f'{self.nome} - {self.id_curso}'

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}({self.idade}anos)'