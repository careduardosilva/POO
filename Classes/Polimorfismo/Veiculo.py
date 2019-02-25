class Veiculo:
	def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo,marchas):
		self._veiculos = list()
		self._grau = 3
		self._placaVeiculo = placaveiculo
		self._fabricanteVeiculo = fabricanteveiculo
		self._numeroRodas = numerorodas
		self._tipoVeiculo = tipoveiculo
		self._marchas = marchas

	def imprime(self):
		print("Placa do veiculo: " + self._placaVeiculo + "\nFabricante do veiculo: " + self._fabricanteVeiculo + "\nNumero de rodas: " + str(self._numeroRodas) + "\nTipo de veiculo " + self._tipoVeiculo)
    
	def getFabricanteVeiculo(self):
		return self._fabricanteVeiculo

	def setFabricanteVeiculo(self, fabricanteveiculo):
		if len(fabricanteveiculo) == 0:
			print ("Fabricante de veiculo vazio")
		else:
			self._fabricanteVeiculo = fabricanteveiculo

	def getPlacaVeiculo(self):
		return self._placaVeiculo

	def setPlacaVeiculo(self, placaveiculo):
		if len(numeroveiculo) == 0:
			print ("Numero de veiculo vazio")
		else:
			self._placaVeiculo = placaveiculo

	def getNumeroRodas(self):
		return self._numeroRodas

	def setNumeroRodas(self, numerorodas):
		if numerorodas <= 0:
			print ("Numero de rodas invalido")
		else:
			self._numeroRodas = numerorodas

	def getTipoVeiculo(self):
		return self._tipoVeiculo

	def setTipoVeiculo(self, tipoveiculo):
		if len(tipoveiculo) == 0:
			print ("Tipo de veiculo vazio")
		else:
			self._tipoVeiculo = tipoveiculo
	def insere(self,objeto):
		self._veiculos.append(objeto)
	def printar(self):
		for i in self._veiculos:
			print(i.imprime())
	def qntdVeiculo(self,tipoVeiculo):
		n = 0
		for i in self._veiculos:
			if(i.getTipoVeiculo() == tipoVeiculo):
				n += 1
		return n
				
	def imprimeFrota(self):
		contador = 0
		for i in self._veiculos:
			if(i.getTipoVeiculo() == "Carro" and self._grau == 3):
				i.imprime()
				contador += 1
				print(contador)
				if(contador == self.qntdVeiculo("Carro")):
					self._grau -= 1
					self.imprimeFrota()			
			if(i.getTipoVeiculo() == "Moto" and self._grau == 2):
				i.imprime()
				contador += 1
				if(contador == self.qntdVeiculo("Moto")):
					self._grau -= 1
					self.imprimeFrota()
			if(i.getTipoVeiculo() == "Bicicleta" and self._grau == 1):
				i.imprime()
				contador += 1
				if(contador == self.qntdVeiculo("Bicicleta")):
					self._grau -= 1
					self.imprimeFrota()	
