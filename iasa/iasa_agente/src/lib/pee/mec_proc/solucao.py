

class Solucao():

    def __init__(self,no_final):
        # inicia o percurso
        self.__percurso = []
        no = no_final


        while no:
            self.__percurso.insert(0,no)
            no = no.antecessor

    # retorna o tipo No
    def remover(self):

        # se existir percurso 
        if(self.__percurso):
            return self.__percurso.pop(0)
    
    # retorna o tipo Iterator<No>
    def __iter__(self):
        return iter(self.__percurso)
    
    # index e do tipo int e este metodo retorna o tipo No
    def __getitem__(self,index):
        return self.__percurso[index]
    
    # retorna a dimensao do percurso
    @property
    def dimensao(self):
        return len(self.__percurso)