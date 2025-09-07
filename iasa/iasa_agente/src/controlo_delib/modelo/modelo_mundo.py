from controlo_delib.modelo.operador_mover import OperadorMover
from lib.mod.agente.estado_agente import EstadoAgente
from sae import Direccao
from lib.plan.modelo.modelo_plan import ModeloPlan
import math

class ModeloMundo(ModeloPlan):

    # tem um lista de operadores, lista de estado e de estados, lista publica de elementos

    def __init__(self):
        self.__estado = None
        self.__estados = [] # lista vazia
        self.__elementos = {} # dicionario
        self.__operadores = [OperadorMover(self,direccao) for direccao in Direccao]
        self.__alterado = False

    
    # retorna o tipo Estado
    def obter_estado(self):
        return self.__estado
    
    # retorna uma lista de Estado
    def obter_estados(self):
        return self.__estados
    
    # retorna uma lista de Operador
    def obter_operadores(self):
        return self.__operadores

    # o argumento estado e do tipo Estado
    # retorna o tipo Elemento
    def obter_elemento(self,estado):

        # retorna o elementos que esta nos elementos indexado pelo posicao do estado

        return self.elementos.get(estado.posicao)
    
    # o argumento distancia estado e do tipo EstadoAgente
    # retorna um float
    def distancia(self,estado):
        return math.dist(self.__estado.posicao,estado.posicao)
    
    # o argumento percepcao era do tipo Percepcao
    # nao tem return
    def actualizar(self,percepcao):

        # na percepcao da sae, vem um imagem do mundo, que tem informacao sobre todos os elementos do mundo
        # atualizar o estado , com uma instancia de EstadoAgente, cujo a posicao e a que vem na percepcao
        self.__estado = EstadoAgente(percepcao.posicao)

        # se os elementos do mundo forem diferentes dos que veeem na percepcao, vamos atualizar
        # vamos colocar os elementos aos elementos da percepcao
        if(self.__elementos != percepcao.elementos):
            self.__elementos = percepcao.elementos 
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
            self.__alterado = True
        else:
            self.__alterado = False
    
    # o argumento vista e do tipo VistaAmb
    # nao tem return
    def mostrar(self,vista):
        
        vista.mostrar_alvos_obst(self.__elementos) # pega nos elementos e mostra os alvos e os obstaculos
        vista.marcar_posicao(self.__estado.posicao)
    
    @property
    def alterado(self):
        return self.__alterado
    
    @property
    def elementos(self):
        return self.__elementos