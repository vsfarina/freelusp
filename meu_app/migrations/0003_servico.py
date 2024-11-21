# Generated by Django 5.1.2 on 2024-11-21 00:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_app', '0002_aluno_foto_perfil_empresa_foto_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('prazo', models.DateField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicos', to='meu_app.empresa')),
            ],
        ),
    ]