# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class Cad_empresa(models.Model):
    nome_fantasia_empresa = models.CharField(max_length=80)
    cnpj_empresa = models.CharField(max_length=18)
    endereco_empresa = models.CharField(max_length=80)
    cidade_empresa = models.CharField(max_length=80)
    cep_empresa = models.CharField(max_length=9)
    estado_empresa = models.CharField(max_length=40)
    telefone_empresa = models.CharField(max_length=15)

class Cad_setores(models.Model):
    setor_nome = models.CharField(max_length=30)
    resposavel_setor = models.CharField(max_length=30)
    cargo_setor = models.CharField(max_length=30)
    contato_setor = models.CharField(max_length=30)

class Cad_equipes(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    responsabilidade = models.CharField(max_length=30)

class Cad_fornecedores(models.Model):
    fornecedor = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=30)
    dpo = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)

class Cad_dpo(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    contato = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)