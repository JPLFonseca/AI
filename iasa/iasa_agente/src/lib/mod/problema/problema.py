from abc import ABC, abstractmethod

class Problema(ABC):
    # o argumento estado_inicial e do tipo Estado e os argumento operadores e uma lista do tipo Operador
    def __init__(self, estado_inicial, operadores):
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores
    
    @abstractmethod
    # o argumento estado e do tipo Estado e este metodo vai retornar booleano
    def objetivo(self, estado):
        ''''''

    # retorna o valor do estado inicial
    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    # retorna os operadores
    @property
    def operadores(self):
        return self.__operadores