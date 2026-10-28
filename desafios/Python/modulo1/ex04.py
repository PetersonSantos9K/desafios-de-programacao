LIMITE_VELOCIDADE = 50
velocidadeCarro = float(input("Digite a velocidade do carro: "))

if(velocidadeCarro > LIMITE_VELOCIDADE):
    print("Multado! Você excedeu o limite de velocidade.")
else:
    print("Parabéns! Você está dentro do limite de velocidade.")
