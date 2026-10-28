RENDA_MINIMA = 2000.00

idade = int(input("Digite a sua idade: "))
rendaMensal = float(input("Digite a sua renda mensal: "))

if idade >= 18 and rendaMensal >= RENDA_MINIMA:
    print("Você é elegível para o empréstimo.")
else:
    print("Desculpe, você não atende aos critérios para o empréstimo.")

