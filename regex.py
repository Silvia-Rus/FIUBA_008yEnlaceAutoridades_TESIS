# -*- coding: utf-8 -*-
import unicodedata
import sys
import re
from Casos.casos008 import a, d, o

def quitarTilde(string):
        return ''.join((c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn'))


def getCuatroPrimerasCifras(texto):
    retorno = False
    busqueda = re.search(r'\d{4}', str(texto))
    if busqueda:
        retorno = busqueda.group()
    return retorno

def apareceElStringEnLaLista(listaDeCasos, listaDeSubcampos):
    for caso in listaDeCasos:
        for sc in listaDeSubcampos:
            if caso in str(sc):
                return  True        
    return False

def tieneIlustraciones(listaDeStrings):
    return apareceElStringEnLaLista(a, listaDeStrings)

def tieneGraficas(listaDeStrings):
    return apareceElStringEnLaLista(d, listaDeStrings)

def tieneFotos(listaDeStrings):
    return apareceElStringEnLaLista(o, listaDeStrings)


    

    

