from lib.mod.problema.problema import Problema
from .estado_localidade import EstadoLocalidade
from .operador_ligacao import OperadorLigacao

class ProblemaPlanTraj(Problema):

    # ligacoes e uma lista de Ligacap, loc_inicial e loc_final sao strings
    def __init__(self,ligacoes,loc_inicial,loc_final):

        # chama o construtor com uma instancia de EstadoLocalidade com a localidade inicial e com uma Instancia de OperadorLigacao com a
        # origem da ligacao, a ligacao de destino e o custo da ligacao
        super().__init__(EstadoLocalidade(loc_inicial),[OperadorLigacao(ligacao.origem, ligacao.destino,ligacao.custo)for ligacao in ligacoes])

        self.__estado_final = EstadoLocalidade(loc_final)

    # a variavel estado e do tipo Estado
    # retorna um booleano
    def objetivo(self,estado):

        # verifica se o estado recebido como argumento e igual ao estado final
        return estado == self.__estado_final