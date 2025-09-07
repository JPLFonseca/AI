from lib.mod.problema.problema import Problema

class ProblemaPlan(Problema):

    # modelo_plan e do tipo ModeloPlan e estado_final e do tipo Estado
    def __init__(self,modelo_plan,estado_final):
        estado = modelo_plan.obter_estado()
        operadores = modelo_plan.obter_operadores()

        super().__init__(estado, operadores)
        self.__estado_final = estado_final
    
    # estado e do tipo Estado
    # retorna um boolean
    def objetivo(self, estado):

        # verifica se o estado e um objetivo
        return estado == self.__estado_final