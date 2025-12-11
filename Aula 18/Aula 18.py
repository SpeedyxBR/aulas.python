"""
Desempacotamento de Listas em Python
"""

lista = ['Andrel', 'Andrezyzz', 'Maria', 1,2,3,4,5,6,7,8,9,100]

tire1, tira2, tira3, *outra_lista, ultimo_da_lista = lista

print(tire1, tira2, tira3, outra_lista, ultimo_da_lista)
