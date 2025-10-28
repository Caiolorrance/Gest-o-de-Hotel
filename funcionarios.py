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
        lista_funcionarios = []
        lista_funcionarios.append(gerente)
        lista_funcionarios.append(recepcionista)
        lista_funcionarios.append(tecnico)
        lista_funcionarios.append(tecnico_recepcao)

        for funcionario in lista_funcionarios:
            funcionario.mostrar_informacoes()

class Recepcionista(Funcionario):
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
        print(f"Profissisão: Recepcionista, ID funcionario: {self.id_func}, Nome do funcionario: {self.nome}, idade: {self.idade}, turno:{self.turno}, salario: {self.salario}")
    
    lista_hospedes=[]
    def registrar_hospede(self, hospede):
        
        self.lista_hospedes.append(hospede)
        print(f"Hóspede {hospede.nome} registrado com sucesso.")
        
    def listar_hospedes(self):
        print("\n--- LISTA DE HÓSPEDES ---")
        if not self.lista_hospedes:
            print("Nenhum hóspede cadastrado.")
        for hospede in self.lista_hospedes:
            hospede.mostrar_informacoes()
            
class TecnicoManutencao(Funcionario):
    def __init__(self, nome, idade, salario=1350, especialidade="indefinido"):
        super().__init__(nome, idade, salario)
        self._especialidade = especialidade  # usamos _ para a propriedade

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, valor):
        self._especialidade = valor

    def mostrar_informacoes(self):
        print(f"Profissisão: Tecnico de Manutenção, Nome: {self.nome},  Idade: {self.idade}, Salário: {self.salario}, Especialidade: {self.especialidade}")

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
        print(f"Profissisão: Tecnico de Recepção, ID funcionario: {self.id_func}, Nome do funcionario: {self.nome}, idade: {self.idade}, turno:{self.turno}, salario: {self.salario}, Setor: {self.setor}, Especialidade: {self.especialidade}")
        
gerente=Gerente("Carlos",45,3000)
recepcionista = Recepcionista("Claudia", 35, 1000, "12345", "manhã")
tecnico = TecnicoManutencao("João", 40, 1350, "Elétrica")
tecnico_recepcao = TecnicoRecepcao("Ana", 30, 1400, "67890", "Tarde", "Recepção", "Hidráulica")



