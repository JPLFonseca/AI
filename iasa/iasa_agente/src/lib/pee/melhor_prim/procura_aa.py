from .procura_informada import ProcuraInformada
from .aval.avaliador_aa import AvaliadorAA

class ProcuraAA(ProcuraInformada):

    # tem uma dependencia a avaliadorAA
    def __init__(self):
        super().__init__(AvaliadorAA())