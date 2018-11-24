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
    k = 0
    alunos = [Estudante("Ronaldo",313,0),Estudante("Ricardo",932,3),Estudante("Felipe",333,1),Estudante("Raissa",321,1)]
    n = input("Digite o nome de um aluno")
    for i in alunos:
        if(n == i.getNome()):
            i.addCreditos(1)
        else:
            if(k >= len(alunos)-1):
                print("Aluno nao esta cadastrado")  
            k += 1
if __name__ == "__main__":
    main()
