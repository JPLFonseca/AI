from lib.ecr.estimulo import Estimulo
from sae import Elemento

class EstimuloObst(Estimulo):

    def __init__(self,direccao,intensidade=1):
        
        self.__direccao = direccao
        self.__intensidade = intensidade
    
    # retorna o tipo float
    # percepcao e do tipo Percepcao
    def detectar(self,percepcao):
        elem, dist, _ = percepcao.per_dir[self.__direccao]
        # deteta se existe um obtstaculo e retorna zero se nao existir

        return self.__intensidade ** dist if elem == Elemento.OBSTACULO else 0
