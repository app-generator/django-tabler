# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.forms import Form_cad_empresa, Form_cad_equipes, Form_cad_fornecedores,Form_cad_setores,Form_cad_dpo,Form_dados_previos, Form_fator_de_risco,Form_itens_auditaveis,Form_mapeamento
from app.models import Cad_dados_previos, Cad_empresa, Cad_equipes, Cad_fator_de_risco, Cad_fornecedores, Cad_setores, Cad_dpo, Cad_itens_auditaveis,Cad_Mapeamento


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")
    
@login_required(login_url="/login/")
def cadastro_setores(request):
        data = {}
        data['form'] = Form_cad_setores
        data['db'] = Cad_setores.objects.all()
        return render(request,"cadastro-setores.html",data)


@login_required(login_url="/login/")
def cadastro_equipes(request):
    data = {}
    data['form'] = Form_cad_equipes
    data['db'] = Cad_equipes.objects.all()
    return render(request,"cadastro-equipes.html",data)

@login_required(login_url="/login/")
def cadastro_fornecedores(request):
    data = {}
    data['form'] = Form_cad_fornecedores
    data['db'] = Cad_fornecedores.objects.all()
    return render(request,"cadastro-fornecedores.html",data)

@login_required(login_url="/login/")
def cadastro_dpo(request):
    data = {}
    data['form'] = Form_cad_dpo
    data['db'] = Cad_dpo.objects.all()
    return render(request,"cadastro-dpo.html",data)

@login_required(login_url="/login/")
def cadastro_empresa(request):
    data = {}
    data['form'] = Form_cad_empresa()
    data['db'] = Cad_empresa.objects.all()
    return render(request,"cadastro-empresa.html",data)

@login_required(login_url="/login/")
def create(request):
    form = Form_cad_empresa(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cadastro_empresa')
    
@login_required(login_url="/login/")
def dados_previos(request):
    data = {}
    data['form'] = Form_dados_previos
    data['db'] = Cad_dados_previos.objects.all()
    return render(request,"dados-previos.html",data)

@login_required(login_url="/login/")
def itens_auditaveis(request):
    data = {}
    data['form'] = Form_itens_auditaveis
    data['db'] = Cad_itens_auditaveis.objects.all()
    return render(request,"itens-auditaveis.html",data)

@login_required(login_url="/login/")
def fator_de_risco(request):
    data = {}
    data['form'] = Form_fator_de_risco
    data['db'] = Cad_fator_de_risco.objects.all()
    return render(request,"fator-de-risco.html",data)

@login_required(login_url="/login/")
def mapeamento(request):
    data = {}
    data['form'] = Form_mapeamento
    data['db'] = Cad_Mapeamento.objects.all()
    return render(request,"mapeamento.html",data)