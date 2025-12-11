"""
Tipos de Dados
str - string 'Assim' "Assim"
int - inteiro - 12345 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False 10 == 10
"""

print("Andrel", type("Andrel"))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))

print('Andrel', type('Andrel'), bool('Andrel'))
print('10', type('10'), type(int('10')))

print('Andrel', type('Andrel'))  #Nome
print(20, type(20))  #Idade
print(1.90, type(1.90))  #Altura
print(10 == 20, type(10 == 20))

"""
O que a função type() faz?

Em poucas palavras, a função type() retorna o tipo de um objeto.

Tudo em Python é um "objeto", e cada objeto tem um tipo específico.
Quando você usa type(), você está perguntando ao Python: "Qual é o tipo deste dado?".

Exemplos:
- type('Olá') -> <class 'str'>
- type(123)   -> <class 'int'>
- type(1.5)   -> <class 'float'>
- type(True)  -> <class 'bool'>

Por que isso é importante?

Saber o tipo de um dado é crucial porque diferentes tipos se comportam de maneiras diferentes.
Por exemplo, você pode somar dois números (10 + 5), mas tentar somar um texto e um número ('Olá' + 5) causará um erro.

A função `type()` é uma das primeiras ferramentas que você usa para depurar (encontrar e corrigir erros) seu código,
pois ajuda a garantir que suas variáveis contenham o tipo de dado que você espera.
"""