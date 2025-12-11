# AULA 17 - Funções Úteis para Strings e Listas: split, join e enumerate

# --- 1. O Método .split() ---
# O método .split() divide uma string em uma lista de substrings.
# Por padrão, ele divide a string usando espaços em branco como separador.

string_frase = "O Python é uma linguagem de programação poderosa"
print(f"String original: '{string_frase}'")

lista_palavras = string_frase.split()
print(f"String dividida em uma lista de palavras: {lista_palavras}")

# Você também pode especificar um separador diferente.
string_csv = "maçã,banana,laranja,uva"
print(f"\nString CSV: '{string_csv}'")

lista_frutas = string_csv.split(',') # Usando a vírgula como separador
print(f"String CSV dividida em uma lista de frutas: {lista_frutas}")


# --- 2. O Método .join() ---
# O método .join() faz o oposto do split: ele une os elementos de uma lista (ou outro iterável) em uma única string.
# A string na qual o método é chamado serve como o "separador" que ficará entre os elementos.

palavras = ['Este', 'é', 'um', 'exemplo', 'de', 'join']
print(f"\nLista de palavras original: {palavras}")

frase_unida = ' '.join(palavras) # Une as palavras com um espaço entre elas
print(f"Palavras unidas com espaço: '{frase_unida}'")

frase_com_hifen = '-'.join(palavras) # Une as palavras com um hífen
print(f"Palavras unidas com hífen: '{frase_com_hifen}'")


# --- 3. A Função enumerate() ---
# A função enumerate() é usada em laços 'for' para obter tanto o índice quanto o valor de cada item em uma lista (ou outro iterável).
# Isso evita a necessidade de criar um contador manual.

lista_de_compras = ['arroz', 'feijão', 'batata']
print(f"\nIterando sobre a lista de compras com enumerate:")

for indice, item in enumerate(lista_de_compras):
    # 'indice' receberá 0, 1, 2...
    # 'item' receberá 'arroz', 'feijão', 'batata'...
    print(f"Índice: {indice}, Item: {item}")

# O enumerate também funciona com listas de listas (listas aninhadas).
lista_aninhada = [
    ['Edu', 'Luiz', 'Andrel'],  # Índice 0
    ['Maria', 'Joana', 'Clara']  # Índice 1
]
print("\nEnumerando uma lista de listas:")
for indice_externo, lista_interna in enumerate(lista_aninhada):
    print(f"Índice da lista externa: {indice_externo}")
    for indice_interno, nome in enumerate(lista_interna):
        print(f"  Índice interno: {indice_interno}, Nome: {nome}")
