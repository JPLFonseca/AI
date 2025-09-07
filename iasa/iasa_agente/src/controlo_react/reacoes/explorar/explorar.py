from lib.ecr.comportamento import Comportamento
from controlo_react.reacoes.resposta.resposta_mover import RespostaMover
from sae import Direccao
import random as rd

class Explorar(Comportamento):

    # tem uma dependencia de recolher

    #retorna o tipo Accao
    def activar(self,percepcao): # gera uma direcao aleatoria, chamar a resposta mover com a direcao aleatoria escolhida e gera uma accao correspondente a resposta mover
        
        dir = rd.choice(list(Direccao))
        resp_mov = RespostaMover(dir)
        resp_mov.activar(percepcao)

        return resp_mov._accao