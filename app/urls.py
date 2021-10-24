# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('cadastro_setores/',views.cadastro_setores, name='cadastro_setores'),
    path('cadastro_equipes/',views.cadastro_equipes, name='cadastro_equipes'),
    path('cadastro_fornecedores/',views.cadastro_fornecedores, name='cadastro_fornecedores'),
    path('cadastro_dpo/',views.cadastro_dpo, name='cadastro_dpo'),
    path('cadastro_empresa/',views.cadastro_empresa, name='cadastro_empresa')
]
