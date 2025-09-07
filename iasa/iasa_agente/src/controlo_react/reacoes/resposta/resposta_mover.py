from lib.ecr.resposta import Resposta
from sae import Accao

class RespostaMover(Resposta):
     
     # direcao e do tipo Direccao
     def __init__(self,direccao):
          
          # chama a classe Resposta com uma acao que tem uma direcao
          super().__init__(Accao(direccao))