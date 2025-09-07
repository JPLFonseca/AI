from controlo_react.reacoes.resposta.resposta_mover import RespostaMover
from sae import Direccao
from random import choice

class RespostaEvitar(RespostaMover):

    def __init__(self,dir_inicial=Direccao.OESTE):

        self.dir_inicial = dir_inicial
        self.__direccoes = Direccao
        super().__init__(dir_inicial)
        
    
    # retornda o tipo Accao
    # percepcao e do tipo Percepcao e intensidade e do tipo float
    def activar(self,percepcao,intensidade):

        contacto_obst = percepcao.contacto_obst(self._accao.direccao) # se existir contato com o obstaculo

        if contacto_obst:
            contacto_obst = self.__alterar_direccao(percepcao)
        
        if not contacto_obst:
            return super().activar(percepcao,intensidade)
            
    
    # retorna o tipo Direccao
    # percepcao e do tipo Percepcao
    def __direccao_livre(self,percepcao):
        
        direccoes_livres = [direccao for direccao in self.__direccoes if not percepcao.contacto_obst(direccao)]

        if(direccoes_livres):
            return choice(direccoes_livres)
        # retorna uma lista com todas as direccoes livres

    
    def __alterar_direccao(self,percepcao):

        nova_dir = self.__direccao_livre(percepcao)
        if(nova_dir):
            # altera a direccao da acao
            self._accao.direccao = nova_dir
            return nova_dir
    
