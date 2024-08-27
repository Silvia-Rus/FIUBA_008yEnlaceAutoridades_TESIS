from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from datetime import datetime
from barcodes import lastBarcode
from gettersSetters.getters import getListaDeCamposEnRegistro, getSubfields
from gettersSetters.setters import setField

class F952_maker:
	def __init__(self, record):
	    self.record = record
	    self.F952 = getListaDeCamposEnRegistro(record, '952')

	def setBarcode(self):
		lastBarcode[0] +=1
		return lastBarcode[0]

	def set952pValue(self, field):
		sfP = getSubfields(field, 'p')
		# return False if len(sfP) > 0 else self.setBarcode()
		return False if len(sfP) > 0 else lastBarcode[0]

	def set952(self):
		fieldList = []
		for item in self.F952:
			subfields = item.subfields
			sf952pValue = self.set952pValue(item)
			if sf952pValue:
				subfields.append(Subfield('p', self.set952pValue(item)))
				lastBarcode[0] +=1
			subfields.append(Subfield('r', datetime.now().strftime('%Y-%m-%d')))
			subfields.sort(key=lambda x: x.code)
			fieldList.append(Field('952', [' ', ' '], subfields))
		setField(self.record, '952', fieldList)

	def addF952(self):
	 	self.set952()
