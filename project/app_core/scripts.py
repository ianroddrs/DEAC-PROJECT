def adicionar_argumentos(DI, DF):
    kwargs = {}
    if  DI != "" and DF != "" :
        kwargs["data_fato__range"] = (DI, DF)
    return kwargs