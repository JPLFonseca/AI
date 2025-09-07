from lib.ecr.hierarquia import Hierarquia
from controlo_react.reacoes.evitar.evitar_obst import EvitarObst 
from controlo_react.reacoes.aproximar.aproximar_alvo import AproximarAlvo
from controlo_react.reacoes.explorar.explorar import Explorar

class Recolher(Hierarquia):
        
        def __init__(self):
                super().__init__([AproximarAlvo(),EvitarObst(),Explorar()])
