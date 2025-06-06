# Generated by Django 5.1.5 on 2025-03-29 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0003_comentario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.TextField(verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='status',
            field=models.CharField(choices=[('EM_ABERTO', 'Em Aberto'), ('CONCLUIDA', 'Concluida')], default='EM_ABERTO', max_length=10, verbose_name='Status'),
        ),
    ]
