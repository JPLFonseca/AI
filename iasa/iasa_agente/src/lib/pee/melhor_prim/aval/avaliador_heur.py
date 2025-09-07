from pee.mec_proc.fronteira.avaliador import Avaliador

class AvaliadorHeur(Avaliador):

    # heurisitca e do tipo Heuristica
    def definir_heuristica(self,heuristia):
        self._heuristica = heuristia # guarda apenas o atributo heuristica