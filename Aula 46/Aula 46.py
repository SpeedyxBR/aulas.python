# Gerator Expression, Iterables e Iterators em Python

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
lista = [n for n in range(1000)]
generator = (n for n in range(1000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))