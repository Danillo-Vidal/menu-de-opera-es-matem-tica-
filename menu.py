
def multiplicar():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"Resultado: {num1 * num2}")

def dividir():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Erro: Divisão por zero não é permitida.")



def menu():
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

    escolha = int(input("Escolha uma opção: "))
    
    if escolha == 1:
        somar()  
    elif escolha == 2:
        subtrair()
    elif escolha == 3:
        multiplicar()
    elif escolha == 4:
        dividir()
    elif escolha == 0:
        print("Saindo...")
    else:
        print("Opção inválida!")

# Chama a função menu para iniciar o programa
menu()
