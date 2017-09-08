# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 13:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empresa', models.CharField(blank=True, choices=[('ASTERBOX', 'ASTERBOX'), ('JUAN', 'JUAN'), ('IFF', 'IFF'), ('GLS_ARGENTINA', 'GLS_ARGENTINA'), ('ISM', 'ISM')], max_length=30, null=True)),
                ('Abonos', models.CharField(blank=True, max_length=4, null=True)),
                ('Descripcion_corta', models.TextField(blank=True, max_length=250, null=True)),
                ('Cuenta_Activa', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
