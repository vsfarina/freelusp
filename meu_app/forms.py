from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Aluno, Empresa, Servico

class AlunoSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user

class EmpresaSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        if commit:
            user.save()
        return user

class AlunoProfileForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'cpf', 'nome_completo', 'faculdade', 
            'curso_graduacao', 'ano_ingresso', 
            'telefone', 'experiencias', 'foto_perfil'
        ]

class EmpresaProfileForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_completo', 'telefone', 'cpf_cnpj', 'foto_perfil']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['titulo', 'descricao', 'preco', 'prazo']
