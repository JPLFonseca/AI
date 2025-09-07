from lib.pee.mec_proc.procura_grafo import ProcuraGrafo
from lib.pee.mec_proc.fronteira.fronteira_prioridade import FronteiraPrioridade

class ProcuraMelhorPrim(ProcuraGrafo):

    # o argumento avaliador e do tipo Avaliador
    def __init__(self,avaliador):
        self._avaliador = avaliador
        super().__init__(FronteiraPrioridade(avaliador)) # inicia a fronteira com prioridade

    
    # o argumento no e do tipo No
    # retorna o tipo boolean
    def _manter(self, no):
        return super()._manter(no) or no < self._explorados[no.estado] # reutilizamos o codigo do manter da classe ProcuraGrafo