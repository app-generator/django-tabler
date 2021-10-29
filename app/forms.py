from django.forms import ModelForm,forms
from django.db import models
from app.models import Cad_empresa,Cad_setores

class Form_cad_empresa(ModelForm):
    class Meta:
        model = Cad_empresa
        #fields = ['nome_fantasia_empresa','cnpj_empresa','endereco_empresa','cidade_empresa','cep_empresa','estado_empresa','telefone_empresa']
        fields = "__all__"
class Form_cad_setores(ModelForm):
    class Meta:
        model = Cad_setores
        #fields = ['setor_nome','responsavel_setor','cargo_setor','contato_setor']
        fields = "__all__"
