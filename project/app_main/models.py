from django.db import models

class Sicadfull(models.Model):
    servidor = models.CharField(max_length=50, blank=True, null=True)
    nro_bop = models.CharField(max_length=500, blank=True, null=True)
    nro_bop_aditado = models.CharField(max_length=500, blank=True, null=True)
    nro_tombo = models.CharField(max_length=500, blank=True, null=True)
    tipo_tombo = models.CharField(max_length=500, blank=True, null=True)
    unidade_origem = models.CharField(max_length=500, blank=True, null=True)
    unidade_responsavel = models.CharField(max_length=500, blank=True, null=True)
    data_registro = models.DateField(blank=True, null=True)
    hora_registro = models.TimeField(blank=True, null=True)
    data_fato = models.DateField(blank=True, null=True)
    dia_semana = models.CharField(max_length=500, blank=True, null=True)
    hora_fato = models.TimeField(blank=True, null=True)
    fx_4_hor = models.CharField(max_length=500, blank=True, null=True)
    fx_12_hr = models.CharField(max_length=500, blank=True, null=True)
    data_inst_proc = models.DateField(blank=True, null=True)
    data_concl_proc = models.DateField(blank=True, null=True)
    sit_proc = models.CharField(max_length=500, blank=True, null=True)
    classe_motivo = models.CharField(max_length=500, blank=True, null=True)
    mes_registro = models.CharField(max_length=500, blank=True, null=True)
    mes_fato = models.CharField(max_length=500, blank=True, null=True)
    ano_registro = models.IntegerField(blank=True, null=True)
    ano_fato = models.IntegerField(blank=True, null=True)
    registros = models.CharField(max_length=500, blank=True, null=True)
    consolidado = models.CharField(max_length=500, blank=True, null=True)
    fato_real = models.CharField(max_length=500, blank=True, null=True)
    especificacao_crime = models.CharField(max_length=500, blank=True, null=True)
    meio_emp_deac = models.CharField(max_length=500, blank=True, null=True)
    latitude = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.CharField(max_length=500, blank=True, null=True)
    causa_presumivel = models.CharField(max_length=500, blank=True, null=True)
    especializacao_fato = models.CharField(max_length=500, blank=True, null=True)
    grupo_ocorrencia = models.CharField(max_length=500, blank=True, null=True)
    sub_grupo = models.CharField(max_length=500, blank=True, null=True)
    meio_empregado_sisp = models.CharField(max_length=500, blank=True, null=True)
    distrito = models.CharField(max_length=500, blank=True, null=True)
    municipios = models.CharField(max_length=500, blank=True, null=True)
    regionais = models.CharField(max_length=500, blank=True, null=True)
    bairros = models.CharField(max_length=500, blank=True, null=True)
    reg_integracao = models.CharField(max_length=500, blank=True, null=True)
    risp = models.CharField(max_length=500, blank=True, null=True)
    aisp = models.CharField(max_length=500, blank=True, null=True)
    rua_fato = models.CharField(max_length=500, blank=True, null=True)
    empresa = models.CharField(max_length=500, blank=True, null=True)
    linha = models.CharField(max_length=500, blank=True, null=True)
    tipo_transporte = models.CharField(max_length=500, blank=True, null=True)
    complemento = models.TextField(blank=True, null=True)
    local_ocorrencia = models.TextField(blank=True, null=True)
    identificacao_fato = models.TextField(blank=True, null=True)
    relator = models.TextField(blank=True, null=True)
    relato = models.TextField(blank=True, null=True)
    atuacao = models.CharField(max_length=500, blank=True, null=True)
    vit_nome = models.TextField(blank=True, null=True)
    vit_alcunha = models.CharField(max_length=500, blank=True, null=True)
    vit_dt_nasc = models.DateField(blank=True, null=True)
    vit_idade = models.IntegerField(blank=True, null=True)
    vit_fx_etaria = models.CharField(max_length=500, blank=True, null=True)
    vit_nro_doc = models.CharField(max_length=500, blank=True, null=True)
    vit_tipo_doc = models.CharField(max_length=500, blank=True, null=True)
    vit_pai = models.CharField(max_length=500, blank=True, null=True)
    vit_mae = models.CharField(max_length=500, blank=True, null=True)
    vit_tipo = models.CharField(max_length=500, blank=True, null=True)
    vit_sexo = models.CharField(max_length=100, blank=True, null=True)
    vit_cor_pele = models.CharField(max_length=500, blank=True, null=True)
    vit_grau_inst = models.CharField(max_length=500, blank=True, null=True)
    vit_profissao = models.CharField(max_length=500, blank=True, null=True)
    vit_situacao_emprego = models.CharField(max_length=500, blank=True, null=True)
    vit_estado_civil = models.CharField(max_length=500, blank=True, null=True)
    aut_nome = models.CharField(max_length=500, blank=True, null=True)
    aut_alcunha = models.CharField(max_length=500, blank=True, null=True)
    aut_data_nasc = models.DateField(blank=True, null=True)
    aut_idade = models.IntegerField(blank=True, null=True)
    aut_fx_etaria = models.CharField(max_length=500, blank=True, null=True)
    aut_nro_doc = models.CharField(max_length=500, blank=True, null=True)
    aut_tipo_doc = models.CharField(max_length=500, blank=True, null=True)
    aut_pai = models.CharField(max_length=500, blank=True, null=True)
    aut_mae = models.CharField(max_length=500, blank=True, null=True)
    aut_tipo = models.CharField(max_length=500, blank=True, null=True)
    aut_sexo = models.CharField(max_length=500, blank=True, null=True)
    grau_de_relacionamento = models.CharField(max_length=500, blank=True, null=True)
    aut_cor_pele = models.CharField(max_length=500, blank=True, null=True)
    aut_grau_inst = models.CharField(max_length=500, blank=True, null=True)
    aut_profissao = models.CharField(max_length=500, blank=True, null=True)
    aut_sit_emprego = models.CharField(max_length=500, blank=True, null=True)
    aut_est_civil = models.CharField(max_length=500, blank=True, null=True)
    meio_locomocao = models.CharField(max_length=500, blank=True, null=True)
    cor_veiculo = models.CharField(max_length=500, blank=True, null=True)
    marca_veic_fuga = models.CharField(max_length=500, blank=True, null=True)
    modelo_do_veic_fuga = models.CharField(max_length=500, blank=True, null=True)
    qtd_autor = models.IntegerField(blank=True, null=True)
    relatorio = models.CharField(max_length=500, blank=True, null=True)
    ident_autoria = models.CharField(max_length=500, blank=True, null=True)
    controle = models.CharField(max_length=500, blank=True, null=True)
    controle_ctcd = models.CharField(max_length=500, blank=True, null=True)
    flags = models.CharField(max_length=500, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    data_upload = models.DateTimeField(blank=True, null=True)
    data_modificacao = models.DateTimeField(blank=True, null=True)
    id_servidor_sicad = models.IntegerField(blank=True, null=True)
    qtd = models.IntegerField(blank=True, null=True)
    data_leitura = models.DateField(blank=True, null=True)
    usuario_modificacao = models.CharField(max_length=200, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    exclusao = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'sicadfull'
        permissions = [
            ("BOP", "Modificar dados relacionados ao BOP"),
            ("Autor", "Modificar dados relacionados ao autor"),
            ("Vitima", "Modificar dados relacionados à vitima"),
            ("Modus", "Modificar dados relacionados ao Modus operandi"),
        ]