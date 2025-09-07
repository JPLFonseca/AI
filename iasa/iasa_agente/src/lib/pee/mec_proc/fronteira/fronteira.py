from abc import ABC, abstractmethod

class Fronteira(ABC):


    def __init__(self):
         
         # inicia a fronteira
         self.iniciar()

    
    def iniciar(self):
        self._nos = []
    
    @abstractmethod
    def inserir(self,no):
        ''''''

    # retorna o tipo No
    def remover(self):
        return self._nos.pop(0)

    # retorna um booleano que indica se ainda existem nos na fronteira ou nao
    @property
    def vazia(self):
        return len(self._nos) == 0
    

    ##### retorna o numero de nos processados #####
    @property
    def memoria(self):
        return len(self._nos)