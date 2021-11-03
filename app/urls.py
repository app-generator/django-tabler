# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from app.views import index,cadastro_setores,cadastrar_setor,cadastro_equipes,cadastro_fornecedores,cadastro_dpo,cadastro_empresa,create, dados_previos, itens_auditaveis,fator_de_risco,mapeamento,documentos,treinamento,relatorio,edit,update,delete

urlpatterns = [
    # The home page
    path('', index, name='home'),
    path('cadastro_setores/',cadastro_setores, name='cadastro_setores'),
    path('cadastrar_setor/',cadastrar_setor, name='cadastrar_setor'),
    path('cadastro_equipes/',cadastro_equipes, name='cadastro_equipes'),
    path('cadastro_fornecedores/',cadastro_fornecedores, name='cadastro_fornecedores'),
    path('cadastro_dpo/',cadastro_dpo, name='cadastro_dpo'),
    path('cadastro_empresa/',cadastro_empresa, name='cadastro_empresa'),
    path('dados_previos/',dados_previos, name='dados_previos'),
    path('itens_auditaveis/',itens_auditaveis, name='itens_auditaveis'),
    path('fator_de_risco/',fator_de_risco, name='fator_de_risco'),
    path('relatorio/',relatorio, name='relatorio'),
    path('mapeamento/',mapeamento, name='mapeamento'),
    path('documentos/',documentos, name='documentos'),
    path('treinamento/',treinamento, name='treinamento'),
    path('create/',create, name='create'),    
    path('edit/<int:pk>/',edit, name='edit'),
    path('update/<int:pk>/',update, name='update'),
    path('delete/<int:pk>/',delete, name='delete'),
]
