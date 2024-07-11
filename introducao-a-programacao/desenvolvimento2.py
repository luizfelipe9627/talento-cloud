"""
Desenvolva um algoritmo que utilize as seguintes características de um veículo:
    Quantidade de rodas;
    Peso bruto em quilogramas;
    Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a
partir das condições:
    A: Veículos com duas ou três rodas;
    B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
    C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
    D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
    E: Veículos com quatro rodas ou mais e com mais de 6000 kg
"""

qntRodas = int(input("Digite a quantidade de rodas do veículo: "))
pesoQuilogramas = int(input("Digite o peso bruto em quilogramas do veículo: "))
qntPessoas = int(input("Digite a quantidade de pessoas no veículo: "))

if qntRodas == 2 or qntRodas == 3:
    print("Categoria Recomendada: A")
elif qntRodas == 4 and qntPessoas <= 8 and pesoQuilogramas <= 3500:
    print("Categoria Recomendada: B")
elif qntRodas >= 4:
    if qntPessoas > 8:
        print("Categoria Recomendada: D")
    elif pesoQuilogramas > 6000:
        print("Categoria Recomendada: E")
    elif pesoQuilogramas > 3500 and pesoQuilogramas <= 6000:
        print("Categoria Recomendada: C")
    else:
        print("Categoria Recomendada: B")
