from abc import ABC, abstractmethod

class Operador(ABC):

    
    @abstractmethod
    # a variavel estado e do tipo Estado e este metodo retorna o tipo Estado
    def aplicar(self, estado):
        ''''''

        # e uma interface
    
    @abstractmethod
    # as duas variaveis recebidas sao do tipo estado e este metodo retorna o tipo float
    def custo(self, estado, estado_suc):
        ''''''