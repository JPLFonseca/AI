from abc import abstractmethod
from lib.mod.estado import Estado
from lib.mod.operador import Operador
from lib.mod.problema.problema import Problema
from plan_traj.planeador.trajecto import Trajecto
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from lib.pee.melhor_prim.procura_aa import ProcuraAA
from lib.pee.melhor_prim.aval.heuristica import Heuristica
from copy import deepcopy

class EstadoEmp(Estado):

    def __init__(self,config):
        self.__config = config
        self.__id_valor = hash(tuple(tuple(i)for i in config)) # criar um tuplo para hash

    @property
    def config(self):
        return self.__config # retorna a configuracao

    def id_valor(self):
        return self.__id_valor
    
class Mover(Operador):
    def __init__(self,idx):
        self._idx = idx
    
    @abstractmethod
    def aplicar(self,idx):
        '''Aplicar operador ao estado'''

    def custo(self,estado,estado_suc):
        return self._idx
    
class Empilhar(Mover):
    
    def aplicar(self,estado):
    
        
        new_conf = deepcopy(estado.config) # faz uma copia da lista
        if(new_conf[self._idx]): # verifica se existem elementos naquele indice
            new_conf[0].append(new_conf[self._idx][0]) # coloca no indice[0][0] o elemento da lista que esta
            new_conf[self._idx].pop(0) # retira o elemento do indice
        return EstadoEmp(new_conf)
    
    def __repr__(self):
        return "Empilhar(%s)" % str(self._idx) # mostra na consola o operador



class Desempilhar(Mover):
    
    def aplicar(self,estado):
        new_conf = deepcopy(estado.config)
        if(new_conf[0]):
              new_conf[self._idx].append(new_conf[0][0])
              new_conf[0].pop(0)
        return EstadoEmp(new_conf)
        
    
    def __repr__(self):
          return "Desempilhar(%s)" % str(self._idx)

class ProblemaEmp(Problema):

    def __init__(self,conf_inicial,conf_final):
        super().__init__(EstadoEmp(conf_inicial),[Empilhar(1),Empilhar(2),Desempilhar(1),Desempilhar(2)])
        self.__conf_final = conf_final

    def objetivo(self,estado_emp):
        return estado_emp.config == self.__conf_final
    
class TrajectoEmp(Trajecto):

    # argumento solucao do tipo Solucao
    def __init__(self,solucao):

        self.__path = [] 
        self.__seq = [] 

        for i in range(solucao.dimensao):
            if(i != 0):
                operador = solucao.__getitem__(i-1).operador
                if(operador):
                    self.__path.append(str(operador))
        
        
            estado = solucao.__getitem__(i).estado
            self.__seq.append(str(estado.config))  # coloca num array a configuracao pela qual passou     


        self.__path.append(str(solucao.__getitem__(-1).operador))  
        self.__dimensao = len(self.__path)
        self.__custo = (solucao.__getitem__(-1)).custo # custo do ultimo no e o custo total
       
    

    def mostrar(self):

        print("Solucao: ", end="\n")

        for op,seq in zip(self.__path,self.__seq):
            print(str(seq),str(op), end=" \n")

        print(str(CONF_FINAL))
            
        print("\nDimensao: " + str(self.__dimensao))
        print("Custo: " + str(self.__custo))

class HeurBlocos(Heuristica):

    def __init__(self,estado_final):
        self.__estado_final = estado_final

    def h(self, estado):
        dis = 0
        
        for i in range(len(estado.config)):
            lista_blocos = estado.config[i]

            for j in range(len(lista_blocos)):
                bloco = lista_blocos[j]

                if bloco not in self.__estado_final.config[i]:
                    dis += 1

        return dis

    

CONF_INICIAL = [[2, 3, 1],[],[]]
CONF_FINAL = [[1,2,3],[],[]]

problema = ProblemaEmp(CONF_INICIAL,CONF_FINAL)
mec_proc = ProcuraAA()

solucao = mec_proc.procurar(problema,HeurBlocos(EstadoEmp(CONF_FINAL)))

print(mec_proc.__class__.__name__)
print("Nos em memoria: " + str(mec_proc.max_nos_memoria))
print("Nos processados: " + str(mec_proc.nos_processados)) 

if(solucao):
        
       traj = TrajectoEmp(solucao)
       traj.mostrar()

'''
ProcuraCustoUnif
Nos em memoria: 26
Nos processados: 14
Solucao:
[[2, 3, 1], [], []] Desempilhar(1)
[[3, 1], [2], []] Desempilhar(1)
[[1], [2, 3], []] Empilhar(1)
[[1, 2], [3], []] Empilhar(1)
[[1, 2, 3], [], []]

Dimensao: 4
Custo: 4


ProcuraAA
Nos em memoria: 15
Nos processados: 7
Solucao:
[[2, 3, 1], [], []] Desempilhar(1)
[[3, 1], [2], []] Empilhar(1)
[[3, 1, 2], [], []] Desempilhar(1)
[[1, 2], [3], []] Empilhar(1)
[[1, 2, 3], [], []]

Dimensao: 4
Custo: 4
'''