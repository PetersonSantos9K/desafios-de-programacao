print("-" * 50)
numeros = [0,1,2,3,4,5,6,7,8,9]
print(numeros[2:7])
print(numeros[:4])
print(numeros[6:])
print(numeros[:])


print("-" * 50)
print(numeros[::2])
print(numeros[1::2])
print(numeros[2:9:3])
print(numeros[7:2:-1])

print("-" * 50)
numeros[2:5] = [20, 30, 40]
print(numeros)

del numeros[2:5]

numeros[1] = 99
print(numeros)