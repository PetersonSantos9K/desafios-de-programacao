
def saudacao(nome):
    print(f"Olá, {nome}")

def processar_usuario(callback):
    usuario = "Alise"
    callback(usuario)
processar_usuario(saudacao)