def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = input("Digite o número para a operação correspondente: ")

        if operacao == '0':
            print("Saindo do programa...")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("Essa opção não existe.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")
            continue

        if operacao == '1':
            resultado = num1 + num2
            print(f"Resultado da Soma: {num1} + {num2} = {resultado}")
        elif operacao == '2':
            resultado = num1 - num2
            print(f"Resultado da Subtração: {num1} - {num2} = {resultado}")
        elif operacao == '3':
            resultado = num1 * num2
            print(f"Resultado da Multiplicação: {num1} * {num2} = {resultado}")
        elif operacao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado da Divisão: {num1} / {num2} = {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")


# Executando a calculadora
calculadora()
