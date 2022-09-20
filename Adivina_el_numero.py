from logging import exception
import random

print("------------------")
print("Juega a adivina el número!!")
print("------------------")
print("Ingresa un número y suerte.")

number = 0


def nivel_dificultad():
    try:
        global number

        difficulty = int(
            input("Marca la dificultad, siendo 1 facil y 5 el nivel mas dificil: "))
        if difficulty == 1:
            number = 5
        elif difficulty == 2:
            number = 10
        elif difficulty == 3:
            number = 20
        elif difficulty == 4:
            number = 50
        elif difficulty == 5:
            number = 100
    except ValueError:
        "Introduce un numero del 1 al 5"

        # print(number)
        return number


nivel_dificultad()
# print(number)


def adivina_el_numero(x):

    num_aleatory = random.randint(1, x)

    prediction = 0

    while prediction != num_aleatory:
        prediction = int(input(f"Adivina el número entre el 1 y el {x}: "))

        if prediction < num_aleatory:
            print("Intentalo otra vez el numero tiene que ser mayor que el introducido.")
        elif prediction > num_aleatory:
            print("El numero es menor que el que marcaste.")
        else:
            print(f"Enhorabuena, {num_aleatory} es el número correcto.")


adivina_el_numero(number)
