nota = float(input("Digite a nota do aluno: "))

if nota < 0.0 or nota > 10.0:
    print("Nota inválida. A nota deve estar entre 0.0 e 10.0.")

if nota < 5.0:
    print("Desempenho Insuficiente")
elif nota < 7.0:
    print("Desempenho Regular")
elif nota < 9.0:
    print("Desempenho Bom")
else:
    print("Desempenho Excelente")