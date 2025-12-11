# AULA 13 - Manipulando Strings: Índices e Fatiamento

"""
Recursos úteis para aprofundar:
Funções built-in: https://docs.python.org/3/library/functions.html
Tipos de dados padrão: https://docs.python.org/3/library/stdtypes.html
"""

# --- Índices de String ---
# Em Python, cada caractere em uma string tem uma posição, chamada de índice.
# Os índices podem ser positivos (começando do 0, da esquerda para a direita) ou
# negativos (começando do -1, da direita para a esquerda).

#               [0] [1] [2] [3] [4] [5] [6] [7] [8]
#                P   y   t   h   o   n       s   2
# Negativos    -[9] [8] [7] [6] [5] [4] [3] [2] [1]
texto = 'Python s2'

# Acessando o caractere no índice 2 (o terceiro caractere)
print(f"Caractere no índice 2: {texto[2]}")

# Acessando o último caractere usando índice negativo
print(f"Último caractere (índice -1): {texto[-1]}")


# --- Fatiamento de Strings (Slicing) ---
# Fatiamento permite pegar um "pedaço" (substring) da string.
# A sintaxe é: string[inicio:fim:passo]
# - inicio: O índice onde a fatia começa (inclusivo).
# - fim: O índice onde a fatia termina (exclusivo - não inclui este índice).
# - passo: De quantos em quantos caracteres a fatia vai pular.

url = 'www.google.com.br/'

# Pegando a string do início (índice 0) até o índice 2 (o 3 não é incluído).
fatia1 = texto[0:3]
print(f"Fatia de 0 a 3: '{fatia1}'")

# Se o início for omitido, ele começa do índice 0.
fatia2 = texto[:6]
print(f"Fatia do início até 6: '{fatia2}'")

# Se o fim for omitido, ele vai até o final da string.
fatia3 = texto[7:]
print(f"Fatia do índice 7 até o fim: '{fatia3}'")

# Fatiando para remover o último caractere.
# Omitir o início significa "comece do início".
# O -1 no fim significa "vá até o penúltimo caractere".
fatia4 = url[:-1]
print(f"URL sem a barra final: '{fatia4}'")


# --- Fatiamento com Passo ---

# Pega a string inteira, pulando de 2 em 2 caracteres.
passo1 = texto[0:9:2]
print(f"String pulando de 2 em 2: '{passo1}'")

# Uma forma comum de inverter uma string é usar o passo -1.
string_invertida = texto[::-1]
print(f"String invertida: '{string_invertida}'")


# --- Função len() ---
# A função len() retorna o tamanho (quantidade de caracteres) de uma string.
print(f"A string 'texto' tem {len(texto)} caracteres.")