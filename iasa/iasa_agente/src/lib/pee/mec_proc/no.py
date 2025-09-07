

class No():

    # estado e do tipo Estao, operador e do tipo Operador e antecessor e do tipo No
    def __init__(self,estado,operador=None,antecessor=None):
        self.estado = estado
        self.operador = operador
        self.__antecessor = antecessor

        # se o no atual tiver um no antecessor, a sua profundidade atual vai ser a profundidade do no antecesor mais um e o custo vai ver
        # o custo do no antecessor mais o custo do no atual, que e obtido dando ao operador o estado do no antecessora e o estado do no atual

        # caso contrario inicializa tanto a profundidade como o custo a 0
        if(antecessor):
            self.__profundidade = antecessor.profundidade + 1
            self.__custo = antecessor.custo + operador.custo(antecessor.estado,estado)
        else:
            self.__profundidade = 0
            self.__custo = 0
    
    # no e do tipo No e retorna o tipo boolean
    def __lt__(self,no):###
        return self.custo < self.antecessor.custo

    # retorna o no antecessor
    @property
    def antecessor(self):
        return self.__antecessor

    # retorna a profundidade
    @property
    def profundidade(self):
        return self.__profundidade
    
    # retorna o custo
    @property
    def custo(self):
         return self.__custo