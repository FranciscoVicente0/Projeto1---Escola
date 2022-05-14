from django.contrib import admin
from .models import Professor,Cadeira, Curso, Aluno

admin.site.register(Professor)
admin.site.register(Cadeira)
admin.site.register(Curso)
admin.site.register(Aluno)