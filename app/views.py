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
from app.forms import Form_cad_empresa, Form_cad_equipes, Form_cad_fornecedores,Form_cad_setores,Form_cad_dpo
from app.models import Cad_empresa, Cad_equipes, Cad_fornecedores, Cad_setores, Cad_dpo


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
    return render(request,"dados-previos.html")
    #return render(request,"ui-form-elements.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
