from sae import Controlo
from sae import Simulador

#Controlo teste

class ControloTeste(Controlo):
    def processar(self,percepcao):
        print("processar")

#instancia do controlo
controlo = ControloTeste()

Simulador(1,controlo).executar()