import pygame
class Initialization():
	def __init__(self,width,height):
		self.__width = width
		self.__height = height
		self.__name = "Snake"
		self.__isWorking = True
		self.__window_params = pygame.display.set_mode((self.__largura,self.__altura))
	def Start(self):
		try:
			pygame.init()
		except:
			print("Falha no módulo")
	def Update(self):
		while self.__isWorking:
			pygame.display.update()
	def Options(self):
		pygame.display.set_caption("Snake")
	def Quit(self):
		pygame.quit()
	def getWindowParams(self):
		return self.__window_params
