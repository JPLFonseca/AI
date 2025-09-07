from .procura_profundidade import ProcuraProfundidade
from lib.pee.mec_proc.no import No

class ProcuraProfLim(ProcuraProfundidade):

    # prof_max e do tipo int
    def __init__(self,prof_max=100):
        self._prof_max = prof_max
        super().__init__()

    # o argumento problema e do tipo Problema e argumento no e do tipo No
    # retorna Yield No 
    def _expandir(self,problema,no):
        
        if(no.profundidade < self._prof_max): # verifica se a profundidade do no e inferior a profundidade maxima

            for node in super()._expandir(problema,no):
                yield No(node.estado,node.operador,no) # faz yield do expandir classe mecanimso_procura com o problema e o no
    
    # o argumento no e do tipo No
    def _memorizar(self, no):
        if(not self._ciclo(no)): # verifica se o no e um ciclo no ramo respetivo
            super()._memorizar(no) # memoriza o no caso este nao seja um ciclo
    

    # o argumento no e do tipo No 
    # retorna um booleano
    def _ciclo(self,no):
        return no.estado in self.__estados_antecessores(no)

        '''
        no_ante = no.antecessor

        while no_ante:
            if(no.estado == no_ante.estado):
                return True
            no_ante = no_ante.antecessor # Se o estado do no atual nao for igual ao estado do no antecessor,
                                        # atualiza o no antecessor, para o antecessor do no antecessor atual. 

            return False'''
            

    def __estados_antecessores(self,no):

        no_ante = no.antecessor

        while no_ante:
            yield no_ante.estado
            no_ante = no_ante.antecessor

    @property
    def prof_max(self):
        return self._prof_max
    
    @prof_max.setter
    def prof_max(self,prof_max):
        self._prof_max = prof_max