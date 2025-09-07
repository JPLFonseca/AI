from lib.mod.estado import Estado

class EstadoAgente(Estado):

    # posicao e do tipo Posicao
    def __init__(self,posicao):
        self.__posicao = posicao
        self.__id_valor = hash(posicao)

    # retorna um int
    def id_valor(self): 
        return self.__id_valor
    
    @property
    def posicao(self):
        return self.__posicao