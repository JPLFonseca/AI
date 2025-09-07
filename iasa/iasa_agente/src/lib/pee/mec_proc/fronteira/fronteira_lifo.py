from .fronteira import Fronteira

class FronteiraLIFO(Fronteira):
    
    def inserir(self, no):
        
        # insero um no no inicio
        self._nos.insert(0,no) 