from lib.plan.planeador import Planeador
from lib.pee.melhor_prim.procura_aa import ProcuraAA
from lib.plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from lib.plan.plan_pee.mod_prob.heur_dist import HeurDist
from lib.plan.plan_pee.plano_pee import PlanoPEE

class PlaneadorPEE(Planeador):

    def __init__(self):

        # cria uma instancia de procuraAA
        self.__mec_pee = ProcuraAA()
        self.__heuristica = None
    
    # o argumento modelo_plan e do tipo ModeloPlan, o argumento objetivos e uma lista de Estado
    # retorna o tipo PlanoPEE
    def planear(self, modelo_plan, objetivos):
        
        # o problema vai ser ProblemaPlan e a heuristica HeurDist
        # usar a procura AA primeira

        problema = ProblemaPlan(modelo_plan,objetivos[0])

        # se existir heuristica cria uma solucao
        if self.__heuristica:
            heuristica = self.__heuristica(objetivos[0])
            solucao = self.__mec_pee.procurar(problema,heuristica)

        '''
        heuristica = HeurDist(objetivos[0])

        solucao = self.__mec_pee.procurar(problema,heuristica)'''


        if solucao:
            return PlanoPEE(solucao)
        
    # define a heuristica
    def setHeur(self,heuristica):
        self.__heuristica = heuristica