from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):

    # problema e do tipo Problema e heuristica e do tipo Heuristica
    # retorna o tipo Solucao
    def procurar(self,problema,heuristica):
        
        self._heuristica = heuristica

        self._avaliador.definir_heuristica(heuristica) # neste metodo, estamos a encaixar uma heuristica
        return super().procurar(problema)