# Generated by Django 5.1.5 on 2025-03-29 13:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0002_ocorrencia_plantonista'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comentarios', to=settings.AUTH_USER_MODEL, verbose_name='Plantonista'),
        ),
    ]
