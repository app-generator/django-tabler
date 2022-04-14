# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app.forms import *
from app.models import *

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")


@login_required(login_url="/login/")
def cadastro_empresa(request):
    data = {}
    data['form'] = Form_cad_empresa()
    data['db'] = Cad_empresa.objects.all()
    return render(request,"cadastro-empresa.html",data)


@login_required(login_url="/login/")
def fator_de_risco(request):
    data = {}
    data['form'] = Form_fator_de_risco
    data['db'] = Cad_fator_de_risco.objects.all()
    return render(request,"fator-de-risco.html",data)

@login_required(login_url="/login/")
def relatorio(request):
    return render(request,"relatorio.html")

@login_required(login_url="/login/")
def documentos(request):
    #data = {}
    #data['form'] = Form_documentos
    #data['db'] = Cad_Mapeamento.objects.all()
    return render(request,"documentos.html")
    

@login_required(login_url="/login/")
def treinamento(request):
    #data = {}
    #data['form'] = Form_documentos
    #data['db'] = Cad_Mapeamento.objects.all()
    return render(request,"treinamento.html")

@login_required(login_url="/login/")
def cadastro_setores(request):
        data = {}
        data['db'] = Cad_setores.objects.all()
        return render(request,"cadastro-setores.html",data)

@login_required(login_url="/login/")
def cadastrar_setor(request):
    data = {}
    data['form'] = Form_cad_setores
    return render(request,"cadastrar-setor.html",data)

@login_required(login_url="/login/")
def create_setor(request):
    form = Form_cad_setores(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_setores')

@login_required(login_url="/login/")
def edit_setor(request,pk):
    data = {}
    data['db'] = Cad_setores.objects.get(pk=pk)
    data['form'] = Form_cad_setores(instance=data['db'])
    return render(request,'cadastrar-setor.html',data)

@login_required(login_url="/login/")
def update_setor(request,pk):
    data = {}
    data['db'] = Cad_setores.objects.get(pk=pk)
    form = Form_cad_setores(request.POST or None,instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('cadastro_setores')

@login_required(login_url="/login/")
def delete_setor(request,pk):
    db = Cad_setores.objects.get(pk=pk)
    db.delete()
    return redirect('cadastro_setores')

@login_required(login_url="/login/")
def cadastro_equipes(request):
    data = {}
    #data['form'] = Form_cad_equipes
    data['db'] = Cad_equipes.objects.all()
    return render(request,"cadastro-equipes.html",data)

@login_required(login_url="/login/")
def cadastrar_equipe(request):
    data = {}
    data['form'] = Form_cad_equipes
    return render(request,"cadastrar-equipe.html",data)
    

@login_required(login_url="/login/")
def create_equipe(request):
    form = Form_cad_equipes(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_equipes')

@login_required(login_url="/login/")
def edit_equipe(request,pk):
    data = {}
    data['db'] = Cad_equipes.objects.get(pk=pk)
    data['form'] = Form_cad_equipes(instance=data['db'])
    return render(request,'cadastrar-equipe.html',data)

@login_required(login_url="/login/")
def update_equipe(request,pk):
    data = {}
    data['db'] = Cad_equipes.objects.get(pk=pk)
    form = Form_cad_equipes(request.POST or None,instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('cadastro_equipes')

@login_required(login_url="/login/")
def delete_equipe(request,pk):
    db = Cad_equipes.objects.get(pk=pk)
    db.delete()
    return redirect('cadastro_equipes')

@login_required(login_url="/login/")
def cadastro_dpo(request):
    data = {}
    data['db'] = Cad_dpo.objects.all()
    return render(request,"cadastro-dpo.html",data)

@login_required(login_url="/login/")
def cadastrar_dpo(request):
    data = {}
    data['form'] = Form_cad_dpo
    return render(request,"cadastrar-dpo.html",data)

@login_required(login_url="/login/")
def create_dpo(request):
    form = Form_cad_dpo(request.POST or None)
    if form.is_valid():
        form.save()
    #else:
        #print("erro")
    return redirect('cadastro_dpo')

@login_required(login_url="/login/")
def edit_dpo(request,pk):
    data = {}
    data['db'] = Cad_dpo.objects.get(pk=pk)
    data['form'] = Form_cad_dpo(instance=data['db'])
    return render(request,'cadastrar-dpo.html',data)

@login_required(login_url="/login/")
def update_dpo(request,pk):
    data = {}
    data['db'] = Cad_dpo.objects.get(pk=pk)
    form = Form_cad_dpo(request.POST or None,instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('cadastro_dpo')

@login_required(login_url="/login/")
def delete_dpo(request,pk):
    db = Cad_dpo.objects.get(pk=pk)
    db.delete()
    return redirect('cadastro_dpo')

@login_required(login_url="/login/")
def cadastro_fornecedores(request):
    data = {}
    data['form'] = Form_cad_fornecedores
    data['db'] = Cad_fornecedores.objects.all()
    return render(request,"cadastro-fornecedores.html",data)

@login_required(login_url="/login/")
def cadastrar_fornecedores(request):
    data = {}
    data['form'] = Form_cad_fornecedores
    return render(request,"cadastrar-fornecedores.html",data)

@login_required(login_url="/login/")
def create_fornecedores(request):
    form = Form_cad_fornecedores(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_fornecedores')

@login_required(login_url="/login/")
def edit_fornecedores(request,pk):
    data = {}
    data['db'] = Cad_fornecedores.objects.get(pk=pk)
    data['form'] = Form_cad_fornecedores(instance=data['db'])
    return render(request,'cadastrar-fornecedores.html',data)

@login_required(login_url="/login/")
def update_fornecedores(request,pk):
    data = {}
    data['db'] = Cad_fornecedores.objects.get(pk=pk)
    form = Form_cad_fornecedores(request.POST or None,instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('cadastro_fornecedores')

@login_required(login_url="/login/")
def delete_fornecedores(request,pk):
    db = Cad_fornecedores.objects.get(pk=pk)
    db.delete()
    return redirect('cadastro_fornecedores')

@login_required(login_url="/login/")
def dados_previos(request):
    data = {}
    data['form'] = Form_dados_previos
    data['db'] = Cad_dados_previos.objects.all()
    return render(request,"dados-previos.html",data)
    
@login_required(login_url="/login/")
def edit_dados_previos(request,pk):
    data = {}
    data['db'] = Cad_dados_previos.objects.get(pk=pk)
    data['form'] = Form_dados_previos(instance=data['db'])
    return render(request,'cadastro-dados-previos.html',data)

@login_required(login_url="/login/")
def update_dados_previos(request,pk):
    data = {}
    data['db'] = Cad_dados_previos.objects.get(pk=pk)
    form = Form_dados_previos(request.POST or None,instance=data['db'])
    if form.is_valid():
        form.save()
    else:
        print("erro")
    return redirect('/dados_previos/')
@login_required(login_url="/login/")
def create_dados_previos(request):
    form = Form_dados_previos(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('dados_previos')
  
@login_required(login_url="/login/")
def itens_auditaveis(request):
    data = {}
    data['form'] = Form_itens_auditaveis
    data['db'] = Cad_itens_auditaveis.objects.all() 
    return render(request,"itens-auditaveis.html",data)

@login_required(login_url="/login/")
def edit_itens_auditaveis(request,pk):
    data = {}
    data['db'] = Cad_itens_auditaveis.objects.get(pk=pk)
    data['form'] = Form_itens_auditaveis(instance=data['db'])
    return render(request,'edit-itens-auditaveis.html',data)

@login_required(login_url="/login/")
def update_itens_auditaveis(request,pk):
    data = {}
    data['db'] = Cad_itens_auditaveis.objects.get(pk=pk)
    form = Form_itens_auditaveis(request.POST or None,instance=data['db'])
    if form.is_valid():
        form.save()
    else:
        print("erro")
    return redirect("itens_auditaveis")

@login_required(login_url="/login/")
def create_itens_auditaveis(request):
    form = Form_itens_auditaveis(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('itens_auditaveis')

@login_required(login_url="/login/")
def mapeamento(request):
    data = {}
    data['form'] = Form_mapeamento
    data['db'] = Cad_Mapeamento.objects.all()
    return render(request,"mapeamento.html",data)

@login_required(login_url="/login/")
def cadastrar_mapeamento(request):
    data = {}
    data['form'] = Form_mapeamento
    return render(request,"cadastrar-mapeamento.html",data)

@login_required(login_url="/login/")
def create_mapeamento(request):
    form = Form_mapeamento(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('mapeamento')

@login_required(login_url="/login/")
def edit_mapeamento(request,pk):
    data = {}
    data['db'] = Cad_Mapeamento.objects.get(pk=pk)
    data['form'] = Form_mapeamento(instance=data['db'])
    return render(request,'cadastrar-mapeamento.html',data)

@login_required(login_url="/login/")
def update_mapeamento(request,pk):
    data = {}
    data['db'] = Cad_Mapeamento.objects.get(pk=pk)
    form = Form_mapeamento(request.POST or None,instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('mapeamento')

@login_required(login_url="/login/")
def delete_mapeamento(request,pk):
    db = Cad_Mapeamento.objects.get(pk=pk)
    db.delete()
    return redirect('mapeamento')
