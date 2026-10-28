   


def calcula_media(notas):
        media = 0
        for i in range(len(notas)):
            media += notas[i]
            
        return media / len(notas)

def verificar_aprovacao(media, media_aprovacao=7.0):
        return "Aprovado" if media >= media_aprovacao else "Reprovado"

def exibir_resultado(nome, media, resultado):
        print(f"Aluno: {nome}")
        print(f"Media: {media:.2f}")
        print(f"Resultado: {resultado}")

nome = "joao"
notas = [8.0, 7.5, 6.0]
media = calcula_media(notas)
resultado = verificar_aprovacao(media)
exibir_resultado(nome, media, resultado)
    
