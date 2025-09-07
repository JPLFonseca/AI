from abc import ABC, abstractmethod

class Avaliador(ABC):

    # retorna um float
    @abstractmethod
    def prioridade(self,no):
        ''''''