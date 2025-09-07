from lib.pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

class AvaliadorAA(AvaliadorHeur):

    # retorna float
    def prioridade(self,no): # minimizacao do custo global
        return (no.custo + self._heuristica.h(no.estado))