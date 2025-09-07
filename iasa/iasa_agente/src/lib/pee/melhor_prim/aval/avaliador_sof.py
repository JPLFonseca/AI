from avaliador_heur import AvaliadorHeur

class AvaliadorSof(AvaliadorHeur):
    
    # retorna o tipo float
    def prioridade(self,no):
        return self._heuristica.h(no.estado)