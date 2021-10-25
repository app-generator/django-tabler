# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app.views import index, cadastro_setores,cadastro_equipes,cadastro_fornecedores,cadastro_dpo,cadastro_empresa,create

urlpatterns = [
    # Matches any html file 
    #re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', index, name='home'),
    path('cadastro_setores/',cadastro_setores, name='cadastro_setores'),
    path('cadastro_equipes/',cadastro_equipes, name='cadastro_equipes'),
    path('cadastro_fornecedores/',cadastro_fornecedores, name='cadastro_fornecedores'),
    path('cadastro_dpo/',cadastro_dpo, name='cadastro_dpo'),
    path('cadastro_empresa/',cadastro_empresa, name='cadastro_empresa'),
    path('create/', create, name='create')
]
