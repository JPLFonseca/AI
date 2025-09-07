from sae import Elemento


class MecDelib:

    # modelo_mundo e do tipo ModeloMundo
    def __init__(self,modelo_mundo):
        self.__modelo_mundo = modelo_mundo

    # retorna uma lista de Estado
    def deliberar(self):

        # vai atualizar os objetivos
        # vai gerar os objetivos do agente, utilizando o modelo do mundo
        objetivos = [estado for estado in self.__modelo_mundo.obter_estados() if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO] # coloca o estado na lista, se o elemento daquele estado for um alvo

        # vai retornar os objetivos, uma lista de estados que sao os objetivos
        # a lista de objetivos tem de ser ordena de acordo com a distancia a posicao atual do agente


        if objetivos:
            objetivos.sort(key=self.__modelo_mundo.distancia) # vai ordenar o array de acordo com a distancia ao alvo
            return objetivos