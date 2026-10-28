from model.client import Client


listClient: list[Client] = []

def registerClient():
    name = input("Enter the client's name: ")
    age = int(input("Enter the client's age: "))
    listClient.append(Client(name, age))


qtdRegisterClient = int(input("How many clients do you want to register? "))

for _ in range(qtdRegisterClient):
    registerClient()

for client in listClient:
    print(f"Client = Name: {client.name}, Age: {client.age}")