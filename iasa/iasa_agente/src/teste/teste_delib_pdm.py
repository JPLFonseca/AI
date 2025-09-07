from controlo_delib.controlo_delib import ControloDelib
from lib.plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Simulador


controlo = ControloDelib(PlaneadorPDM())

Simulador(3,controlo).executar()