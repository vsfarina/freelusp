from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AlunoSignUpForm, EmpresaSignUpForm, AlunoProfileForm, EmpresaProfileForm, ServicoForm
from .models import Servico

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def aluno_signup(request):
    if request.method == 'POST':
        user_form = AlunoSignUpForm(request.POST)
        profile_form = AlunoProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = AlunoSignUpForm()
        profile_form = AlunoProfileForm()
    return render(request, 'aluno_signup.html', {'user_form': user_form, 'profile_form': profile_form})

def empresa_signup(request):
    if request.method == 'POST':
        user_form = EmpresaSignUpForm(request.POST)
        profile_form = EmpresaProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = EmpresaSignUpForm()
        profile_form = EmpresaProfileForm()
    return render(request, 'empresa_signup.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def servicos(request):
    if not request.user.is_student:
        return redirect('home')
    servicos = Servico.objects.all()
    return render(request, 'meu_app/servicos.html', {'servicos': servicos})

@login_required
def criar_servico(request):
    if not request.user.is_company:
        return redirect('home')
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.empresa = request.user.empresa 
            servico.save()
            return redirect('servicos')
    else:
        form = ServicoForm()
    return render(request, 'meu_app/criar_servico.html', {'form': form})


def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'meu_app/servicos.html', {'servicos': servicos})

@login_required
def profile_redirect(request):
    if request.user.is_company:
        return redirect('criar_servico')
    elif request.user.is_student:
        return redirect('servicos')
    return redirect('home')
