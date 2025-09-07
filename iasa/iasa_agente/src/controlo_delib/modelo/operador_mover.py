from lib.mod.operador import Operador
from sae import Accao
from lib.mod.agente.estado_agente import EstadoAgente
import math

class OperadorMover(Operador):
    
    # modelo_mundo e do tipo ModeloMudno e direcao e do tipo Direccao
    def __init__(self,modelo_mundo,direccao):
        self.__ang = direccao.value
        self.__accao = Accao(direccao)

        self.__modelo_mundo = modelo_mundo

    # o argumento estado e do tipo Estado
    # retorna o tipo Estado
    def aplicar(self,estado):

        # simular a translacao geometrica

        # calculo do dx e do dy utilizando o passo( ver os slides)
        # as accoes da sae tem um atributo passo
        # usar o x e o y da posicao

        x,y = estado.posicao

        dx = round(self.accao.passo * math.cos(self.__ang))
        dy = round(- self.accao.passo * math.sin(self.__ang))

        # cria uma nova posicao
        nova_posicao = (x + dx, y + dy)

        # cria um novo estado
        novo_estado = EstadoAgente(nova_posicao)

        # modeloMundo tem um metodo obterEstados, que vai servir para validar o novo_estado criado. Ou seja, se o estado criado for um dos estados validos do modelo do mundo, retorn o estado
        if(novo_estado in self.__modelo_mundo.obter_estados()):
            return novo_estado
    
    # estado e estado suc sao do tipo Estado
    # retorna um float
    def custo(self,estado,estado_suc):

        # o custo tem um valor minimo de 1

        distancia = math.dist(estado_suc.posicao,estado.posicao)
        
        # retorna a distancia se esta for maior que 1, caso contrario retorna 1
        return max(distancia,1)
        

    # retorna um float
    @property
    def ang(self):
        return self.__ang
    
    # retorna o tipo Accao
    @property
    def accao(self):
        return self.__accao