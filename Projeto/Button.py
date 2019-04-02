from Drawables import *
class Button(Drawables):
	def __init__(self,color,x,y,width, height, hasborder,active, name,drawable_type):
		super().__init__(color,x,y,width, height, hasborder,active, name,drawable_type)
	def Draw(self):
		pygame.draw.rect(init.getWindowParams,self.__color,[self.__x,self.__y,self.__width,self.__height])
		
		
