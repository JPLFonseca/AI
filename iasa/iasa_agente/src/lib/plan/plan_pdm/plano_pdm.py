from lib.plan.plano import Plano

class PlanoPDM(Plano):

    def __init__(self,utilidade,politica) :
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        """_summary_

        Args:
            estado (Estado)

        Returns:
            Operador: _description_
        """

        # obter o operador correspondente ao estado, atraves da politica

        if(self.__politica):
            return self.__politica.get(estado)
    
    def mostrar(self, vista):
        """_summary_

        Args:
            vista (VistaAmb): _description_
        """
        if(self.__politica): # se existir politica
            vista.mostrar_valor(self.__utilidade) # mostra a utilidade e a politica
            vista.mostrar_politica(self.__politica)