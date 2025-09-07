

# trajeto e uma lista de nomes de localidades, representado com uma lista de nomes de localidades
class Trajecto:

    # argumento solucao do tipo Solucao
    def __init__(self,solucao):

        
        self.__percurso = list(solucao.__iter__())
        self.__dimensao = solucao.dimensao
        self.__custo = self.__percurso[-1].custo # custo do ultimo no e o custo total
       
    

    def mostrar(self):

        

        print("Solucao: ", end="")

        for no in self.__percurso:
            print(no.estado.localidade, end=" ")
            
        print("\nDimensao: " + str(self.__dimensao))
        print("Custo: " + str(self.__custo))
