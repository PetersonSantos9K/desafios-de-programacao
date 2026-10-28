
numero = int(input("Digite um numero: "))
soma_positivo = 0
soma_negativo = 0
while (numero !=0):
     if numero > 0:
         soma_posi1tivo += numero
     else: 
         soma_negativo += numero
     numero = int(input("Digite um numero: "))
print(f"Soma positivo {soma_positivo}")
print(f"Soma negativo: {soma_negativo}")