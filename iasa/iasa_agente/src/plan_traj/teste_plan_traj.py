from planeador.ligacao import Ligacao
from planeador.planeador_trajecto import PlaneadorTrajecto
from plan_traj.planeador.trajecto import Trajecto
from lib.pee.mec_proc.mecanismo_procura import MecanismoProcura
from lib.pee.prof.procura_prof_lim import ProcuraProfLim
from lib.pee.larg.procura_largura import ProcuraLargura
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from lib.pee.prof.procura_prof_iter import ProcuraProfIter
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif


LOC_INICIAL = "loc-0"
LOC_FINAL = "loc-4"

LIGACOES = [Ligacao("loc-0","loc-1",5),
            Ligacao("loc-0","loc-2",25),
            Ligacao("loc-1","loc-3",12),
            Ligacao("loc-1","loc-6",5),
            Ligacao("loc-2","loc-4",30),
            Ligacao("loc-3","loc-2",10),
            Ligacao("loc-3","loc-5",5),
            Ligacao("loc-4","loc-3",2),
            Ligacao("loc-5","loc-6",8),
            Ligacao("loc-5","loc-4",10),
            Ligacao("loc-6","loc-3",15)] # lista de instancia de ligacoes

def teste_plan_traj():

    # cria instancia do planeador
    # gerar uma solucao para a partir da localidade inicial obter um trajeto para a localidade final
    # se existir solucao, cria um trajeto para ela e mostra
    planeador = PlaneadorTrajecto()
    solucao = planeador.planear(LIGACOES,LOC_INICIAL,LOC_FINAL)



    if(solucao):
        
        Trajecto(solucao).mostrar()
        


teste_plan_traj()

'''
ProcuraCustoUnif
Nos em memoria: 7
Nos processados: 7
Solucao: loc-0 loc-1 loc-3 loc-5 loc-4
Dimensao: 5
Custo: 32

ProcuraLargura
Nos em memoria: 7
Nos processados: 6
Solucao: loc-0 loc-2 loc-4
Dimensao: 3
Custo: 55

ProcuraProfundidade
Nos em memoria: 2
Nos processados: 3
Solucao: loc-0 loc-2 loc-4
Dimensao: 3
Custo: 55

ProcuraProfLim
Nos em memoria: 2
Nos processados: 3
Solucao: loc-0 loc-2 loc-4
Dimensao: 3
Custo: 55

ProcuraProfIter
Nos em memoria: 2
Nos processados: 6
Solucao: loc-0 loc-2 loc-4
Dimensao: 3
Custo: 55
'''