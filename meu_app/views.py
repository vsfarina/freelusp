from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import AlunoSignUpForm, EmpresaSignUpForm, AlunoProfileForm, EmpresaProfileForm


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

