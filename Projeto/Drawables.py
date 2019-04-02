import pygame
import Initialization as init
class Drawables():
	def __init__(self,color,x,y,width, height, hasborder,active, name,drawable_type):
		self.__color = color
		self.__position = list(x,y)
		self.__hasborder = hasborder
		self.__active = active
		self.__name = name
		self.__type = drawable_type
		self.__width = witdh
		self.__height = height
	def Draw(self):
		window = init.getWindowParams
							
	def isOver(self,pos):
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		return False
