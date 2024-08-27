
# -*- coding: utf-8 -*-
from gettersSetters.getters   import getAnio26X, getIl300
from gettersSetters.getters   import getCF008
from gettersSetters.setters   import setCF008
from regex import getCuatroPrimerasCifras, tieneFotos, tieneGraficas, tieneIlustraciones
from datetime import datetime
from pymarc import Field

class CF008_maker:
    def __init__(self, record):
        self.record = record
        self.CF008 = str(getCF008(record).data)
    
    def __str__(self):
        return self.CF008

    def setPosiciones008(self, valores, posicionDesde, posicionHasta = None):
      retorno = False
      if posicionHasta < 40:
        # print("entra a posicion hasta mayor a 39")
        # print(posicionDesde > -1)
        # print(posicionHasta > -1)
        # print(posicionDesde < posicionHasta)
        # print((posicionHasta-posicionDesde+1) == len(valores))
        lista008 = list(self.CF008)
        if posicionHasta == None and len(valores) == 1:
            self.CF008[posicionDesde] = valores
            retorno = True
        elif posicionDesde > -1 and posicionHasta > -1 and posicionDesde < posicionHasta and (posicionHasta-posicionDesde+1) == len(valores):
            i = posicionDesde
            for valor in valores:
                lista008[i] = valor
                i+=1
            retorno = True
        self.CF008 = ''.join(lista008)
      return retorno
        
    def setControlField008_00_05(self): # fecha de catalogación
       fechaAhora = datetime.now().strftime('%y%m%d')
       return self.setPosiciones008(fechaAhora, 0, 5)
    
    def setControlField008_06_10(self): # fecha de publicacion
      anioCifras = self.getAnio26XCifras()
      str06_10 = 's'+anioCifras if anioCifras else 'uuuuu'
      return self.setPosiciones008(str06_10, 6, 10)
    
    def setControlField008_18_21(self): #ilustraciones
       listaDe300a300b = getIl300(self.record)
       str18_21 =  'a' if tieneIlustraciones(listaDe300a300b) else ''
       str18_21 += 'd' if tieneGraficas(listaDe300a300b) else ''
       str18_21 += 'o' if tieneFotos(listaDe300a300b) else ''
       while len(str18_21) < 4:
        str18_21 += '|'
       return self.setPosiciones008(str18_21, 18, 21)

    def getAnio26XCifras(self):
      anio26X = getAnio26X(self.record)[0]
      return getCuatroPrimerasCifras(anio26X)
    
    def addCF008(self):
       self.setControlField008_00_05()
       self.setControlField008_06_10()
       self.setControlField008_18_21()
       fechaActual = datetime.now()
       fechaActualConFormato = fechaActual.strftime('%Y%m%d%H%M%S.%f')[:-5]
       self.record.add_field(Field(tag='005', data=fechaActualConFormato))
       setCF008(self.record, self.CF008)


              
              
                  
        



        



    



