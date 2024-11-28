from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoSignUpForm, EmpresaSignUpForm, AlunoProfileForm, EmpresaProfileForm, ServicoForm
from .models import Servico, Empresa, Aluno, Candidatura
from django.utils import timezone
from django.db.models import Q

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

    query = request.GET.get('q')
    preco_min = request.GET.get('preco_min')
    preco_max = request.GET.get('preco_max')
    prazo_max = request.GET.get('prazo_max')

    servicos = Servico.objects.all()

    if query:
        servicos = servicos.filter(
            Q(titulo__icontains=query) |
            Q(descricao__icontains=query)
        )

    if preco_min:
        servicos = servicos.filter(preco__gte=preco_min)

    if preco_max:
        servicos = servicos.filter(preco__lte=preco_max)

    if prazo_max:
        servicos = servicos.filter(prazo__gte=prazo_max)

    user = request.user
    servicos_info = []
    for servico in servicos:
        ja_candidatado = servico.candidatura_set.filter(aluno=user.aluno).exists()
        servicos_info.append({
            'servico': servico,
            'ja_candidatado': ja_candidatado
        })

    return render(request, 'meu_app/servicos.html', {'servicos_info': servicos_info})

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
            return redirect('servicosDaEmpresa')
    else:
        form = ServicoForm()
    return render(request, 'meu_app/criar_servico.html', {'form': form})

def listar_servicos(request):
    if not request.user.is_company:
        return redirect('home')
    empresa = request.user.empresa
    servicos = Servico.objects.filter(empresa=empresa)
    return render(request, 'meu_app/servicosDaEmpresa.html', {'servicos': servicos})

@login_required
def excluir_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id, empresa__user=request.user)
    servico.delete()
    return redirect('servicosDaEmpresa')


@login_required
def profile_redirect(request):
    if request.user.is_company:
        return redirect('servicosDaEmpresa')
    elif request.user.is_student:
        return redirect('servicos')
    return redirect('home')


@login_required
def servicosDaEmpresa(request):
    if request.user.is_company:
        empresa = Empresa.objects.get(user=request.user)
        servicos = Servico.objects.filter(empresa=empresa)
    else:
        servicos = Servico.objects.none()
    return render(request, 'servicosDaEmpresa.html', {'servicos': servicos})


@login_required
def candidatar_servico(request, servico_id):
    if not request.user.is_student:
        return redirect('home')

    servico = get_object_or_404(Servico, id=servico_id)
    aluno = Aluno.objects.get(user=request.user)

    if Candidatura.objects.filter(aluno=aluno, servico=servico).exists():
        return redirect('servicos')

    if request.method == 'POST':
        mensagem = request.POST.get('mensagem', '')
        candidatura = Candidatura.objects.create(
            aluno=aluno,
            servico=servico,
            mensagem=mensagem,
            data_candidatura=timezone.now()
        )
        return redirect('servicos')

    return render(request, 'meu_app/servicos.html', {'servico': servico})


@login_required
def listar_candidatos(request, servico_id):
    if not request.user.is_company:
        return redirect('home')
    servico = get_object_or_404(Servico, id=servico_id, empresa=request.user.empresa)
    candidaturas = Candidatura.objects.filter(servico=servico).select_related('aluno__user')
    return render(request, 'meu_app/listar_candidatos.html', {'servico': servico, 'candidaturas': candidaturas})


@login_required
def visualizar_candidaturas(request, servico_id):
    if not request.user.is_company:
        return redirect('home')
    servico = get_object_or_404(Servico, id=servico_id, empresa=request.user.empresa)
    candidaturas = Candidatura.objects.filter(servico=servico)
    return render(request, 'meu_app/visualizar_candidaturas.html', {'servico': servico, 'candidaturas': candidaturas})


@login_required
def perfil_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    return render(request, 'meu_app/perfil_aluno.html', {'aluno': aluno})
