from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from datetime import date

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='meu_app_users_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='meu_app_users_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cpf = models.CharField(max_length=14, unique=True)
    nome_completo = models.CharField(max_length=255)
    faculdade = models.CharField(max_length=255)
    curso_graduacao = models.CharField(max_length=255)
    ano_ingresso = models.IntegerField()
    telefone = models.CharField(max_length=20)
    experiencias = models.TextField()
    foto_perfil = models.URLField(max_length=200, blank=True)

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telefone = models.CharField(max_length=20)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    nome_completo = models.CharField(max_length=255)
    foto_perfil = models.URLField(max_length=200, blank=True)

class Servico(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    prazo = models.DateField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='servicos')

    def __str__(self):
        return self.titulo

from django.db import models

class Candidatura(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    mensagem = models.TextField(blank=True, null=True)
    data_candidatura = models.DateTimeField(auto_now_add=True)  # Defina o campo data_candidatura

    def __str__(self):
        return f'Candidatura de {self.aluno} para {self.servico}'

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'cpf',
            'nome_completo',
            'faculdade',
            'curso_graduacao',
            'ano_ingresso',
            'telefone',
            'experiencias',
            'foto_perfil'
        ]

