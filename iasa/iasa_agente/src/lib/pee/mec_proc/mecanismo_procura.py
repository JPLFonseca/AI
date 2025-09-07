from abc import ABC, abstractmethod, abstractproperty
from .no import No
from .fronteira.fronteira import Fronteira
from mod.problema.problema import Problema
from mod.operador import Operador
from mod.estado import Estado
from .solucao import Solucao

class MecanismoProcura(ABC):

    def __init__(self,fronteira):
       self._fronteira = fronteira
       self.__nos_processados = 0

    # limpa a fronteiras
    def _iniciar_memoria(self):
        self._fronteira.iniciar()
    
    # no é do tipo NO
    @abstractmethod
    def _memorizar(self,no):
        ''''''

    # problema e do tipo Problema e retorna o tipo Solucao
    def procurar(self,problema):
        self._iniciar_memoria()
        no = No(problema.estado_inicial) # aceder ao estado inicial
        self._memorizar(no)

        

        while(not self._fronteira.vazia):

            self.__nos_processados = self.__nos_processados + 1
            no = self._fronteira.remover() # retira o primeiro no da fronteira e ve se ele e objetivo
            

            

            if(problema.objetivo(no.estado)):


                ### retorna o numero maximo de nos mantido em memoria ###
                #self._fronteira.memoria()
                

                return Solucao(no)
            else:
                for noSucessor in self._expandir(problema,no):
                    # vai adicionar a lista os nos expandidos, para cada no que ele expandir
                    self._memorizar(noSucessor)
                    


    
    # problema e do tipo Problema e no e do tipo No
    # retorna o tipo Yield<No>
    def _expandir(self,problema,no):

        for operador in problema.operadores:
            EstadoSucessor = operador.aplicar(no.estado)
            
            

            if(EstadoSucessor): # verifica se existe estado sucessor
               
               yield No(EstadoSucessor,operador,no)

    @property
    def nos_processados(self):
        return self.__nos_processados

    @abstractproperty
    def max_nos_memoria(self):
        ''''''