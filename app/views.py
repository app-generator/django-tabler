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
from app.forms import Form_cad_empresa,Form_cad_setores


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")
    
@login_required(login_url="/login/")
def cadastro_setores(request):
    data = {}
    data['form'] = Form_cad_setores()
    return render(request,"cadastro-setores.html",data)

@login_required(login_url="/login/")
def cadastro_equipes(request):
    return render(request,"cadastro-equipes.html")

@login_required(login_url="/login/")
def cadastro_fornecedores(request):
    return render(request,"cadastro-fornecedores.html")

@login_required(login_url="/login/")
def cadastro_dpo(request):
    return render(request,"cadastro-dpo.html")

@login_required(login_url="/login/")
def cadastro_empresa(request):
    data = {}
    data['form'] = Form_cad_empresa()
    return render(request,"cadastro-empresa.html",data)

@login_required(login_url="/login/")
def create(request):
    form = Form_cad_empresa(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cadastro_empresa')


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
