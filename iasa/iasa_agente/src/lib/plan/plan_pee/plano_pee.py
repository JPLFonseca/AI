from lib.plan.plano import Plano

class PlanoPEE(Plano):

    def __init__(self,solucao):
        self.__solucao = solucao 

    # o argumento estado e do tipo Estado
    # retorna o tipo Operador
    def obter_accao(self,estado):
        
        if self.__solucao.dimensao > 1:

            if estado == self.__solucao[0].estado:

                operador = self.__solucao[1].operador
                self.__solucao.remover()
                return operador
    
    # vista e do tipo VistaAmb
    # nao tem return
    def mostrar(self, vista):
        vista.mostrar_solucao(self.__solucao)