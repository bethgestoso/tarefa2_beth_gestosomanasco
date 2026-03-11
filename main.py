from faker import Faker
import random

fake = Faker("es_ES")

# Tarefa para a UD2.
# Faker é un paquete que se usa para xerar datos ficticios de usuarios e así poder
# facer probas nas nosas aplicacións.

# Nesta tarefa debes empregar Faker para desenvolver un programa que cree os datos
# ficticios de 15 usuarios. Os datos deben almacenarse nun dicionario, de forma que:

# Os usuarios estean identificados por un código comprendido entre o número 1 e o 15.
# Non poderá haber dous usuarios co mesmo código.
# Para cada usuario se almacenen os seguintes datos:
# nome, dirección, correo electrónico, teléfono.
dic_usuarios = {}
for i in range(1, 16):
    dic_usuarios[i] = {
        "nome": fake.name(),
        "dirección": fake.address(),
        "correo electrónico": fake.email(),
        "teléfono": fake.phone_number(),
    }


# O programa debe mostrar por pantalla os datos de todos os usuarios creados.
print(f"Os usuarios creados son: {dic_usuarios}")

# Despois, o programa seleccionará aleatoriamente a un dos usuarios para mostrar a
# seguinte mensaxe: "O usuario chamado NOME foi o afortunado!"
claves = list(dic_usuarios.keys())
afortunado = dic_usuarios[random.choice(claves)]["nome"]
print(f"O usuario chamado {afortunado} foi o afortunado!")
