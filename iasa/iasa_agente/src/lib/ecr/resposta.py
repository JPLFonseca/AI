class Resposta:

    #construtor da classe
    # accao e do tipo Accao
    def __init__(self,accao):
        self._accao = accao
    
    # este metodo vai definir uma resposta a estimulos, uma accao, e a sua prioridade
    # percepcao e do tipo Percepcao e intensidade e do tipo float
    def activar(self,percepcao,intensidade=0):
        # o argumento percepcao nao e usado nesta parte da implementacao, mas esta aqui por questao de compatibilidade

        

        self._accao.prioridade = intensidade # iniciar a accao com a intensidade *o parametro vai ficar a 0 para ser feito teste*
        return self._accao # retornar a accao
