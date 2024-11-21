from django.contrib import admin
from .models import User, Aluno, Empresa

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_student', 'is_company')
    search_fields = ('username', 'email')

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'nome_completo', 'faculdade', 'curso_graduacao', 'ano_ingresso', 'telefone')
    search_fields = ('cpf', 'nome_completo', 'faculdade', 'curso_graduacao')

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefone', 'cpf_cnpj', 'nome_completo')
    search_fields = ('cpf_cnpj', 'nome_completo')

admin.site.register(User, UserAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Empresa, EmpresaAdmin)
