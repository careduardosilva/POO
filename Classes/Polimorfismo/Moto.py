from Veiculo import *
class Moto(Veiculo):
	def __init__(self, placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo,marchas,cilindradas):
		Veiculo.__init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo,marchas)
		self._cilindradas = cilindradas
	def getCilindradas(self):
		return self_cilindradas
	def setCilindradas(self,novo):
		self._cilindradas = novo
	
