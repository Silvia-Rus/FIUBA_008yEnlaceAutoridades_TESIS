
import os
import sys
from datetime import datetime
from entidades.campo     import Campo
from entidades.subcampo  import Subcampo
from enlazador import Enlazador
from pymarc    import MARCReader
from escribirMarc import EscribirMARC
from informes  import initCSV, writeCSVCounter
from CF008_maker import CF008_maker
from F952_maker import F952_maker


# biblios = 'archivos/mrcFiles/BIB_TODOS.mrc'
# biblios = 'archivos/mrcFiles/BIB_10REG.mrc'
# biblios = 'archivos/mrcFiles/BIB_1REG.mrc'
biblios = 'archivos/mrcFiles/BIB3.mrc'


campo100 = Campo('100', [Subcampo('a', ''), Subcampo('d', '')])
campo110 = Campo('110', [Subcampo('a', ''), Subcampo('b', '')])
campo650 = Campo('650', [Subcampo('a', '')])
campo700 = Campo('700', [Subcampo('a', ''), Subcampo('d', '')])
campo710 = Campo('710', [Subcampo('a', ''), Subcampo('b', '')])
fechaAhora = datetime.now().strftime("%Y%m%d%H%M%S")
nameMrcModified = 'archivos/mrcTransformed/'+fechaAhora+'_BIB_EXPORT.mrc'

listaDeCampos = [campo100, campo110, campo650, campo710, campo700]

e = EscribirMARC(nameMrcModified)
enlazador = Enlazador()

initCSV()
print(sys.version)

if(len(listaDeCampos) > 0):
    if os.path.exists(biblios):
        with open(biblios, 'rb') as fh:
            reader = MARCReader(fh)
            for record in reader:
                enlazador.record = record
                enlazador.link_auth(listaDeCampos)
                CF008_maker(record).addCF008()
                F952_maker(record).addF952()
                # print(record)
                e.escribir(record)
            print(writeCSVCounter(enlazador.recordCounter, enlazador.unlinkedAuth, enlazador.matchingAuth))
            print("Transformacion exitosa:\n"
                  "->Puede ver su archivo mrc modificado en archivos/mrcTransformed.\n"
                  "->Puede ver los informes completos en archivos/reports.")
    else:
           print("No se puede encontrar el archivo .mrc que se quiere modificar. \nRecuerde declararlo correctamente en la variable 'biblios' en el archivo main.py")  
else:
   print("No ha declarado campos para enlazar. \nRecuerde declaralos correctamente en la variable 'listaDeCampos' en el archivo main.py ")
   



   
