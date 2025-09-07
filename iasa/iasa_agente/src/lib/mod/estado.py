from abc import ABC, abstractmethod


class Estado(ABC):



    @abstractmethod
    # retorna do tipo int
    def id_valor(self) :
        ''''''

    # retorna um numero inteiro (int) que e uma identificacao unica de um objeto
    def __hash__(self):
        return self.id_valor()

    # other e um objeto
    # corresponde ao operador =
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()