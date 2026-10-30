import time

def finalizar_pedido(pedido, callback):
    print(f"Processamento pedido {pedido}")
    time.sleep(2)
    print(f"Pedido {pedido} finalizdo")
    callback(pedido)
def notificar_usuario(pedido):
    print(f"Seu pedido {pedido} foi concluido com sucesso!")

finalizar_pedido("123", notificar_usuario)