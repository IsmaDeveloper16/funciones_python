# CODE:35
# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios con funciones y módulos
import random

'''
Enunciado:
Crear la función "contar"
Utilizar la función "lista_aleatoria" creada antes 
para generar una lista de 5 números en
un rango de 1 a 6 inclusive

lista_numeros = lista_aleatoria(inicio, fin, cantidad)

Alumno:
- Generar una una nueva funcion que se llame "contar",
que cuente la cantidad de veces que un número (pasado
por parámetro a la función) se repite en la lista
(también pasada por parámetro)
- Primer parámetro --> número a buscar y contar
- Segundo parámetro --> la lista de números

Para saber cuantas veces se repiten el elemento pasado
en la lista pueden usar el método nativo de list "count"
'''


# --------------------------------
# Aquí copiar la función "lista_aleatoria"
# ya elaborada en el ejercicio anterior
lista = []

def lista_aleatoria(inicio,fin,cantidad):
    for i in range(cantidad):
        numero = random.randint(inicio,fin)
        lista.append(numero)
    return lista


# --------------------------------

# --------------------------------
# Aquí dentro definir la función contar

def cuenta(contar, lista):
    lista_contada = lista.count(contar)
    return lista_contada

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Utilizar la función "lista_aleatoria"
    # para que genere una lista de 5 números que esten comprendidos
    # entre los números 1 al 6 inclusive

    # lista_numeros = lista_aleatoria(...)
    lista_numeros = lista_aleatoria(0,6,5)
    
    # Imprimir en pantalla "lista_numeros" que tendrá
    print(lista_numeros)
    # los valores retornado por la función "lista_aleatoria":

    # print(lista_numeros)

    # Luego quiero averiguar cuantas veces se repite el numero 3
    # en la lista aleatoria creada
    # cantidad_tres = contar(lista_numeros, 3)
    
    cantidad_tres = cuenta(3,lista_numeros)

    # print(cantidad_tres)
    print(cantidad_tres)

    print("terminamos")
