from abc import ABC,abstractmethod

class ModeloPlan(ABC):

    # retorna o tipo estado
    @abstractmethod
    def obter_estado(self):
        ''''''

    # retorna uma lista de estado
    @abstractmethod
    def obter_estados(self):
        ''''''

    # retorna uma lista de operador
    @abstractmethod
    def obter_operadores(self):
        ''''''  