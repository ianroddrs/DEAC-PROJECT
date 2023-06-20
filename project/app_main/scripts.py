from django.db.models import Q
from .lists import fields_mapping

def columns_list(Sicadfull):
    excluded = ["_meta", "__module__", "__doc__", "MultipleObjectsReturned", "DoesNotExist", "objects", "qtd"]
    columns = [column for column in vars(Sicadfull) if column != "id" and not any(s in column for s in excluded)]
    return columns

def listar(input):
    lista = input.split(',')
    return lista

def filtros(request):
    query = Q()

    DATA_INICIO = request.get('data_inicio') 
    DATA_FIM = request.get('data_fim')
    if DATA_INICIO and DATA_FIM:
        query &= Q(data_registro__range=(DATA_INICIO, DATA_FIM))

    excl = ['csrfmiddlewaretoken', 'data_inicio', 'data_fim']

    for input in request:
        if input in excl:
            continue
        if request.get(input):
            select = listar(request.get(input))
            query_temp_1 = Q()
            for item in select:
                query_temp_2 = Q()
                for palavra in item.split():
                    if input in fields_mapping.keys():
                        field = fields_mapping[input]
                        query_temp_2 &= Q(**{field: palavra.strip()})
                    else:
                        query_temp_2 &= Q(**{input: palavra.strip()})
                if len(select) == 1:
                    query &= query_temp_2
                    break
                query_temp_1 |= query_temp_2
            query &= query_temp_1
    print(query)
    return query
