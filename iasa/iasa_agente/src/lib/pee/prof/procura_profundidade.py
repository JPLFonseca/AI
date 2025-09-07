from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):

    #inicia o mecanismo de procura no modo lifo, last in first out
    def __init__(self):
        self.__nos_memoria_max = 0
        super().__init__(FronteiraLIFO())
    
    # insere o no na fronteira
    def _memorizar(self, no):

        self._fronteira.inserir(no)

        '''if self._fronteira.dimensao > self.__nos_mem_max:
                self.__nos_mem_max = self._fronteira.dimensao
        '''
        if ((num_nos_mem := self._fronteira.memoria) > (self.__nos_memoria_max)):
            self.__nos_memoria_max = num_nos_mem

    @property
    def max_nos_memoria(self):
        return self.__nos_memoria_max

    