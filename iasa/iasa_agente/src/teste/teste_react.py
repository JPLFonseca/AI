from sae import Controlo
from sae import Simulador
from controlo_react.reacoes.explorar.explorar import Explorar
from controlo_react.controlo_react import ControloReact
from lib.ecr.hierarquia import Hierarquia
from controlo_react.reacoes.recolher import Recolher

# reduzir para apenas 1 comportamento, instancia de explorar

class ControloTeste(Controlo):
    def processar(self,percepcao):
        print("processar")



comportamento = [Recolher()]
controlo = ControloReact(Hierarquia(comportamento))

Simulador(1,controlo).executar()

# controlo = ControloReact(comportamento) precisa de um comportamento composto que tem la dentro uma instancia de explorar