# AULA 15 - Laço de Repetição 'for' e a Função 'range'

"""
O laço 'for' é usado para iterar sobre uma sequência (como uma string, lista, ou um objeto range).
Ele executa um bloco de código para cada item na sequência.

A função range() gera uma sequência de números.
Sintaxe: range(start, stop, step)
- start (opcional): O número inicial da sequência. O padrão é 0.
- stop (obrigatório): O número onde a sequência para. O número de 'stop' NÃO é incluído na sequência.
- step (opcional): O incremento entre cada número. O padrão é 1.
"""

# --- Exemplo 1: Iterando sobre uma String ---

texto = "Python"
print("--- Iterando sobre a string 'Python' ---")

# A cada repetição do laço, a variável 'letra' receberá um dos caracteres da string 'texto'.
for letra in texto:
    print(f"A letra agora é: {letra}")


# --- Exemplo 2: Usando a função range() ---

# range(10) gera uma sequência de 0 a 9.
print("\n--- Usando range(10) ---")
for numero in range(10):
    print(f"Número: {numero}")


# --- Exemplo 3: range() com start, stop e step ---

# range(20, 10, -1) gera uma contagem regressiva.
# Começa em 20, vai até 11 (pois o 10 não é incluído), e o passo é -1.
print("\n--- Contagem regressiva de 20 a 11 ---")
for n in range(20, 10, -1):
    print(n)


# --- Exemplo 4: 'for' com 'if' para filtrar resultados ---

# O operador de módulo (%) retorna o resto de uma divisão.
# 'n % 8 == 0' é verdadeiro se 'n' for perfeitamente divisível por 8.
print("\n--- Números divisíveis por 8 entre 0 e 99 ---")
for n in range(100):
    if n % 8 == 0:
        print(f"{n} é divisível por 8")


# --- Exemplo 5: 'for' com 'else' ---

# O bloco 'else' em um laço 'for' é executado apenas se o laço
# terminar completamente, sem ser interrompido por um 'break'.
print("\n--- Laço com else ---")
for i in range(5):
    print(f"i = {i}")
else:
    print("O laço 'for' foi concluído com sucesso!")