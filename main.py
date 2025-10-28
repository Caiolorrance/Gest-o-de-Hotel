from funcionarios import Recepcionista, Gerente
from pessoa import Hospede

lista_hospedes = []
recepcionista = Recepcionista("Claudia", 35, 1000, "12345", "manhã")


nome = str(input("Nome do hóspede: "))
idade = int(input("Idade: "))
dias_estadia = int(input("Dias de estadia: "))

hospede = Hospede(nome, idade, dias_estadia)
recepcionista.registrar_hospede(hospede)
hospede.atribuir_quarto(lista_hospedes)
while True:
    print("\n====================MENU DE NAVEGAÇÃO DO HOTEL================\n")
    print("\n1 - Registrar Hóspede\n2 - Listar Hóspedes\n3 - Checkout \n4 - Lista de Funcionarios\n5 - Sair\n")
    op = input("ESCOLHA: ")

    if op == "1":
        nome = str(input("dentro a Nome do hóspede: "))
        idade = int(input("Idade: "))
        dias_estadia = int(input("Dias de estadia: "))

        hospede = Hospede(nome, idade, dias_estadia)
        recepcionista.registrar_hospede(hospede)
        hospede.atribuir_quarto(lista_hospedes)

    elif op == "2":
        recepcionista.listar_hospedes()
        pass

    elif op == "3":
        hospede = Hospede(nome, idade, dias_estadia)
        hospede.calcular_conta()
        hospede.checkout()

    elif op == "4":
        gerente=Gerente("Carlos",45,3000)
        gerente.gerar_relatorio()
    elif op == "5":
        print("Encerrando programa...")
        break