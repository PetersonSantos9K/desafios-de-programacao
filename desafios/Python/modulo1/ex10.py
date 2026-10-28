number = int(input("Enter a number: "))
soma = 0

while number >= 0:
    soma += number
    number = int(input("Enter a number: "))

print("The sum of the numbers is:", soma)