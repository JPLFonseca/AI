from abc import abstractmethod
from .comportamento import Comportamento

class ComportComp(Comportamento):

    # comportamentos e uma lista do tipo Comportamento
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos
        

    # percepcao e do tipo Percepcao
    # retornar o tipo Accao
    def activar(self,percepcao):

        list = []

        # vai ativar cada um dos sub comportamentos com a percepcao recebida
        # vai fazer um ciclo for que passa por os comportamentos que ficam ativos de acordo com a percepcao

        for i in range(len(self.__comportamentos)):
            ac = self.__comportamentos[i].activar(percepcao)
            if(ac):
                list.append(ac)
        if(list):
        # retorna uma accao
            return self.selecionar_accao(list)

    # accoes e uma lista do tipo Accao
    # retorna do tipo Accao
    @abstractmethod
    def selecionar_accao(self,accoes):
        ''''''
