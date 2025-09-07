from abc import ABC, abstractmethod

class Planeador(ABC): # interface

    # o argumento modelo_plan e do tipo ModeloPlan, o argumento objetivos e uma lista de Estado
    # retorna o tipo Plano
    @abstractmethod
    def planear(self,modelo_plan,objetivos):
        ''''''