

class MecUtil():

    def __init__(self,modelo,gama,delta_max):
        """_summary_

        Args:
            modelo (ModeloPDM): contem funcoes que dao acesso ao dominio do problema
            gama (float): aquilo que se retem ao passar o tempo da recompensa
            delta_max (int): criterio em que vamos parar de iterar, correspondente a maior diferenca entre estados
        """
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max

    def utilidade(self):
        """
        Comecar por definicar um dicionario de utilidade
        Vai ao modelo pdm e coloca todos os estados a 0
        Vai iterar, calculando a maior das utilidades da accao
        Reflete o efeito cumulativo de tomada de decisões

        Returns:
            Utilidade
        """
        S, A = self.__modelo.S, self.__modelo.A
        U = {s: 0.0 for s in S()}

        # faz o calculo da utilidade
        while True:

            Uant = U.copy()
            delta = 0

            # vai iterar pelo conjunto de estados do modelo
            for s in S():
                U[s] = max([self.util_acao(s,a,Uant)for a in A(s)],default=0) # max da acao do conjunto de acoes para a utilidade das acoes
                delta = max(delta,abs(U[s]-Uant[s]))
        
            # verifica a condicao
            if(delta <= self.__delta_max):
                break

        return U
        

    def util_acao(self,s,a,U):
        """
        utilidade de um determinado estado fazer uma acao

        somatorio da probabilidade de transicao * gama R * s

        Args:
            s (Estado)
            a (Operador)
            U (Utilidade)

        Returns:
            float
        """

        
        
        T, R, nextState = self.__modelo.T,self.__modelo.R, self.__modelo.nextState

        # vai aplicar a formula
        # vai percorrer todos os estados possiveis


        util = sum(T(s, a, sn) * (R(s, a, sn) + self.__gama * U[sn]) for sn in nextState(s,a))
        return util