# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from django.contrib import admin
#from app.models import Cad_Mapeamento, Cad_empresa, Cad_equipes,Cad_setores,Cad_fornecedores,Cad_dpo,Cad_dados_previos,Cad_itens_auditaveis,Cad_fator_de_risco
from app.models import *


admin.site.register(Cad_empresa)
admin.site.register(Cad_setores)
admin.site.register(Cad_equipes)
admin.site.register(Cad_dpo)
admin.site.register(Cad_fornecedores)
admin.site.register(Cad_dados_previos)
admin.site.register(Cad_itens_auditaveis)
#admin.site.register(Cad_fator_de_risco)
admin.site.register(Cad_Mapeamento)


