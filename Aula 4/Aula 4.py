# Aula 4: Tipos de Dados e a Função type()

# --- Tipos de Dados Primitivos ---
# Python tem vários tipos de dados básicos para representar informações.
"""
str (string): Para representar texto. Pode usar aspas simples ou duplas.
    Ex: 'Olá', "Andrel"

int (inteiro): Para representar números inteiros, sem parte decimal.
    Ex: 123, 0, -50

float (ponto flutuante): Para representar números reais, com parte decimal.
    Ex: 10.50, -50.93, 0.0

bool (booleano): Para representar valores lógicos de Verdadeiro ou Falso.
    Ex: True, False. Comparações como 10 == 10 resultam em um booleano.
"""

# --- A Função type() ---
# A função type() nos diz qual é o tipo de um determinado dado.

# Exemplo com string (str)
print("Andrel", type("Andrel"))  # Mostra o texto e <class 'str'>

# Exemplo com inteiro (int)
print(10, type(10))  # Mostra o número e <class 'int'>

# Exemplo com ponto flutuante (float)
print(25.23, type(25.23))  # Mostra o número e <class 'float'>

# Exemplo com booleano (bool)
# A expressão 10 == 10 é avaliada primeiro, resultando em True.
print(10 == 10, type(10 == 10))  # Mostra True e <class 'bool'>

# --- Conversão de Tipos (Type Casting) ---
# Às vezes, precisamos converter um tipo de dado em outro.

# A função bool() tenta converter um valor para booleano.
# Strings não vazias são consideradas True.
print('Andrel', type('Andrel'), bool('Andrel'))

# A função int() tenta converter um valor para inteiro.
# Aqui, convertemos a string '10' para o número inteiro 10.
print('10', type('10'), type(int('10')))

# --- Exercício Prático: Cadastro Simples ---
# Usando type() para verificar os dados de um cadastro.

# Nome (string)
print('Andrel', type('Andrel'))

# Idade (inteiro)
print(20, type(20))

# Altura (float)
print(1.90, type(1.90))

# É maior de idade? (booleano)
# A expressão 20 > 18 resulta em True.
print(20 > 18, type(20 > 18))
