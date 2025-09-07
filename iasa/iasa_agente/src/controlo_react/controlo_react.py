from sae import Controlo

class ControloReact(Controlo):

    # inicializa o comportamento
    def __init__(self,comportamento):
        self.__comportamento = comportamento
    
    #retorna o tipo Accao
    def processar(self,percepcao):

        # ativa o comportamento de acordo com a percepcao recebida

        if(percepcao is not None):
            return self.__comportamento.activar(percepcao)
        