from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from meu_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signup/aluno/', views.aluno_signup, name='aluno_signup'),
    path('signup/empresa/', views.empresa_signup, name='empresa_signup'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile_redirect/', views.profile_redirect, name='profile_redirect'),
    path('servicos/', views.servicos, name='servicos'),
    path('servicos/criar/', views.criar_servico, name='criar_servico'),
    path('servicos-da-empresa/', views.servicosDaEmpresa, name='servicosDaEmpresa'),
    path('servicos/<int:servico_id>/candidatar/', views.candidatar_servico, name='candidatar_servico'),
    path('servicos/<int:servico_id>/candidaturas/', views.visualizar_candidaturas, name='visualizar_candidaturas'),
    path('servicos/<int:servico_id>/candidaturas/', views.visualizar_candidaturas, name='visualizar_candidaturas'),
    path('aluno/<int:aluno_id>/', views.perfil_aluno, name='perfil_aluno'),
    
]
