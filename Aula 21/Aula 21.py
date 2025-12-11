# AULA 21 - Revisão: Combinando for, range e enumerate

"""
Nesta aula, vamos revisar e combinar três conceitos importantes que já vimos:
1. O laço 'for': Para iterar sobre uma sequência.
2. A função 'range()': Para gerar uma sequência de números.
3. A função 'enumerate()': Para obter o índice e o valor de um item em uma sequência.

Vamos criar uma contagem regressiva e, ao mesmo tempo, mostrar o número da iteração.
"""

# --- Passo 1: Criando a sequência da contagem regressiva ---

# Usamos a função range() para criar uma sequência de números.
# - Começa em 10 (start=10).
# - Para ANTES de chegar no 1 (stop=1).
# - Diminui de 1 em 1 a cada passo (step=-1).
# Portanto, 'contador' representa a sequência: 10, 9, 8, 7, 6, 5, 4, 3, 2.
contador = range(10, 1, -1)

# --- Passo 2: Iterando com for e enumerate ---

print("Índice | Contagem Regressiva")
print("-------------------------")

# Usamos 'enumerate()' para obter um índice para cada item da nossa sequência 'contador'.
# O laço 'for' desempacota o resultado do enumerate em duas variáveis a cada iteração:
# - 'indice': Receberá o índice da iteração, começando em 0.
# - 'cont': Receberá o valor da nossa contagem regressiva (10, 9, 8, ...).
for indice, cont in enumerate(contador):
    # Imprimimos o índice da iteração e o número correspondente da contagem regressiva.
    # O resultado mostrará o índice (0 a 8) ao lado da contagem (10 a 2).
    print(f"   {indice}   |         {cont}")

print("\nFim da contagem!")