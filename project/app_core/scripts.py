from django.db.models import Q

def adicionar_filtros(request):    
    DATA_INICIO = request.POST.get('data_inicio')
    DATA_FIM = request.POST.get('data_fim')
    VIT_NOME = request.POST.getlist('vit_nome')

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
    exclude_strings = ["_meta", "__module__", "__doc__", "MultipleObjectsReturned", "DoesNotExist"]
    colunas = [coluna for coluna in vars(Sicadfull) if not any(s in coluna for s in exclude_strings)]
    colunas.sort()
    return colunas