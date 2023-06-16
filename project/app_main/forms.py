from django.forms import ModelForm
from django import forms
from .models import Sicadfull

class SicadfullForm(forms.ModelForm):
    class Meta:
        model = Sicadfull
        fields = ['servidor','nro_bop','nro_bop_aditado','nro_tombo','tipo_tombo','unidade_origem','unidade_responsavel','dia_semana','fx_4_hor','fx_12_hr','sit_proc','classe_motivo','mes_registro','mes_fato','registros','consolidado','fato_real','especificacao_crime','meio_emp_deac','latitude','longitude','causa_presumivel','especializacao_fato','grupo_ocorrencia','sub_grupo','meio_empregado_sisp','distrito','municipios','regionais','bairros','reg_integracao','risp','aisp','rua_fato','empresa','linha','tipo_transporte','complemento','local_ocorrencia','identificacao_fato','relator','relato','atuacao','vit_nome','vit_alcunha','vit_fx_etaria','vit_nro_doc','vit_tipo_doc','vit_pai','vit_mae','vit_tipo','vit_sexo','vit_cor_pele','vit_grau_inst','vit_profissao','vit_situacao_emprego','vit_estado_civil','aut_nome','aut_fx_etaria','aut_nro_doc','aut_tipo_doc','aut_pai','aut_mae','aut_tipo','aut_sexo','grau_de_relacionamento','aut_cor_pele','aut_grau_inst','aut_profissao','aut_sit_emprego','aut_est_civil','meio_locomocao','cor_veiculo','marca_veic_fuga','modelo_do_veic_fuga']