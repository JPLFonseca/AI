from .procura_prof_lim import ProcuraProfLim
from pee.mec_proc.no import No

class ProcuraProfIter(ProcuraProfLim):
    
    # o argumento problema e do tipo Problema, o argumento inc_prof e um int e o argumento limite_prof e um int
    # retorna o tipo Solucao
    def procurar(self,problema,inc_prof=1,limite_prof=100):

        for i in range(inc_prof,limite_prof+1,inc_prof): 
            self.prof_max = i # atualiza o valor do prof_max
            
            sol = super().procurar(problema) # chama a classe procurar do MecanismoProcura
            if sol:
                return sol