from .comport_comp import ComportComp

class Hierarquia(ComportComp):

    # retorna do tipo Accao
    def selecionar_accao(self,accoes):

        # as accoes recebidas ja estao por ordem de prioridade, basta apenas retornar a primeira accao que e a mais prioritaria
        if(accoes is not None):
            return accoes[0]
        