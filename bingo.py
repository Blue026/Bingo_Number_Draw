import random

continuar = False

# List of numbers drawn
n_sorteados = []
sorteados = set()

# Draw loop
while not continuar == "n":

    # checks whether a number has already been drawn or not
    while True:
        numero = random.randint(1, 75)
        if numero not in sorteados:
            break
        else:
            True
    sorteados.add(numero)

    # checks which column the number drawn is in and prints it
    if numero <= 15:
        print(f"B {numero}")
        numero = f"B {numero}"
    elif numero <= 30:
        print(f"I {numero}")
        numero = f"I {numero}"
    elif numero <= 45:
        print(f"N {numero}")
        numero = f"N {numero}"
    elif numero <= 60:
        print(f"G {numero}")
        numero = f"G {numero}"
    elif numero <= 75:
        print(f"O {numero}")
        numero = f"O {numero}"

    # adds the number to the list of numbers drawn
    n_sorteados.append(numero)

    # Check if you want to draw another number

    continuar = str(input("draw one more number: [y/n]   ")).lower()


# shows all numbers drawn
print(f"Numbers drawn:  {n_sorteados}")

