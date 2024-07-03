import re

def getCuatroPrimerasCifras(texto):
    retorno = False
    busqueda = re.search(r'\d{4}', texto)
    if busqueda:
        retorno = busqueda.group[0]
    return retorno

