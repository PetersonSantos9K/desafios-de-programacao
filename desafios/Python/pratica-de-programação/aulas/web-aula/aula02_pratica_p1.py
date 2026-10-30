notas = [7.5, 6.0, 9.0, 8.5, 5.5, 10.0, 4.0, 8.0]

print(f"3 primeiras notas: {notas[:3]}")
print(f"2 Ultimas notas: {notas[len(notas) - 2:]}")
print(f"Lista de notas invertida: {notas[::-1]}")
print(f"Imprimir uma nota sim e outra não: {notas[::2]}")

notas[2:5] = [9.9, 9.9, 9.9]
print(f"Notas dos indices de 2 a 4 trocados: {notas}")


print(notas[::-2])