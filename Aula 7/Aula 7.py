# Aula 7: Precedência de Operadores Aritméticos

# Quando temos múltiplos operadores em uma mesma expressão, o Python segue uma ordem de prioridade
# para resolver a conta, conhecida como "precedência".

# A ordem de precedência é a seguinte (do mais importante para o menos importante):
# 1. Parênteses: ( )
# 2. Potenciação: **
# 3. Multiplicação, Divisão, Divisão Inteira e Módulo: *, /, //, %
# 4. Soma e Subtração: +, -

# --- Exemplo 1: Sem parênteses ---
# Nesta expressão, a multiplicação (2 * 3) será resolvida PRIMEIRO.
# 1 + 2 * 3  ->  1 + 6  ->  7
resultado1 = 1 + 2 * 3
print("Resultado de 1 + 2 * 3 é:", resultado1)

# --- Exemplo 2: Com parênteses ---
# Os parênteses forçam a expressão dentro deles a ser resolvida primeiro.
# (1 + 2) * 3  ->  3 * 3  ->  9
resultado2 = (1 + 2) * 3
print("Resultado de (1 + 2) * 3 é:", resultado2)

# --- Exemplo 3: Expressão mais complexa ---
# 1. Potenciação: 2 ** 3 = 8
# 2. Multiplicação: 5 * 2 = 10
# 3. Soma e Subtração (da esquerda para a direita): 10 + 8 - 10 = 8
resultado3 = 10 + 2 ** 3 - 5 * 2
print("Resultado de 10 + 2 ** 3 - 5 * 2 é:", resultado3)

# --- Exemplo 4: Usando parênteses para clareza ---
# Mesmo que a precedência já fizesse a multiplicação primeiro, usar parênteses
# pode deixar a intenção do código mais clara para quem está lendo.
resultado4 = 10 + (5 * 2)
print("Resultado de 10 + (5 * 2) é:", resultado4)
