"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando
infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
    1: Soma
    2: Subtração
    3: Multiplicação
    4: Divisão
    0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a
mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa
executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.
"""

def calculadora():
    exit = False
    resultado = 0
    operador = ""

    while exit != True:
        operacao = int(input("1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair\n"))

        if operacao == 0:
            exit = True
            return
        elif operacao > 0 and operacao <= 4:
            num1 = int(input("Digite o primeiro valor: "))
            num2 = int(input("Digite o segundo valor: "))

            if operacao == 1:
                operador = "+"
                resultado = num1 + num2
            elif operacao == 2:
                operador = "-"
                resultado = num1 - num2
            elif operacao == 3:
                operador = "*"
                resultado = num1 * num2
            elif operacao == 4:
                operador = "/"
                resultado = num1 / num2

            print(f"{num1} {operador} {num2} = {resultado}")
        else:
            print("Essa opção não existe.");

calculadora()