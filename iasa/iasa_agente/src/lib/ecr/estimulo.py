from abc import ABC, abstractmethod


# esta classe abstrata e importante por ser uma ferramente base para lidar com a complexidade, focando-se apenas realcar o essencial, simplificando-a
class Estimulo(ABC):


    # retorna do tipo float
    @abstractmethod
    def detectar(self,percepcao):
        """""" #metodo abstrato
