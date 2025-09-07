from .fronteira import Fronteira
from heapq import heappush,heappop

class FronteiraPrioridade(Fronteira): 

    # o argumento avaliador e do tipo avaliador
    def __init__(self,avaliador):
        super().__init__()
        self.__avaliador = avaliador

    # o argumento no e do tipo No
    def inserir(self,no):
        prioridade = self.__avaliador.prioridade(no) # avalia a prioridade do no
        heappush(self._nos,(prioridade,no)) # nos com prioridade associada
    
    # retorna o tipo No
    def remover(self):
        prioridade,no = heappop(self._nos)
        return no