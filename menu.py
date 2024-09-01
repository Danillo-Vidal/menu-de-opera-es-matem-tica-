def menu():
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

    escolha = int(input("Escolha uma opção: "))
    
    if escolha == 1:
        print("Função somar ainda não implementada.")
    elif escolha == 2:
        print("Função subtrair ainda não implementada.")
    elif escolha == 3:
        print("Função multiplicar ainda não implementada.")
    elif escolha == 4:
        print("Função dividir ainda não implementada.")
    elif escolha == 0:
        print("Saindo...")
    else:
        print("Opção inválida!")
