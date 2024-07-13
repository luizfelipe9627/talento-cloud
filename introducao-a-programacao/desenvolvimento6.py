"""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual
(2024).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará
perguntando até que um valor correto seja preenchido.
"""

def calcular_idade():
    valido = False

    while valido == False:
        try:
            nome = input('Digite o seu nome completo: ')
            ano_nascimento = int(input('Digite o ano de nascimento: '))
            idade = 2024 - ano_nascimento

            if ano_nascimento > 1922 and ano_nascimento < 2021:
                print(f"Em 2024 você terá {idade} anos.")
                valido = True
            else:
                print("Você digitou um ano de nascimento inválida, tente novamente.")
                valido = False
        except:
            print("Tipo de dado inválido, tente novamente.")

calcular_idade()