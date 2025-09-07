from .procura_melhor_prim import ProcuraMelhorPrim
from .aval.avaliador_custo_unif import AvaliadorCustoUnif

class ProcuraCustoUnif(ProcuraMelhorPrim):

    def __init__(self): # vai dar prioridade a nos que tenham o custo ate ao no o mais baixo possivel

        super().__init__(AvaliadorCustoUnif())

        
        