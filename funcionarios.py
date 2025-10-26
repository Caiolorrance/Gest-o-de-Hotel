from pessoa import Pessoa
class Funcionario(Pessoa):
    Lista_funcionarios=[]
    def __init__(self, nome, idade,salario):
        super().__init__(nome, idade)
        self.salario=salario
        
       

class Gerente(Funcionario):
    def __init__(self, nome="", idade=0, salario=2100):
        super().__init__(nome, idade, salario)
    

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome} Idade: {self.idade} Salario: {self.salario} Bônus: {self.salario*0.1}")

    def gerar_relatorio(self):
        print("\n===== RELATÓRIO DE FUNCIONÁRIOS =====")
        if not Funcionario.Lista_funcionarios:
            print("Nenhum funcionário registrado.")
        else:
            total_salarios = 0
            for func in Funcionario.Lista_funcionarios:
                func.mostrar_informacoes()
                total_salarios += func.salario

            print("--------------------------------------")
            print(f"Total de funcionários: {len(Funcionario.Lista_funcionarios)}")
            print(f"Folha salarial total: R$ {total_salarios:.2f}")
            print(f"Folha com bônus do gerente: R$ {total_salarios + (self.salario * 0.1):.2f}")
        print("======================================\n")

class Recepcionista(Funcionario):
    
    lista_hospedes=[]
    def __init__(self, nome, idade, salario, id_func, turno):
        super().__init__(nome, idade, salario,)

        self.id_func=id_func
        self._turno=turno
        


    @property
    def turno(self):
        return self._turno
    
    @turno.setter
    def turno(self):
        op=input("Escolha o turno de trabalho:\n1-Manhã\n2-Tarde\n3-Noite")
        if op==1:
            self._turno="Manhâ"

        if op==2:
            self._turno="Tarde"

        else:
            self._turno="Noite"
    
    def mostrar_informacoes(self):
        print(f"ID funcionario: {self.id_func} Nome do funcionario: {self.nome} idade: {self.idade} turno:{self.turno} salario: {self.salario}")
    
    def registrar_hospede(self,hospede,lista_hospedes):

        hospede=input("Nome: ")
        lista_hospedes.append(hospede)
        
        

    def listar_hospedes(self):
        for hospede in self.lista_hospedes:
                print(f" - Hospedes registrados: {hospede.nome}, Idade: {hospede.idade}, Dias de estadia: {hospede.dias_estadia} quarto: {hospede.quarto}")

class TecnicoManutencao(Funcionario):
    def __init__(self, nome, idade, salario=1350, especialidade="indefinido"):
        super().__init__(nome, idade, salario,)

        self.especialidade=especialidade

        @property
        def especialidade(self):
            return self.especialidade
        
        def mostrar_informacoes(self):
            print(f"Nome: {self.nome} Idade: {self.idade} Salario: {self.salario} Especialidade: {self.especialidade}")



"""
• __init__(self, nome, id_fun, salario, setor, especialidade)
• registrar_hospede(nome_hospede): de Recepcionista
• registrar_reparo(descricao): de TecnicoManutencao
• mostrar_info(): sobrescrito (exibe dados de ambas as funções)
"""

class TecnicoRecepcao(Recepcionista,TecnicoManutencao):
    def __init__(self, nome="", idade=0, salario=1400, id_func="indefinido", turno="indefinido",setor="indefinido", especialidade="indefinido"):
        super().__init__(nome, idade, salario, id_func, turno,)

        self.setor=setor
        self.especialidade=especialidade

    def registrar_hospede(self):
        hospede=Recepcionista()
        hospede.registrar_hospede()
    
    def registrar_reparo(descricao):
        descricao=input("Descreva o reparo a ser realizado: ") 
        print(f"Reparo registrado: {descricao}")
        

    def mostrar_informacoes(self):
        print(f"ID funcionario: {self.id_func} Nome do funcionario: {self.nome} idade: {self.idade} turno:{self.turno} salario: {self.salario} Setor: {self.setor} Especialidade: {self.especialidade}")
        