from .comportamento import Comportamento

# vai associar os estimulos as respetivas respostas
class Reaccao(Comportamento):
    def __init__(self,estimulo,resposta):
        self.__estimulo = estimulo  # e do tipo Estimulo
        self.__resposta = resposta  # e do tipo Reposta

    # faz return do tipo Accao
    # percepcao e do tipo percepcao
    def activar(self,percepcao): 
        intensidade = self.__estimulo.detectar(percepcao)

        if(intensidade > 0):
            return self.__resposta.activar(percepcao,intensidade)