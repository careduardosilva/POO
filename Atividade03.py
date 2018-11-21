class Estudante():
    """attributes:nome,matricula,creditos"""
    def __init__(self,nome,matricula,creditos): #Construtor
        self.__nome = nome
        self.__matricula = matricula
        self.__creditos = creditos
    #Adicionar Creditos
    def addCreditos(self,quantidade):
        self.__creditos += quantidade
    #Métodos acessores
    def setNome(self,novo_nome):
        self.__nome = novo_nome
    def setCreditos(self,novo_credito):
        self.__creditos = novo_credito
    def getNome(self):
        return self.__nome
    def getCreditos(self):
        return self.__creditos
        
def main():
    #Alunos
    alunos = [Estudante("Ronaldo",313,0),Estudante("Ricardo",932,3),Estudante("Felipe",333,1),Estudante("Raissa",321,1)]
    for i in alunos:
        print(i.getNome())
        print(i.getCreditos())
    
    
if __name__ == "__main__":
    main()
