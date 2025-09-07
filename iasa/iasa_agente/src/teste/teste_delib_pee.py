from controlo_delib.controlo_delib import ControloDelib
from lib.plan.plan_pee.planeador_pee import PlaneadorPEE
from lib.plan.plan_pee.mod_prob.heur_dist import HeurDist,HeurManhattan
from sae import Simulador


#controlo = ControloDelib(PlaneadorPEE())


# cria o planeador e define a heuristica
planeador = PlaneadorPEE()
planeador.setHeur(HeurManhattan)

controlo = ControloDelib(planeador)

Simulador(4,controlo).executar()