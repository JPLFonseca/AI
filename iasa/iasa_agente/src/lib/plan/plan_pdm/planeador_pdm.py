from lib.plan.planeador import Planeador
from lib.plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from lib.pdm.pdm import PDM
from lib.plan.plan_pdm.plano_pdm import PlanoPDM

class PlaneadorPDM(Planeador):

    def __init__(self,gama=0.85,delta_max=1.0):
        self.__gama = gama
        self.__delta_max = delta_max


    def planear(self, modelo_plan, objetivos):
        """_summary_

        Args:
            modelo_plan (ModeloPlan)
            objetivos (List<Estado>)

        Returns:
            _type_: PlanoPDM
        """

        # criar uma instancia do modelopdmplano
        # criar a instancia de pdm
        # a seguir fazemos resolver e obtemos uma utilidade e uma politica
        # com essa utilidade e essa politica retornamos uma instancia

        modelo_pdm = ModeloPDMPlan(modelo_plan,objetivos)
        pdm = PDM(modelo_pdm,self.__gama,self.__delta_max)
        u, pol = pdm.resolver()

        plano = PlanoPDM(u,pol)

        return plano
        