from pymarc    import MARCReader
from gettersSetters.getters   import getHasUnlinkedAuth, getListaDeCamposEnRegistro, getCF001
from gettersSetters.setters   import setCampoSubcampoValor
from DAO.autoridadesDAO import findMatchingAuth
from informes  import writeCSVUnmatched, writeCSVMatched
from entidades.campo     import Campo
from entidades.subcampo  import Subcampo

class Enlazador:
  """
    Clase que sirve para enlazar autoridades a un archivo mrc. 
  """

  def __init__(self):
    """
      Se inician los valores de los contadores para la estadistica final.
    """
    self.record = ''
    self.unlinkedAuth  = 0 
    self.matchingAuth  = 0
    self.recordCounter = 0

  def link_auth(self, listaDeCampos): 
    """
      Se generan los enlaces a las autoridades (en el caso de que no lo tenga y de que exista en la base de autoridades) 
      en un registro bibliografico concreto.

      Se asume que el registro sera incorporado a un catalogo Koha, es decir, 
      se aniadira un $9 con el auth_id de la base de datos de autoridades.

      Args:
        listaDeCampos (list de Campo): la lista de campos que se quieren enlazar del registro bibliografico.
          estos campos deberan contener el listado de subcampos que se deben chequear para establecer la igualdad.

      Return:
        Record: devuelve el registro con los encabezamientos enlazados. 
    """
    self.recordCounter += 1
    for campo in listaDeCampos: 
      ocurrenciasDelCampo = getListaDeCamposEnRegistro(self.record, campo.campo)
      if(len(ocurrenciasDelCampo) > 0):
        i = 0
        for ocurrencia in ocurrenciasDelCampo:
          campoSin9 = Enlazador.detectarCampoSinEnlazar(ocurrencia, campo)
          if(campoSin9 != False):
            biblionumber = getCF001(self.record)
            authEnBd = Enlazador.detectarAuthEnBD(campoSin9)
            authId = authEnBd[0] if authEnBd else ''
            tesauro = authEnBd[1] if authEnBd else ''
            if(authEnBd != False):
              setCampoSubcampoValor(ocurrenciasDelCampo[i], '9', authId)
              setCampoSubcampoValor(ocurrenciasDelCampo[i], '2', tesauro)
              print(writeCSVMatched(str(biblionumber), authId, campoSin9))
              self.matchingAuth+=1
            else:
              print(writeCSVUnmatched(str(biblionumber), campoSin9))
              self.unlinkedAuth+=1
          i+=1
   
  
  @staticmethod
  def detectarCampoSinEnlazar(field, campo): 
    """
      Se detecta si un encabezamiento no tiene enlace a autoridades.

      Args:
        field (Field): encabezamiento del cual se quiere chequear si esta enlazado a la autoridad.
        campo (str): campo a chequear.
      
      Return:
        Bool: devuelve False si el campo ya tiene enlace a la autoridad.
        Campo: devuelve el campo formado para poder ser buscado en la Base de datos.
    """
    retorno = False  
    if getHasUnlinkedAuth(field):
      retorno = Campo.fieldToCampo(field, campo)
    return retorno
  
  @staticmethod
  def detectarAuthEnBD(campo):
    """
      Busca en la BD el AuthId que eventualmente debe ser el valor a asignar en el $9 del campo del registro.

      Args:
        campo (Campo): campo formado para ser buscado en la BD.
    """
    retorno = False
    ocurrenciasEnBD = findMatchingAuth(campo)
    if(len(ocurrenciasEnBD) > 0):
      return ocurrenciasEnBD[0]
    return retorno




  
    
  
     








             
      

            
         

  

  




