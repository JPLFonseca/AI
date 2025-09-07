from lib.pee.mec_proc.fronteira.avaliador import Avaliador

class AvaliadorCustoUnif(Avaliador):

    # retorna o tipo float
    def prioridade(self,no):
        return no.custo