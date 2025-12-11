# AULA 19 - Operador Condicional Ternário

"""
O operador condicional ternário é uma forma compacta de escrever uma estrutura if-else em uma única linha.
É muito útil para atribuir um valor a uma variável com base em uma condição.

Sintaxe:
valor_se_verdadeiro if condicao else valor_se_falso
"""

# --- Exemplo 1: Verificando a maioridade ---

idade = 20
print(f"--- Verificando se a idade é {idade} anos ---")

# A variável 'status' receberá 'Maior de idade' se a condição 'idade >= 18' for verdadeira.
# Caso contrário, receberá 'Menor de idade'.
status = 'Maior de idade' if idade >= 18 else 'Menor de idade'

print(f"Status: {status}")


# --- Exemplo 2: Verificando o status de login (corrigindo o exemplo original) ---

# Simulamos o status do login com uma variável booleana (True ou False).
usuario_logado = True
print(f"\n--- Verificando status de login (usuario_logado = {usuario_logado}) ---")

# A variável 'mensagem' recebe um valor com base no estado de 'usuario_logado'.
mensagem = 'Usuário está logado.' if usuario_logado else 'Usuário precisa fazer o login.'

print(mensagem)

# Agora, simulando com o usuário deslogado:
usuario_logado = False
print(f"\n--- Verificando status de login (usuario_logado = {usuario_logado}) ---")
mensagem = 'Usuário está logado.' if usuario_logado else 'Usuário precisa fazer o login.'
print(mensagem)


# --- Exemplo 3: Verificando se um número é par ou ímpar ---

numero = 11
print(f"\n--- Verificando se o número {numero} é par ou ímpar ---")

# Usamos o operador de módulo (%) para checar o resto da divisão por 2.
resultado = 'Par' if numero % 2 == 0 else 'Ímpar'

print(f"O número {numero} é {resultado}.")