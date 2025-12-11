# AULA 18 - Desempacotamento de Listas

"""
O desempacotamento de listas é um recurso que permite atribuir os elementos de uma lista
(ou outro iterável) a múltiplas variáveis de uma só vez.
"""

# --- Exemplo 1: Desempacotamento Simples ---
# O número de variáveis à esquerda do sinal de igualdade deve ser exatamente
# o mesmo que o número de elementos na lista.

print("--- Desempacotamento Simples ---")
lista_simples = ['Maria', 'Helena', 'Luiz']

nome1, nome2, nome3 = lista_simples

print(f"Nome 1: {nome1}")
print(f"Nome 2: {nome2}")
print(f"Nome 3: {nome3}")

# Se o número de variáveis e elementos for diferente, ocorrerá um erro (ValueError).
# Exemplo de erro: nome1, nome2 = lista_simples  # Erro! Muitos valores para desempacotar.


# --- Exemplo 2: Desempacotamento com o Operador * ---
# O operador asterisco (*) pode ser usado para capturar múltiplos elementos
# restantes em uma nova lista.

print("\n--- Desempacotamento com * ---")
lista_completa = ['Andrel', 'Andrezyzz', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

# - 'primeiro_nome' receberá o primeiro item ('Andrel').
# - 'segundo_nome' receberá o segundo item ('Andrezyzz').
# - 'ultimo_da_lista' receberá o último item (100).
# - 'outra_lista' (a variável com *) receberá TODOS os itens restantes em uma nova lista.
primeiro_nome, segundo_nome, *outra_lista, ultimo_da_lista = lista_completa

print(f"Primeiro nome: {primeiro_nome}")
print(f"Segundo nome: {segundo_nome}")
print(f"Último da lista: {ultimo_da_lista}")
print(f"O resto da lista (outra_lista): {outra_lista}")


# --- Exemplo 3: Usando * para ignorar o resto ---
# Por convenção, usamos um sublinhado (_) para uma variável que não pretendemos usar.
# *_ significa "pegue todo o resto da lista e armazene em uma variável que não vou usar".

print("\n--- Usando * para ignorar o resto ---")
lista_numeros = [10, 20, 30, 40, 50]

primeiro, segundo, *_ = lista_numeros

print(f"Pegando apenas os dois primeiros valores: {primeiro}, {segundo}")
