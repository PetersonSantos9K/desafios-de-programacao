frequencia = int(input("Frequencia: "))
nota = int(input("Nota: "))

if frequencia >= 75 and nota >= 60:
    if nota >= 60:
        print("Aprovado")
    else:  
        print("Reprovado por nota")
else:
    print("Reprovado por frequencia")