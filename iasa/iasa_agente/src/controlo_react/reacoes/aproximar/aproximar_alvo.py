
from lib.ecr.prioridade import Prioridade 
from controlo_react.reacoes.aproximar.aproximar_dir import AproximarDir
from sae import Direccao

class AproximarAlvo(Prioridade):
    
    # tem uma dependencia de Recolher
    def __init__(self):


        # o comportamento tem por objetivo aproximar o alvo mais proximo, que atraves de um mecanismo de selecao de acao por prioridade
        # vai determinar o alvo mais proximo

        list = []
        list.append(AproximarDir(Direccao.NORTE))
        list.append(AproximarDir(Direccao.SUL))
        list.append(AproximarDir(Direccao.ESTE))
        list.append(AproximarDir(Direccao.OESTE))

        super().__init__(list)
