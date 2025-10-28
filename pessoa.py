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
        
    def atribuir_quarto(self,quarto=None):
        print("----------Quartos do Hotel------------")
        
        lista_quartos=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
        for quarto in lista_quartos:
            quarto.mostrar_informacoes()

        n_quarto=int(input("\nNª quarto que você deseja: "))
        self._quarto=n_quarto

        if n_quarto==101:
            if q1.ocupado==True:
                print("Não foi possivel executar a operação (Quarto ocupado)")
            else:
                
                q1.ocupado=True
                print(f"Quarto {self.quarto} atribuído ao hóspede {self.nome}")

        elif n_quarto==102:
            if q2.ocupado==True:
                print("Não foi possivel executar a operação (Quarto ocupado)")
            else:
                
                q2.ocupado=True
                print(f"Quarto {self.quarto} atribuído ao hóspede {self.nome}")

        elif n_quarto==103:
            if q3.ocupado==True:
                print("Não foi possivel executar a operação (Quarto ocupado)")
            else:
                q3.ocupado=True
                print(f"Quarto {self.quarto} atribuído ao hóspede {self.nome}")

        elif n_quarto==104:
            if q4.ocupado==True:
                print("Não foi possivel executar a operação (Quarto ocupado)")
            else:
                q4.ocupado=True
                print(f"Quarto {self.quarto} atribuído ao hóspede {self.nome}")

        elif n_quarto==105:
            if q5.ocupado==True:
                print("Não foi possivel executar a operação (Quarto ocupado)")
            else:
                q5.ocupado=True
                print(f"Quarto {self.quarto} atribuído ao hóspede {self.nome}")

        elif n_quarto==201:
            if q6.ocupado==True:
                print("Não foi possivel executar a operação (Quarto ocupado)")
            else:
                q6.ocupado=True
                print(f"Quarto {self.quarto} atribuído ao hóspede {self.nome}")

        elif n_quarto==202:
            if q7.ocupado==True:
                print("Não foi possivel executar a operação (Quarto ocupado)")
            else:
                q7.ocupado=True
                print(f"Quarto {self.quarto} atribuído ao hóspede {self.nome}")

        elif n_quarto==203:
            if q8.ocupado==True:
                print("Não foi possivel executar a operação (Quarto ocupado)")
            else:
                q8.ocupado=True
                print(f"Quarto {self.quarto} atribuído ao hóspede {self.nome}")

        elif n_quarto==204:
            if q9.ocupado==True:
                print("Não foi possivel executar a operação (Quarto ocupado)")
            else:
                q9.ocupado=True
                print(f"Quarto {self.quarto} atribuído ao hóspede {self.nome}")

        elif n_quarto==205: 
            if q10.ocupado==True:
                print("Não foi possivel executar a operação (Quarto ocupado)")
            else:
                q10.ocupado=True
                print(f"Quarto {self.quarto} atribuído ao hóspede {self.nome}")
    
    def calcular_conta(self):
        self.n_quarto_calcular_conta=int(input("Digite o nº do quarto para calcular a conta: "))
        if self.n_quarto_calcular_conta==101:
            if q1.ocupado==False:
                print("Não foi possivel executar a operação (Quarto desocupado)")
            else:
                contaTotal=self.dias_estadia * q1._preco_diaria
                print(f"Total da conta do hóspede {self.nome} é €{contaTotal}")

        elif self.n_quarto_calcular_conta==102:
            if q2.ocupado==False:
                print("Não foi possivel executar a operação (Quarto desocupado)")
            else:
                contaTotal=self.dias_estadia * q2._preco_diaria
                print(f"Total da conta do hóspede {self.nome} é €{contaTotal}")

        elif self.n_quarto_calcular_conta==103:
            if q3.ocupado==False:
                print("Não foi possivel executar a operação (Quarto desocupado)")
            else:
                contaTotal=self.dias_estadia * q3._preco_diaria
                print(f"Total da conta do hóspede {self.nome} é €{contaTotal}")
        
        elif self.n_quarto_calcular_conta==104:
            if q4.ocupado==False:
                print("Não foi possivel executar a operação (Quarto desocupado)")
            else:
                contaTotal=self.dias_estadia * q4._preco_diaria
                print(f"Total da conta do hóspede {self.nome} é €{contaTotal}")
        
        elif self.n_quarto_calcular_conta==105:
            if q5.ocupado==False:
                print("Não foi possivel executar a operação (Quarto desocupado)")
            else:
                contaTotal=self.dias_estadia * q5._preco_diaria
                print(f"Total da conta do hóspede {self.nome} é €{contaTotal}")
        
        elif self.n_quarto_calcular_conta==201:
            if q6.ocupado==False:
                print("Não foi possivel executar a operação (Quarto desocupado)")
            else:
                contaTotal=self.dias_estadia * q6._preco_diaria
                print(f"Total da conta do hóspede {self.nome} é €{contaTotal}")
        
        elif self.n_quarto_calcular_conta==202:
            if q7.ocupado==False:
                print("Não foi possivel executar a operação (Quarto desocupado)")
            else:
                contaTotal=self.dias_estadia * q7._preco_diaria
                print(f"Total da conta do hóspede {self.nome} é €{contaTotal}")
            
        elif self.n_quarto_calcular_conta==203:
            if q8.ocupado==False:
                print("Não foi possivel executar a operação (Quarto desocupado)")
            else:
                contaTotal=self.dias_estadia * q8._preco_diaria
                print(f"Total da conta do hóspede {self.nome} é €{contaTotal}")
        
        elif self.n_quarto_calcular_conta==204:
            if q9.ocupado==False:
                print("Não foi possivel executar a operação (Quarto desocupado)")
            else:
                contaTotal=self.dias_estadia * q9._preco_diaria
                print(f"Total da conta do hóspede {self.nome} é €{contaTotal}")

        elif self.n_quarto_calcular_conta==205: 
            if q10.ocupado==False:
                print("Não foi possivel executar a operação (Quarto desocupado)")
            else:
                contaTotal=self.dias_estadia * q10._preco_diaria
                print(f"Total da conta do hóspede {self.nome} é €{contaTotal}")
       
    
    def mostrar_informacoes(self):
        print(f" - Nome do Hospede: {self.nome} Idade: {self.idade} Dias de Estadia: {self.dias_estadia} Nº Quarto: {self.quarto}")
    
    def checkout(self):
        if self.n_quarto_calcular_conta ==101:
            q1.ocupado=False
        elif self.n_quarto_calcular_conta ==102:
            q2.ocupado=False
        elif self.n_quarto_calcular_conta ==103:
            q3.ocupado=False
        elif self.n_quarto_calcular_conta ==104:
            q4.ocupado=False
        elif self.n_quarto_calcular_conta ==105:
            q5.ocupado=False
        elif self.n_quarto_calcular_conta ==201:
            q6.ocupado=False
        elif self.n_quarto_calcular_conta ==202:
            q7.ocupado=False
        elif self.n_quarto_calcular_conta ==203:
            q8.ocupado=False
        elif self.n_quarto_calcular_conta ==204:
            q9.ocupado=False
        elif self.n_quarto_calcular_conta ==205:
            q10.ocupado=False
        
        print(f"Fez {self.nome} checkout do quarto: {self.n_quarto_calcular_conta}(quarto disponivel)")

from quartos import QuartoSimples,QuartoLuxo
q1=QuartoSimples(101)
q2=QuartoSimples(102)
q3=QuartoSimples(103)
q4=QuartoSimples(104)
q5=QuartoSimples(105)

q6=QuartoLuxo(201)
q7=QuartoLuxo(202)
q8=QuartoLuxo(203)
q9=QuartoLuxo(204)
q10=QuartoLuxo(205)
