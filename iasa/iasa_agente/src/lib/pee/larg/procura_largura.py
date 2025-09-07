from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.mec_proc.fronteira.fronteira_fifo import FronteiraFIFO

class ProcuraLargura(ProcuraGrafo):

    # vai inicializar o procura grafo com a classe FronteiraFIFO, first in first out
    def __init__(self):
        super().__init__(FronteiraFIFO())
