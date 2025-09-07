from lib.pdm.mec_util import MecUtil

class PDM:

    def __init__(self,modelo,gama,delta_max):
        """

        Args:
            modelo (ModeloPDM)
            gama (float): aquilo que se retem ao passar o tempo da recompensa
            delta_max (int): criterio em que vamos parar de iterar, correspondente a maior diferenca entre estados
        """
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo,gama,delta_max)

    def politica(self,U):
        """colocar o metodo correspondente ao estado e a acao em 2 variaveis

            em cada estado escolher a acao que leva ao estado seguinte com maior utilidade

            para cada estado, vai escolher uma acao

        Args:
            U (Utilidade)

        Returns:
            Politica
        """
        S, A = self.__modelo.S, self.__modelo.A
        pol = {}
        for s in S():
            if(A(s)): # se existirem acoes para aquele estado, calculo a sua politica
                pol[s] = max(A(s),key=lambda a: self.__mec_util.util_acao(s,a,U))

        return pol
    
    def resolver(self):
        """

        calcular a utilidade
        depois a politica
        retornar a utilidade e politica

        Returns:
            Tuple<Utilidade,Politica>
        """
        
        U = self.__mec_util.utilidade()
        pol = self.politica(U)
        return U,pol