# Generated by Django 5.1.5 on 2025-02-25 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0007_alter_ocorrencia_matricula_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='ordem_de_servico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ocorrencias', to='ocorrencia.ordemdeservico'),
        ),
    ]
