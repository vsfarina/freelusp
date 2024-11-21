from django.contrib import admin
from django.urls import path, include
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
    path('servicos/', views.listar_servicos, name='listar_servicos'),
]
