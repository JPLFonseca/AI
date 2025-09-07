from lib.mod.operador import Operador
from .estado_localidade import EstadoLocalidade

class OperadorLigacao(Operador):

    # origem e destino sao strings e custo e int
    def __init__(self,origem,destino,custo):

        self.__custo = custo

        self.__estado_origem = EstadoLocalidade(origem)
        self.__estado_destino = EstadoLocalidade(destino)

    # o argumento estado e do tipo Estado
    # retorna o tipo Estado
    def aplicar(self,estado):

        # verifica se o estado recebido e igual ao estado de origem
        if(estado == self.__estado_origem):

            # se a condicao se verificar retorna o estado de destino
            return self.__estado_destino
        else:

            # se nao se verificar a condicao, retorna None
            return None
    
    # retorna um float
    def custo(self,estado,estado_suc):
        return self.__custo
    
    