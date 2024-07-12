"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o
terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""

def calculadora(num1, num2, operador):
    if operador == "+":
        return print(f"{num1} + {num2} = {num1 + num2}")
    elif operador == "-":
        return print(f"{num1} - {num2} = {num1 - num2}")
    elif operador == "*":
        return print(f"{num1} * {num2} = {num1 * num2}")
    elif operador == "/":
        return print(f"{num1} / {num2} = {num1 / num2}")
    else:
        return print("0")

calculadora(2, 4, "*")
