from lib.pee.mec_proc.mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura):

    def _iniciar_memoria(self):

        # inicar a memoria e inicia um dicionario vazio
        super()._iniciar_memoria()
        self._explorados = {}


    def _memorizar(self, no):

        # verifica a condicao e caso esta seja true, adiciona o no ao dicionario, tendo como key o seu estado e insere o no na fronteira
        if(self._manter(no)):
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)

            #tamanho dos exploradas

    # no e do tipo no e retorna o tipo boolean
    # verifica se o no ja existe no dicionario
    def _manter(self,no):
        return no.estado not in self._explorados
    
    @property
    def max_nos_memoria(self):
        return len(self._explorados)