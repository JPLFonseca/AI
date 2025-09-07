from .fronteira import Fronteira

class FronteiraFIFO(Fronteira):
    
    def inserir(self, no): # vai inserir o no no fim
        self._nos.append(no)