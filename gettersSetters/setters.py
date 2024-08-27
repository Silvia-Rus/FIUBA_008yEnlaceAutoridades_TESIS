# -*- coding: utf-8 -*-
from pymarc import MARCReader, Field

def setCampoSubcampoValor(campo, subcampo, valor):
    """
        Se aniade un subcampo a un campo y se le asigna un valor.

        Args:
            campo (Field): campo al cual se le quiere aniadir el subcampo y el valor.
            subcampo (str): subcampo que se quiere aniadir al campo.
            valor (str): valor que se le quiere asignar al subcampo
    """
    campo.add_subfield(subcampo, valor)

def setField(record, tag, fieldList):
    listToRemove = record.get_fields(tag);
    for item in listToRemove:   
        record.remove_field(item)
    for field in fieldList:
        record.add_field(field)

def setCF(record, CF, valores):
    record.remove_field(record.get_fields(CF)[0])
    record.add_field(Field(tag=CF, data=valores))

def setCF008(record, valores):
    setCF(record, '008', valores)

def setCF(record, CF, valores):
    record.remove_field(record.get_fields(CF)[0])
    record.add_field(Field(tag=CF, data=valores))



