from django.db.models import fields
from django.forms import ModelForm,forms
from django.db import models
from app.models import Cad_empresa,Cad_setores,Cad_fornecedores,Cad_equipes,Cad_dpo


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

class Form_cad_fornecedores(ModelForm):
    class meta:
        model = Cad_fornecedores
        fields = "__all__"

class Form_cad_equipes(ModelForm):
    class Meta:
        model = Cad_equipes
        fields = "__all__"

class Form_cad_dpo(ModelForm):
    class Meta:
        models = Cad_dpo
        fields = "__all__"
