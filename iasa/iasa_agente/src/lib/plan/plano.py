from abc import ABC,abstractmethod

class Plano(ABC):

    # retorna o tipo Operador
    @abstractmethod
    def obter_accao(self,estado):
        ''''''

    # vista e do tipo VistaAmb
    @abstractmethod
    def mostrar(self,vista):
        ''''''