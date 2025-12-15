# Introdução à compreensão de lista em Python
# Lista de compreensão é uma forma rápida para criar listas
# a partir de iteráveis.
# print(lista(intervalo(10)))

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista  = [
    numero * 2
    for numero in range(10)
]
print(lista)