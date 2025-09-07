from abc import abstractmethod
from lib.mod.estado import Estado
from lib.mod.operador import Operador
from lib.mod.problema.problema import Problema
from plan_traj.planeador.trajecto import Trajecto
from lib.pee.prof.procura_prof_lim import ProcuraProfLim
from lib.pee.prof.procura_prof_iter import ProcuraProfIter
from lib.pee.larg.procura_largura import ProcuraLargura
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif

class EstadoDeposito(Estado):

	def __init__(self,volume):
		self.__volume = volume
		self.__id_valor = hash(self.__volume)

	@property
	def volume(self):
		return self.__volume

	
	def id_valor(self):
		return self.__id_valor


class OperadorTransferir(Operador):

	def __init__(self,volume):
		self._volume = volume
	
	@abstractmethod
	def aplicar(self,estado):
		'''Aplicar operador ao estado'''

	def custo(self,estado,estado_suc):
		return abs(estado_suc.volume - estado.volume) ** 2
    
class OperadorEncher(OperadorTransferir):
	
    def aplicar(self,estado):
        return EstadoDeposito(estado.volume + self._volume)
    
    def __repr__(self):
        return "Encher(%s)" % self._volume



class OperadorVazar(OperadorTransferir):
	
	def aplicar(self,estado):
		novo_volume = estado.volume - self._volume
		if novo_volume < 0:
			novo_volume = 0
		return EstadoDeposito(novo_volume)

	def __repr__(self):
		return "Vazar(%s)" % self._volume
	



class ProblemaDeposito(Problema):

	def __init__(self,volume_inicial,volume_final):
		super().__init__(EstadoDeposito(volume_inicial),[OperadorEncher(2),OperadorEncher(3),OperadorVazar(2),OperadorVazar(3)])
		self.__volume_final = volume_final

	def objetivo(self,estado):
		return estado.volume == self.__volume_final
	


# trajeto e uma lista de nomes de localidades, representado com uma lista de nomes de localidades
class TrajectoDeposito(Trajecto):

    # argumento solucao do tipo Solucao
    def __init__(self,solucao):

        
        self.__percurso = list(solucao.__iter__())
        self.__dimensao = solucao.dimensao
        self.__custo = self.__percurso[-1].custo # custo do ultimo no e o custo total
       
    

    def mostrar(self):

        print("Solucao: ", end="")

        for no in self.__percurso:
            print(str(no.operador), end=" ")
            
        print("\nDimensao: " + str(self.__dimensao))
        print("Custo: " + str(self.__custo))

	


VOL_INICIAL = 1
VOL_FINAL = 9

problema = ProblemaDeposito(VOL_INICIAL,VOL_FINAL)

mec_proc = ProcuraCustoUnif()

solucao = mec_proc.procurar(problema)

print(mec_proc.__class__.__name__)
print("Nos em memoria: " + str(mec_proc.max_nos_memoria))
print("Nos processados: " + str(mec_proc.nos_processados))

if(solucao):
        
        TrajectoDeposito(solucao).mostrar()
	
'''

ProcuraProfLim
Nos em memoria: 13
Nos processados: 10
Solucao: Vazar(3) Encher(3) Encher(3) Vazar(2) Vazar(2) Encher(3) Encher(3) Encher(3) Vazar(2)
Dimensao: 10
Custo: 58

ProcuraProfIter
Nos em memoria: 6
Nos processados: 44
Solucao: Encher(3) Encher(3) Encher(2)
Dimensao: 4
Custo: 22

ProcuraLargura
Nos em memoria: 12
Nos processados: 10
Solucao: Encher(2) Encher(3) Encher(3)
Dimensao: 4
Custo: 22

ProcuraCustoUnif
Nos em memoria: 11
Nos processados: 9
Solucao: Encher(2) Encher(2) Encher(2) Encher(2)
Dimensao: 5
Custo: 16

'''