from lib.pdm.modelo.modelo_pdm import ModeloPDM
from lib.plan.modelo.modelo_plan import ModeloPlan

class ModeloPDMPlan(ModeloPDM,ModeloPlan):

    def __init__(self,modelo_plan,objetivos,rmax=1000):
        """
        Args:
            modelo_plan (ModeloPlan): _description_
            objetivos (List<Estado>): _description_
            rmax (float, optional): recompensa maxima. Defaults to 1000.
        """

        self.__modelo_plan = modelo_plan
        self.__objetivos = objetivos
        self.__rmax = rmax 
        self.__transicoes = {}

        # percorremos todos os estados e para todos estados percorremos todas as acoes
        for s in self.obter_estados():
            for a in self.obter_operadores():
                sn = a.aplicar(s) # aplica a acao o estado
                if sn: # se existir sn
                    self.__transicoes[(s,a)] = sn # vai dizer que existe uma transicao

    def obter_estado(self):
        """
        Returns:
            Estado
        """
        return self.__modelo_plan.obter_estado()
    
    def obter_estados(self):
        """
        Returns:
            List<Estado>
        """
        return self.__modelo_plan.obter_estados()
    
    def obter_operadores(self):
        """
        Returns:
            List<Operador>
        """
        return self.__modelo_plan.obter_operadores()
    
    def S(self):
        return self.obter_estados()
    
    def A(self,s):
        return self.obter_operadores()
    
    def T(self,s,a,sn):

        # se a transicao for igual a transicao no dicionario correspondento aquele estado e acao
        if(sn == self.__transicoes.get((s,a))):
            return 1.0
        else:
            return 0.0
        
    
    def R(self,s,a,sn):

        r = -a.custo(s,sn) # custo da transicao que perdemos
        if sn in self.__objetivos: # se a transicao estiver nos objetivos
            r += self.__rmax # adiciona a recompensa a recompensa maxima

        return r
    
    def nextState(self, s, a):
        ns = self.__transicoes.get((s,a))

        return [ns] if ns else [] # se existir transicao retorna uma lista com o estado sucessor, caso contrario retorna uma lista vazia