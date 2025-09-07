from lib.mod.estado import Estado

class EstadoLocalidade(Estado):

    def __init__(self,localidade):
        self.localidade = localidade

    # retorna do tipo int
    def id_valor(self):

        # retorna um valor inteiro correspondente ao valor da localidade
        return int(self.localidade[-1])
    
    @property
    def _localidade(self):
        return self.localidade