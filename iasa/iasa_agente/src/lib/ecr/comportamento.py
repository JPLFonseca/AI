
from abc import ABC, abstractmethod

# e uma interface porque nao define nenhuma estrutura apenas o comportamento expresso de forma dinamica
# class porque queremos garantir a compatibilidade funcional
class Comportamento(ABC):

    # retorna o tipo Accao
    @abstractmethod
    def activar(self,percepcao):
        """"""""