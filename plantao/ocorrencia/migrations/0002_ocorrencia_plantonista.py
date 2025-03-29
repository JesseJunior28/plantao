# Generated by Django 5.1.5 on 2025-03-28 00:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ocorrencia',
            name='plantonista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ocorrencias', to=settings.AUTH_USER_MODEL, verbose_name='Plantonista'),
        ),
    ]
