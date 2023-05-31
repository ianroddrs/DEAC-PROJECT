from django.db.models import Q

def adicionar_filtros(request):
    chaves = request.keys()
    valores = request.values()
    dic = {chaves[i]: valores[i] for i in range(len(chaves))}

    DATA_INICIO = request.get('data_inicio')
    DATA_FIM = request.get('data_fim')
    VIT_NOME = request.getlist('vit_nome')

    query = Q()
    
    if VIT_NOME:
        for nome in VIT_NOME:
            query_nome_temp = Q()
            for palavra in nome.split():
                query_nome_temp &= Q(vit_nome__icontains=palavra)
            query |= query_nome_temp

    if DATA_INICIO and DATA_FIM:
        query &= Q(data_fato__range=(DATA_INICIO, DATA_FIM))

    return query

def collumns_list(Sicadfull):
    colunas = [coluna for coluna in vars(Sicadfull) if not any(s in coluna for s in ["_meta", "__module__", "__doc__", "MultipleObjectsReturned", "DoesNotExist", "objects"])]
    colunas.sort()
    return colunas