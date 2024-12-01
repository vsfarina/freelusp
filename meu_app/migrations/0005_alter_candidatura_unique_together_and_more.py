# Generated by Django 5.1.2 on 2024-11-28 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_app', '0004_candidatura'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='candidatura',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='candidatura',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meu_app.aluno'),
        ),
        migrations.AlterField(
            model_name='candidatura',
            name='mensagem',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidatura',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meu_app.servico'),
        ),
        migrations.CreateModel(
            name='Acordo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_acordo', models.DateTimeField(auto_now_add=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meu_app.aluno')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meu_app.empresa')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meu_app.servico')),
            ],
        ),
        migrations.CreateModel(
            name='Conversa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField(auto_now_add=True)),
                ('mensagens', models.TextField(blank=True, null=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meu_app.aluno')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meu_app.empresa')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meu_app.servico')),
            ],
        ),
    ]