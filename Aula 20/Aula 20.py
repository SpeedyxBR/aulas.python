
# AULA 20 - Expressões Condicionais com OR e AND (Curto-Circuito)

"""
Em Python, os operadores lógicos 'or' e 'and' têm um comportamento especial
chamado "avaliação de curto-circuito".

Isso significa que eles não necessariamente retornam True ou False. Em vez disso,
eles retornam um dos valores que estão sendo comparados.

Valores considerados "Falsy" (falsos) em Python:
- None
- False
- 0 (de qualquer tipo numérico: 0, 0.0, 0j)
- Sequências vazias (string "", lista [], tupla (), etc.)
- Mapeamentos vazios (dicionário {})

Qualquer outro valor é considerado "Truthy" (verdadeiro).
"""

# --- Como funciona o 'or' ---
# O 'or' avalia as expressões da esquerda para a direita e retorna o PRIMEIRO valor "Truthy" que encontrar.
# Se todos os valores forem "Falsy", ele retorna o ÚLTIMO valor "Falsy".

print("--- Exemplos com 'or' ---")

# 'Python' é o primeiro valor Truthy, então é retornado. O resto é ignorado.
print(f"0 or 'Python' or True: {0 or 'Python' or True}")

# Todos são Falsy, então o último (a string vazia) é retornado.
print(f"False or 0 or None or ' ': {False or 0 or None or ''}")

# Este é o caso do exemplo original da aula.
# A função input() retorna uma string. Se o usuário digitar algo, a string é Truthy.
# Se o usuário apenas pressionar Enter, a string é vazia (""), que é Falsy.

nome = input('Qual o seu nome? (Pressione Enter sem digitar nada para ver o curto-circuito): ')

# Se 'nome' for Truthy (usuário digitou algo), o valor de 'nome' é usado.
# Se 'nome' for Falsy (usuário não digitou nada), o Python continua avaliando...
# ...e retorna o primeiro valor Truthy que encontrar, que é "Você não digitou nada".
mensagem = nome or 'Você não digitou nada.'
print(mensagem)


# --- Como funciona o 'and' ---
# O 'and' também avalia da esquerda para a direita. Ele retorna o PRIMEIRO valor "Falsy" que encontrar.
# Se todos os valores forem "Truthy", ele retorna o ÚLTIMO valor "Truthy".

print("\n--- Exemplos com 'and' ---")

# 0 é o primeiro valor Falsy, então é retornado. O resto é ignorado.
print(f"'Python' and 0 and True: {'Python' and 0 and True}")

# Todos são Truthy, então o último (True) é retornado.
print(f"'Gato' and 10 and True: {'Gato' and 10 and True}")