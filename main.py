from funcionarios import Recepcionista
from pessoa import Hospede

while True:
    print("-------------------MENU DE NAVEGAÇÃO DO HOTEL-------------------\n")
    print("1 - Registrar Hóspede \n2 - Atribuir Quarto ao Hóspede")
    op=input("ESCOLHA: ")

    recepcionista=Recepcionista("Claudia",35,1000,"12345","manhã")
    if op=="1":      
        recepcionista.registrar_hospede()

    elif op=="2":
        hospede=Hospede("Caio",18,2,101)
        hospede.quarto=5
        print(f"Quarto Nº {hospede.quarto}")

    elif op=="3":
        pass   
   