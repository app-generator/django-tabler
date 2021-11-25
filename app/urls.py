# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
#from app.views import create_setor, index,cadastro_mapeamentos,cadastro_fornecedores,cadastro_empresa,dados_previos, itens_auditaveis,fator_de_risco,mapeamento,documentos,treinamento,relatorio,cadastro_setores,cadastrar_setor,edit_setor,update_setor,delete_setor,cadastrar_mapeamento,create_mapeamento,edit_mapeamento,update_mapeamento,delete_mapeamento,cadastro_dpo,cadastrar_dpo,create_dpo,edit_dpo,update_dpo,delete_dpo
from app.views import *
urlpatterns = [
    # The home page
    path('', index, name='home'),
    #path('fator_de_risco/',fator_de_risco, name='fator_de_risco'),
    path('relatorio/',relatorio, name='relatorio'),    
    path('documentos/',documentos, name='documentos'),
    path('treinamento/',treinamento, name='treinamento'),
    # Setores
    path('cadastro_setores/',cadastro_setores, name='cadastro_setores'),
    path('cadastrar_setor/',cadastrar_setor, name='cadastrar_setor'),
    path('create_setor/',create_setor, name='create_setor'),    
    path('edit_setor/<int:pk>/',edit_setor, name='edit_setor'),
    path('update_setor/<int:pk>/',update_setor, name='update_setor'),
    path('delete_setor/<int:pk>/',delete_setor, name='delete_setor'),
    #Equipes
    path('cadastro_equipes/',cadastro_equipes, name='cadastro_equipes'),
    path('cadastrar_equipe/',cadastrar_equipe, name='cadastrar_equipe'),
    path('create_equipe/',create_equipe, name='create_equipe'),    
    path('edit_equipe/<int:pk>/',edit_equipe, name='edit_equipe'),
    path('update_equipe/<int:pk>/',update_equipe, name='update_equipe'),
    path('delete_equipe/<int:pk>/',delete_equipe, name='delete_equipe'),
    # DPO
    path('cadastro_dpo/',cadastro_dpo, name='cadastro_dpo'),
    path('cadastrar_dpo/',cadastrar_dpo, name='cadastrar_dpo'),
    path('create_dpo/',create_dpo, name='create_dpo'),    
    path('edit_dpo/<int:pk>/',edit_dpo, name='edit_dpo'),
    path('update_dpo/<int:pk>/',update_dpo, name='update_dpo'),
    path('delete_dpo/<int:pk>/',delete_dpo, name='delete_dpo'),
    # Cadastro da Empresa
    path('cadastro_empresa/',cadastro_empresa, name='cadastro_empresa'),
    # Cadastro de Fornecedores
    path('cadastro_fornecedores/',cadastro_fornecedores, name='cadastro_fornecedores'),
    path('cadastrar_fornecedores/',cadastrar_fornecedores, name='cadastrar_fornecedores'),
    path('create_fornecedores/',create_fornecedores, name='create_fornecedores'),    
    path('edit_fornecedores/<int:pk>/',edit_fornecedores, name='edit_fornecedores'),
    path('update_fornecedores/<int:pk>/',update_fornecedores, name='update_fornecedores'),
    path('delete_fornecedores/<int:pk>/',delete_fornecedores, name='delete_fornecedores'),
    # Dados Prévios
    path('dados_previos/',dados_previos, name='dados_previos'),
    path('edit_dados_previos/<int:pk>/',edit_dados_previos, name='edit_dados_previos'),
    path('update_dados_previos/<int:pk>/',update_dados_previos, name='update_dados_previos'),
    path('create_dados_previos/',create_dados_previos, name='create_dados_previos'),
    # Itens Auditáveis
    path('itens_auditaveis/',itens_auditaveis, name='itens_auditaveis'),
    path('edit_itens_auditaveis/<int:pk>/',edit_itens_auditaveis, name='edit_itens_auditaveis'),
    path('update_itens_auditaveis/<int:pk>/',update_itens_auditaveis, name='update_itens_auditaveiss'),
    path('create_itens_auditaveis/',create_itens_auditaveis, name='create_itens_auditaveis'),
    # Mapeamento
    path('mapeamento/',mapeamento, name='mapeamento'),
    path('cadastrar_mapeamento/',cadastrar_mapeamento, name='cadastrar_mapeamento'),
    path('create_mapeamento/',create_mapeamento, name='create_mapeamento'),    
    path('edit_mapeamento/<int:pk>/',edit_mapeamento, name='edit_mapeamento'),
    path('update_mapeamento/<int:pk>/',update_mapeamento, name='update_mapeamento'),
    path('delete_mapeamento/<int:pk>/',delete_mapeamento, name='delete_mapeamento'),   
    # Adicionar a função de visualizar
]
