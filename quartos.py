from abc import ABC
class Quarto(ABC):
    def __init__(self, numero="indefinido", tipo="indefinido", preco_diaria=0):
        super().__init__()

        self.numero=numero
        self.tipo=tipo
        self._preco_diaria=preco_diaria
    
    @property
    def ocupado(self):
        return self._ocupado
    
    @property
    def preco_diaria(self):
        return self._preco_diaria
    
    @preco_diaria.setter
    def preco_diaria(self,valor):
        if valor<0:
            print("preço da diaria não pode ser negativo!")
        else:
            self._preco_diaria=valor
    
    def mostrar_informacoes(self):
        status="Ocupado" if self.ocupado else "Disponível"
        print(f"Nº do quarto: {self.numero}, Tipo: {self.tipo}, Preço da diária: {self.preco_diaria}, Status: {status}")

class QuartoSimples(Quarto):
    def __init__(self, numero=101, preco_diaria=300):
        super().__init__(numero, "Simples", preco_diaria)
        self._ocupado=False

class QuartoLuxo(Quarto):
    def __init__(self, numero, preco_diaria):
        super().__init__(numero, "Luxo", preco_diaria)
        self._ocupado=False

