from django.db.models import Q

def adicionar_filtros(request):

    

    DATA_INICIO = request.get('data_inicio')
    DATA_FIM = request.get('data_fim')
    VIT_NOME = request.getlist('vit_nome')
    VIT_ALCUNHA = request.getlist('vit_alcunha')
    VIT_PAI = request.getlist('vit_pai')
    VIT_MAE = request.getlist('vit_mae')
    AUT_NOME = request.getlist('aut_nome')
    AUT_ALCUNHA = request.getlist('aut_alcunha')
    AUT_PAI = request.getlist('aut_pai')
    AUT_MAE = request.getlist('aut_mae')
    RELATOR = request.getlist('relator')
    RELATO = request.getlist('relato')
    RUA_FATO = request.getlist('rua_fato')
    COMPLEMENTO = request.getlist('complemento')
    EMPRESA = request.getlist('empresa')

    query = Q()

    if VIT_NOME:
        for vnome in VIT_NOME:
            query_temp = Q()
            for palavra in vnome.split():
                query_temp &= Q(vit_nome__icontains=palavra)
            if(len(VIT_NOME)==1):
                query &= query_temp
                break
            query |= query_temp

    if VIT_ALCUNHA:
        for valcunha in VIT_ALCUNHA:
            query_temp = Q()
            for palavra in valcunha.split():
                query_temp &= Q(vit_alcunha__icontains=palavra)
            if(len(VIT_ALCUNHA)==1):
                query &= query_temp
                break
            query |= query_temp

    if VIT_PAI:
        for vpai in VIT_PAI:
            query_temp = Q()
            for palavra in vpai.split():
                query_temp &= Q(vit_pai__icontains=palavra)
            if(len(VIT_PAI)==1):
                query &= query_temp
                break
            query |= query_temp

    if VIT_MAE:
        for vmae in VIT_MAE:
            query_temp = Q()
            for palavra in vmae.split():
                query_temp &= Q(vit_mae__icontains=palavra)
            if(len(VIT_MAE)==1):
                query &= query_temp
                break
            query |= query_temp

    if AUT_NOME:
        for anome in AUT_NOME:
            query_temp = Q()
            for palavra in anome.split():
                query_temp &= Q(aut_nome__icontains=palavra)
            if(len(AUT_NOME)==1):
                query &= query_temp
                break
            query |= query_temp

    if AUT_ALCUNHA:
        for aalcunha in AUT_ALCUNHA:
            query_temp = Q()
            for palavra in aalcunha.split():
                query_temp &= Q(aut_alcunha__icontains=palavra)
            if(len(AUT_ALCUNHA)==1):
                query &= query_temp
                break
            query |= query_temp

    if AUT_PAI:
        for apai in AUT_PAI:
            query_temp = Q()
            for palavra in apai.split():
                query_temp &= Q(aut_pai__icontains=palavra)
            if(len(AUT_PAI)==1):
                query &= query_temp
                break
            query |= query_temp

    if AUT_MAE:
        for amae in AUT_MAE:
            query_temp = Q()
            for palavra in amae.split():
                query_temp &= Q(aut_mae__icontains=palavra)
            if(len(AUT_MAE)==1):
                query &= query_temp
                break
            query |= query_temp

    if RELATOR:
        for relator in RELATOR:
            query_temp = Q()
            for palavra in relator.split():
                query_temp &= Q(relator__icontains=palavra)
            if(len(RELATOR)==1):
                query &= query_temp
                break
            query |= query_temp

    if RELATO:
        for relato in RELATO:
            query_temp = Q()
            for palavra in relato.split():
                query_temp &= Q(relato__icontains=palavra)
            if(len(RELATO)==1):
                query &= query_temp
                break
            query |= query_temp

    if RUA_FATO:
        for rua in RUA_FATO:
            query_temp = Q()
            for palavra in rua.split():
                query_temp &= Q(rua_fato__icontains=palavra)
            if(len(RUA_FATO)==1):
                query &= query_temp
                break
            query |= query_temp

    if COMPLEMENTO:
        for complemento in COMPLEMENTO:
            query_temp = Q()
            for palavra in complemento.split():
                query_temp &= Q(complemento__icontains=palavra)
            if(len(COMPLEMENTO)==1):
                query &= query_temp
                break
            query |= query_temp

    if EMPRESA:
        for empresa in EMPRESA:
            query_temp = Q()
            for palavra in empresa.split():
                query_temp &= Q(empresa__icontains=palavra)
            if(len(EMPRESA)==1):
                query &= query_temp
                break
            query |= query_temp

    if DATA_INICIO and DATA_FIM:
        query &= Q(data_fato__range=(DATA_INICIO, DATA_FIM))

    return query


def collumns_list(Sicadfull):
    colunas = [coluna for coluna in vars(Sicadfull) if not any(s in coluna for s in ["_meta", "__module__", "__doc__", "MultipleObjectsReturned", "DoesNotExist", "objects"])]
    colunas.sort()
    return colunas
