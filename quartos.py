from abc import ABC
class Quarto(ABC):
    def __init__(self, numero="indefinido", tipo="indefinido", preco_diaria=0):
        super().__init__()

        self.numero=numero
        self.tipo=tipo
        self._preco_diaria=preco_diaria
        self._ocupado = False
        
    
    @property
    def ocupado(self):
        return self._ocupado
    
    @ocupado.setter
    def ocupado(self,valor):
        self._ocupado=valor
    @property
    def preco_diaria(self):
        return self._preco_diaria
    
    @preco_diaria.setter
    def preco_diaria(self,valor):
        if valor < 0:
            print("preço da diaria não pode ser negativo!")
        else:
            self._preco_diaria=valor
    
    def mostrar_informacoes(self):
        status = "Ocupado" if self._ocupado else "Disponível"
        print(f" - Quarto {self.numero} - {self.tipo} | Diária: €{self.preco_diaria:.2f} | Status: {status}")
        

class QuartoSimples(Quarto):
    def __init__(self, numero, preco_diaria=300):
        super().__init__(numero, "Simples", preco_diaria)
        self.preco_diaria=preco_diaria
    
    @property
    def preco_diaria(self):
        return self._preco_diaria
    
    @preco_diaria.setter
    def preco_diaria(self,valor):
        if valor < 0:
            print("preço da diaria não pode ser negativo!")
        else:
            self._preco_diaria=valor
        

class QuartoLuxo(Quarto):
    def __init__(self, numero, preco_diaria=1000):
        super().__init__(numero, "Luxo", preco_diaria)
        self.preco_diaria=preco_diaria
    
    @property
    def preco_diaria(self):
        return self._preco_diaria
    
    @preco_diaria.setter
    def preco_diaria(self,valor):
        if valor < 0:
            print("preço da diaria não pode ser negativo!")
        else:
            self._preco_diaria=valor


