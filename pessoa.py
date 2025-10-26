from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self,nome,idade):
        self._nome=nome
        self._idade=idade
    
    @property 
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,valor):
        self._nome=valor

    @property 
    def idade(self):
        return self._idade
    
    @idade.setter 
    def idade(self):
        pass

    @abstractmethod
    def mostrar_informacoes(self):
        pass

class Hospede(Pessoa):
    lista_quartos=[]
    def __init__(self, nome, idade, dias_estadia, quarto=None):
        super().__init__(nome, idade)

        self.dias_estadia=dias_estadia
        self._quarto=quarto
    @property
    def quarto(self):
        return self._quarto
    
    @quarto.setter
    def quarto(self,novo_quarto):
        self._quarto=novo_quarto
        
    def atribuir_quarto(self):
        h=Hospede()
        h.quarto="1"

        

    
    def calcular_conta(self,valor_total_estadia):
        return valor_total_estadia#continuar
    
    def mostrar_informacoes(self):
        print(f"\nNome do Hospede: {self.nome}\nIdade: {self.idade}\nNº Quarto: {self.quarto}")
    
    def checkout(self):
        #Continuar
        print(f"Fez {self.nome} checkout do quarto: {self.quarto}(quarto disponivel)")


