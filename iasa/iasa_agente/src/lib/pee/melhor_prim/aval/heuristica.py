from abc import ABC, abstractmethod

class Heuristica(ABC):

    # estado e do tipo Estado
    # retorna float
    @abstractmethod
    def h(self,estado): # implementa a funcao heuristica, estimativa de custo ate ao no
        ''''''