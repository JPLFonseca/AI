from .procura_informada import ProcuraInformada
from .aval.avaliador_sof import AvaliadorSof

class ProcuraSofrega(ProcuraInformada):

    # tem uma dependencia de avaliadorSof
    def __init__(self):
        super().__init__(AvaliadorSof())