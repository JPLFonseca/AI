
from lib.ecr.estimulo import Estimulo
from sae import Elemento

class EstimuloAlvo(Estimulo):

    # direccao e do tipo Direccao e gama e um float
    def __init__(self,direccao,gama=0.9):


        self.__direccao = direccao
        self.__gama = gama
        
    
    # percepcao e do tipo Percepcao
    def detectar(self,percepcao):


        elem, dist, _ = percepcao.per_dir[self.__direccao]


        # caso o elemente detetado seja um alvo, retorna o gama elevado a distancia. Caso contrario retorna false
        return self.__gama ** dist if elem == Elemento.ALVO else 0