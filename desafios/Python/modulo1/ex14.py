number1 = int(input("Digite o primeiro numero: "))
number2 = int(input("Digite o segundo numero: "))
number3 = int(input("Digite o terceiro numero: "))

maior_numero = number1

if number2 > maior_numero: 
    maior_numero = number2

if number3 > maior_numero:
    maior_numero = number3

print("Maior numero: ", maior_numero)