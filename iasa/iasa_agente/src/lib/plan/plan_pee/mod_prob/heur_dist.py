from lib.pee.melhor_prim.aval.heuristica import Heuristica
import math

class HeurDist(Heuristica):

    # estado_final e do tipo Estado
    def __init__(self,estado_final):
        self.__estado_final = estado_final

    # estado e do tipo Estado
    # retorna um float
    def h(self,estado):

        # distancia entre o estado recebido e o estado_final
        # distancia em linha reta, sem nada no meio

        return math.dist(estado.posicao,self.__estado_final.posicao)
    
class HeurManhattan(Heuristica):
    
    def __init__(self,estado_final):
        self.__estado_final = estado_final

    # aplica a formula da heuristica de Manhattan
    def h(self,estado):
        return (abs(estado.posicao[0]-self.__estado_final.posicao[0])+abs(estado.posicao[1]-self.__estado_final.posicao[1]))