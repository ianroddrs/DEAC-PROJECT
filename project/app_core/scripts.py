from django.db.models import Q

def listar(input):
    lista = input.split(',')
    return lista

def filtros(request):
    query = Q()

    DATA_INICIO = request.get('data_inicio') 
    DATA_FIM = request.get('data_fim')

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
    }

    for input in request:
        if request.get(input) and not input == 'csrfmiddlewaretoken':
            if input in fields_mapping.keys():
                select = listar(request.get(input))
                query_temp_1 = Q()
                for item in select:
                    query_temp_2 = Q()
                    for palavra in item.split():
                        if input in fields_mapping:
                            field = fields_mapping[input]
                            query_temp_2 &= Q(**{field: palavra.strip()})
                    if len(select) == 1:
                        query &= query_temp_2
                        break
                    query_temp_1 |= query_temp_2
                query &= query_temp_1
            else:
                if DATA_INICIO and DATA_FIM:
                    query &= Q(data_fato__range=(DATA_INICIO, DATA_FIM))
                

                
                # query_temp_1 = Q()
                # for item in select:
                #     query_temp_2 = Q()
                #     for palavra in item.split():
                #         if input in fields_mapping:
                #             field = fields_mapping[input]
                #             query_temp_2 &= Q(**{field: palavra.strip()})
                #     if len(select) == 1:
                #         query &= query_temp_2
                #         break
                #     query_temp_1 |= query_temp_2
                # query &= query_temp_1

    print(query)
    return query





def columns_list(Sicadfull):
    excluded = ["_meta", "__module__", "__doc__", "MultipleObjectsReturned", "DoesNotExist", "objects"]
    columns = [column for column in vars(Sicadfull) if column != "id" and not any(s in column for s in excluded)]
    columns.sort()
    return columns
