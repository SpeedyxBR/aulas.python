# AULA 14 - Laço de Repetição 'while' (Enquanto)

"""
O laço 'while' é usado para executar um bloco de código repetidamente,
enquanto uma determinada condição for verdadeira.

Estrutura:
while condicao:
    # código a ser executado
    # É crucial que algo dentro do laço mude a 'condicao',
    # para que em algum momento ela se torne falsa e o laço termine.
"""

# --- Exemplo 1: Contagem Simples ---

# Inicializamos uma variável de controle, chamada 'x'.
# Ela servirá para contar as repetições do laço.
x = 0

# A condição do while é 'x < 10'.
# O código dentro do laço será executado enquanto o valor de 'x' for menor que 10.
print("--- Iniciando Contagem Simples de 0 a 9 ---")
while x < 10:
    # Imprime o valor atual do contador.
    print(f"O valor de x é: {x}")

    # Incrementamos o contador em 1 a cada repetição.
    # Esta linha é ESSENCIAL. Sem ela, 'x' seria sempre 0,
    # a condição 'x < 10' seria sempre verdadeira, e teríamos um laço infinito!
    x = x + 1

# Esta linha só é executada quando o laço termina, ou seja,
# quando 'x' chega a 10 e a condição '10 < 10' se torna falsa.
print("Laço 'while' finalizado!")


# --- Exemplo 2: 'while' com a palavra-chave 'break' ---

# A palavra-chave 'break' interrompe o laço imediatamente,
# mesmo que a condição do 'while' ainda seja verdadeira.

y = 0
print("\n--- Iniciando Laço com Break --- ")
while y < 100: # A condição permite ir até 99
    print(f"Executando o laço, y = {y}")

    # Criamos uma condição para parar o laço antes do previsto.
    if y == 5:
        print("Condição de parada atingida! Usando 'break'...")
        break  # Interrompe o laço agora.

    y += 1 # Forma abreviada de 'y = y + 1'

print(f"Laço com break finalizado. O valor final de y foi: {y}")