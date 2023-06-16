fields_mapping = {
        'vit_nome': 'vit_nome__icontains',
        'vit_alcunha': 'vit_alcunha__icontains',
        'vit_pai': 'vit_pai__icontains',
        'vit_mae': 'vit_mae__icontains',
        'aut_nome': 'aut_nome__icontains',
        'aut_alcunha': 'aut_alcunha__icontains',
        'aut_pai': 'aut_pai__icontains',
        'aut_mae': 'aut_mae__icontains',
        'relator': 'relator__icontains',
        'relato': 'relato__icontains',
        'rua_fato': 'rua_fato__icontains',
        'complemento': 'complemento__icontains',
        'empresa' : 'empresa__icontains',
        'servidor' : 'servidor__icontains',
    }















QUALI_PERMISSIONS = [
    'nro_tombo','tipo_tombo','controle','consolidado','fato_real',
    'especificacao_crime','meio_emp_deac','distrito','municipios',
    'bairros','atuacao','vit_nome','vit_alcunha','vit_dt_nasc','vit_idade',
    'vit_fx_etaria','vit_nro_doc','vit_tipo_doc','vit_pai','vit_mae',
    'vit_tipo','vit_sexo','vit_cor_pele','vit_grau_inst,vit_profissao',
    'vit_situacao_emprego,vit_estado_civil','aut_nome','aut_alcunha',
    'aut_data_nasc','aut_idade','aut_fx_etaria','aut_nro_doc','aut_tipo_doc',
    'aut_pai','aut_mae','aut_tipo','aut_sexo','grau_de_relacionamento',
    'aut_cor_pele','aut_grau_inst','aut_profissao','aut_sit_emprego',
    'aut_est_civil','meio_locomocao','cor_veiculo','marca_veic_fuga',
    'modelo_do_veic_fuga','qtd_autor','relatorio','ident_autoria','exclusao'
]

GROUP_PERMISSIONS = [
    'BOP', 'Autor', 'Vitima', 'Modus'
]





## VITIMA
# vit_nome = models.TextField(blank=True, null=True)
# vit_alcunha = models.CharField(max_length=500, blank=True, null=True)
# vit_dt_nasc = models.DateField(blank=True, null=True)
# vit_idade = models.IntegerField(blank=True, null=True)
# vit_fx_etaria = models.CharField(max_length=500, blank=True, null=True)
# vit_nro_doc = models.CharField(max_length=500, blank=True, null=True)
# vit_tipo_doc = models.CharField(max_length=500, blank=True, null=True)
# vit_pai = models.CharField(max_length=500, blank=True, null=True)
# vit_mae = models.CharField(max_length=500, blank=True, null=True)
# vit_tipo = models.CharField(max_length=500, blank=True, null=True)
# vit_sexo = models.CharField(max_length=100, blank=True, null=True)
# vit_cor_pele = models.CharField(max_length=500, blank=True, null=True)
# vit_grau_inst = models.CharField(max_length=500, blank=True, null=True)
# vit_profissao = models.CharField(max_length=500, blank=True, null=True)
# vit_situacao_emprego = models.CharField(max_length=500, blank=True, null=True)
# vit_estado_civil = models.CharField(max_length=500, blank=True, null=True)
# relator = models.TextField(blank=True, null=True) BLOQUEADO
# atuacao = models.CharField(max_length=500, blank=True, null=True)

## AUTOR
# aut_nome = models.CharField(max_length=500, blank=True, null=True)
# aut_alcunha = models.CharField(max_length=500, blank=True, null=True)
# aut_data_nasc = models.DateField(blank=True, null=True)
# aut_idade = models.IntegerField(blank=True, null=True)
# aut_fx_etaria = models.CharField(max_length=500, blank=True, null=True)
# aut_nro_doc = models.CharField(max_length=500, blank=True, null=True)
# aut_tipo_doc = models.CharField(max_length=500, blank=True, null=True)
# aut_pai = models.CharField(max_length=500, blank=True, null=True)
# aut_mae = models.CharField(max_length=500, blank=True, null=True)
# aut_tipo = models.CharField(max_length=500, blank=True, null=True)
# aut_sexo = models.CharField(max_length=500, blank=True, null=True)
# grau_de_relacionamento = models.CharField(max_length=500, blank=True, null=True)
# aut_cor_pele = models.CharField(max_length=500, blank=True, null=True)
# aut_grau_inst = models.CharField(max_length=500, blank=True, null=True)
# aut_profissao = models.CharField(max_length=500, blank=True, null=True)
# aut_sit_emprego = models.CharField(max_length=500, blank=True, null=True)
# aut_est_civil = models.CharField(max_length=500, blank=True, null=True)
# qtd_autor = models.IntegerField(blank=True, null=True)


## MODUS OPERANDI
# meio_locomocao = models.CharField(max_length=500, blank=True, null=True)
# cor_veiculo = models.CharField(max_length=500, blank=True, null=True)
# marca_veic_fuga = models.CharField(max_length=500, blank=True, null=True)
# modelo_do_veic_fuga = models.CharField(max_length=500, blank=True, null=True)

## BOLETIM
# nro_bop = models.CharField(max_length=500, blank=True, null=True)
# nro_bop_aditado = models.CharField(max_length=500, blank=True, null=True)
# distrito = models.CharField(max_length=500, blank=True, null=True)
# municipios = models.CharField(max_length=500, blank=True, null=True)
# identificacao_fato = models.TextField(blank=True, null=True)
# bairros = models.CharField(max_length=500, blank=True, null=True)
# nro_tombo = models.CharField(max_length=500, blank=True, null=True)
# tipo_tombo = models.CharField(max_length=500, blank=True, null=True)
# controle = models.CharField(max_length=500, blank=True, null=True)
# consolidado = models.CharField(max_length=500, blank=True, null=True)
# fato_real = models.CharField(max_length=500, blank=True, null=True)
# especificacao_crime = models.CharField(max_length=500, blank=True, null=True)
# relatorio = models.CharField(max_length=500, blank=True, null=True)
# ident_autoria = models.CharField(max_length=500, blank=True, null=True)
# exclusao = models.BooleanField()
# meio_emp_deac = models.CharField(max_length=500, blank=True, null=True)