from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Aluno, Empresa, Servico
from datetime import date, datetime

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

class DateInput(forms.DateInput):
    input_type = 'date'

    def format_value(self, value):
        if isinstance(value, (datetime, date)):
            return value.strftime('%Y-%m-%d')
        return value

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['titulo', 'descricao', 'prazo', 'preco']
        widgets = {
            'prazo': DateInput(),
        }

    def clean_prazo(self):
        prazo = self.cleaned_data.get('prazo')
        if prazo and prazo <= date.today():
            raise forms.ValidationError('O prazo deve ser posterior ao dia de hoje.')
        return prazo
