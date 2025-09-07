from sae import Controlo
from controlo_delib.modelo.modelo_mundo import ModeloMundo
from controlo_delib.mec_delib import MecDelib


class ControloDelib(Controlo):


    # o argumento planeador e do tipo Planeador
    def __init__(self,planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__objetivos = None # inicialmente e iniciado a None. E uma lista de EstadoAgente
        self.__plano = None

    # percepcao e do tipo Percepcao
    # retorna o tipo Accao
    def processar(self, percepcao):

        self.__assimilar(percepcao)

        if(self.__reconsiderar()):
            self.__deliberar()
            self.__planear()
        
        self.__mostrar()
        accao = self.__executar()

        return accao
    
    # percepcao e do tipo Percepcao
    # nao tem return
    def __assimilar(self,percepcao):

        # sobre o modelo do mundo, atualiza-o
        self.__modelo_mundo.actualizar(percepcao)
    
    # retorna um boolean
    def __reconsiderar(self):
        
        # verifica se e necessario reconsiderar

        # e necessario reconsiderar: se o modelo do mundo se tiver alterado ou o plano estiver vazio or for None
        if(self.__modelo_mundo.alterado or not self.__plano):
            return True
        else:
            return False
    
    # nao tem return
    def __deliberar(self):
        
        # vai atualizar os objetivos com o que o mecanismo de deliberacao produzir
        self.__objetivos = self.__mec_delib.deliberar()
    
    # nao tem return
    def __planear(self):

        # dado os objetivos que o agente tem, gera um plano para executar
        self.__plano = self.__planeador.planear(self.__modelo_mundo,self.__objetivos)
        
    
    # retorna o tipo Accao
    def __executar(self):

        print(self.__modelo_mundo.obter_estado())


        estado_atual = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
        # o executar vai ao plano, buscar a accao para o estado atual do agente, para retornar essa accao

        

        return estado_atual
    
    # nao tem return
    def __mostrar(self):

        # mostrar o modelo do mundo e mostrar o plano atual

        self.__modelo_mundo.mostrar(self.vista)

        if self.__plano is not None:
            self.__plano.mostrar(self.vista)

        '''
        if self.__objetivos:
            self.__objetivos.mostrar(self.vista)
        '''
