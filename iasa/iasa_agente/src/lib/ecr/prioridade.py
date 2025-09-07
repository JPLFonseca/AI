from .comport_comp import ComportComp


# as acoes tem uma prioridade associada, que vai definir os modo como estas vao ser selecionadas
class Prioridade(ComportComp):

    # retorna do tipo Accao
    def selecionar_accao(self,accoes):

        # vai order a lista de accoes de acordo com a sua prioridade. Para isso vai utilizar o metodo prioridade de accao e a
        # funcao max do python

        if(accoes is not None):
            return max(accoes, key=lambda accao: accao.prioridade)
                   
        
