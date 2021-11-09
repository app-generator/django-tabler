#from django.db import models
from django.db.models import fields
from django.forms import ModelForm,forms
from app.models import Cad_dados_previos, Cad_empresa, Cad_fator_de_risco, Cad_itens_auditaveis,Cad_setores,Cad_fornecedores,Cad_equipes,Cad_dpo,Cad_Mapeamento


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
    class Meta:
        model = Cad_fornecedores
        fields = "__all__"

class Form_cad_equipes(ModelForm):
    class Meta:
        model = Cad_equipes
        fields = "__all__"

class Form_cad_dpo(ModelForm):
    class Meta:
        model = Cad_dpo
        #fields = ['nome','cpf','cargo']
        fields = "__all__"

class Form_dados_previos(ModelForm):
    class Meta:
        model = Cad_dados_previos
        fields = "__all__"

class Form_itens_auditaveis(ModelForm):
    class Meta:
        model = Cad_itens_auditaveis
        fields = "__all__"

class Form_fator_de_risco(ModelForm):
    class Meta:
        model = Cad_fator_de_risco
        fields = "__all__"

class Form_mapeamento(ModelForm):
    class Meta:
        model = Cad_Mapeamento
        fields = "__all__"