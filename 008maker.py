
from gettersSetters.getters   import getAnio26X
from gettersSetters.getters   import getCF008
from regex import getCuatroPrimerasCifras
from datetime import datetime

class ControlField008:
    def __init__(self, record):
        self.record = record
        self.CF008 = getCF008(record)
        self.il = ['lámina', 'láminas', 'láms', 'dibujos', 'lám', 'il', 'figs.', 'diagrama']
        self.graf = ['gráfs']
        self.foto = ['fotografia', 'fotos']
    
    def __str__(self):
        return self.CF008

    def setPosiciones008(self, valores: str, posicionDesde: int, posicionHasta = None):
      retorno = False
      if posicionHasta > 39:
        if posicionHasta == None and len(valores) == 1:
            self.CF008[posicionDesde] = valores
            retorno = True
        elif posicionDesde > -1 and posicionHasta > -1 and posicionDesde < posicionHasta and (posicionDesde-posicionHasta+1) == len(valores):
            i = posicionDesde
            for valor in valores:
                self.CF008[i] = valor
                i+=1
            retorno = True
      return retorno
        
    def setControlField008_06_10(self):
      anioCifras = self.getAnio26XCifras()
      str06_10 = 's'+anioCifras if anioCifras else 'uuuuu'
      return self.setPosiciones008(self, str06_10, 6, 10)
    
    def setControlField008_00_05(self):
       fechaAhora = datetime.now().strftime('%y%m%d')
       return self.setPosiciones008(self, fechaAhora, 0, 5)

    def getAnio26XCifras(self):
      anio26X = getAnio26X(self.record)[0]
      return getCuatroPrimerasCifras(anio26X)
    
    
              
                  
        



        



    



