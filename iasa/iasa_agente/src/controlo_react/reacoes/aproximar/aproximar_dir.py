
from controlo_react.reacoes.aproximar.estimulo.estimulo_alvo import EstimuloAlvo
from lib.ecr.reaccao import Reaccao 
from controlo_react.reacoes.resposta.resposta_mover import RespostaMover


class AproximarDir(Reaccao):

    # o argumento direccao e do tipo Direccao
    def __init__(self,direccao):
        self.direccao = direccao
        # estimulo alvo
        super().__init__(EstimuloAlvo(direccao),RespostaMover(direccao)) 
