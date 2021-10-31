# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Cad_empresa, Cad_equipes,Cad_setores,Cad_fornecedores,Cad_dpo

admin.site.register(Cad_empresa)
admin.site.register(Cad_setores)
admin.site.register(Cad_equipes)
admin.site.register(Cad_dpo)
admin.site.register(Cad_fornecedores)
