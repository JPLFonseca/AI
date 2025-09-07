from lib.ecr.hierarquia import Hierarquia
from controlo_react.reacoes.evitar.resposta.resposta_evitar import RespostaEvitar
from controlo_react.reacoes.evitar.evitar_dir import EvitarDir
from sae import Direccao

class EvitarObst(Hierarquia):

    # tem uma dependencia de recolher
    def __init__(self):
        self.__resposta = RespostaEvitar()
        super().__init__([EvitarDir(direccao,self.__resposta) for direccao in Direccao])

        #  chama o construtor da classe herdada, com uma lista do evitar direcional em cada direcao e com a mesma resposta para todas as direccoes
        
