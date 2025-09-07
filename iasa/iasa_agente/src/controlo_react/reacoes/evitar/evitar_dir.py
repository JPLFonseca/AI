
from .estimulo.estimulo_obst import EstimuloObst
from lib.ecr.reaccao import Reaccao

class EvitarDir(Reaccao):

    # direccao e do tipo Direccao e a resposta e do tipo RespostaEvitar
    def __init__(self,direccao,resposta):

        est = EstimuloObst(direccao)
        super().__init__(est,resposta)
        # passar com o estimulo e com a resposta
        
        
