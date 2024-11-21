from django.db import models
from django.contrib.auth.models import AbstractUser

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
    foto_perfil = models.URLField(max_length=200, blank=True)  # Certifique-se de que o campo está aqui

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telefone = models.CharField(max_length=20)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    nome_completo = models.CharField(max_length=255)
    foto_perfil = models.URLField(max_length=200, blank=True)  # Certifique-se de que o campo está aqui
