from Aquecedor import Aquecedor12

def main():
   object1 = Aquecedor12()
   temperatura = object1.getTemperatura()
   print(temperatura)
   object1.setTemperatura(20)
   temperatura = object1.getTemperatura()
   print(temperatura)
   object1.MaisMorno()
   temperatura = object1.getTemperatura()
   print(temperatura)
   object1.MenosMorno()
   temperatura = object1.getTemperatura()
   print(temperatura)
main()
