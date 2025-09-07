from lib.pee.mec_proc.solucao import Solucao
from plan_traj.mod_prob.problema_plan_traj import ProblemaPlanTraj
from lib.pee.prof.procura_prof_lim import ProcuraProfLim
from lib.pee.larg.procura_largura import ProcuraLargura
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from lib.pee.prof.procura_prof_iter import ProcuraProfIter
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif

class PlaneadorTrajecto:

    # ligacoes e uma lista de Ligacao, loc_inicial e loc_final sao strings
    # o metodo retorna Solucao
    def planear(self,ligacoes,loc_inicial,loc_final):

        # cria uma instancia de problema com os argumentos recebidos para usar no mecanismo de procura
        problema = ProblemaPlanTraj(ligacoes,loc_inicial,loc_final)
        mec_proc = ProcuraProfIter()
    
        solucao = mec_proc.procurar(problema)

        print(mec_proc.__class__.__name__)
        print("Nos em memoria: " + str(mec_proc.max_nos_memoria))
        print("Nos processados: " + str(mec_proc.nos_processados))
        
        # retorna uma solucao
        return solucao
    
        # cria uma instancia de problema
        # preciso de uma instancia de problema e evoca o metodo procurar