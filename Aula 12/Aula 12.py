# AULA 12 - Formatando valores com modificadores

"""
Guia Rápido de Modificadores de Formatação em f-strings:

:s - Formata como texto (string).
:d - Formata como um número inteiro (int).
:f - Formata como um número de ponto flutuante (float).

:.{NÚMERO}f - Define a quantidade de casas decimais para um float.
    Exemplo: {valor:.2f} exibe o valor com 2 casas decimais.

:{CARACTERE}(> ou < ou ^){QUANTIDADE}{TIPO} - Preenche uma string com um caractere específico até um certo tamanho.
    > - Alinha o texto à direita (preenche à esquerda).
    < - Alinha o texto à esquerda (preenche à direita).
    ^ - Centraliza o texto.

    Exemplo: {nome: >10} alinha a variável 'nome' à direita em um espaço de 10 caracteres.
    Exemplo: {nome:*^10} centraliza a variável 'nome' em um espaço de 10 caracteres, preenchendo com '*'.
"""

# --- Exemplo 1: Formatando Casas Decimais ---

# Definimos duas variáveis numéricas inteiras.
num_1 = 10
num_2 = 3

# Realizamos a divisão. Em Python, a divisão com uma única barra (/) sempre resulta em um float.
# 10 / 3 = 3.3333333333333335
divisao = num_1 / num_2

# Usamos uma f-string para imprimir o resultado da divisão.
# O modificador ':.2f' formata a variável 'divisao' para que exiba apenas 2 casas decimais.
# O 'f' indica que estamos formatando um número float.
print(f'Resultado da divisão com 2 casas decimais: {divisao:.2f}')


# --- Exemplo 2: Alinhamento e Preenchimento ---

nome = "Andrel"

# A variável 'nome' será impressa alinhada à direita, dentro de um espaço total de 20 caracteres.
print(f'Nome alinhado à direita: "{nome:>20}"')

# A variável 'nome' será impressa alinhada à esquerda, dentro de um espaço total de 20 caracteres.
print(f'Nome alinhado à esquerda: "{nome:<20}"')

# A variável 'nome' será impressa centralizada, dentro de um espaço total de 20 caracteres.
print(f'Nome centralizado: "{nome:^20}"')

# A variável 'nome' será impressa centralizada, e os espaços vazios serão preenchidos com o caractere '='.
print(f'Nome centralizado e preenchido: "{nome:=^20}"')


# --- Exemplo 3: Combinando formatações ---

num_3 = 1
# Adiciona zeros à esquerda até o número ter um total de 10 dígitos.
print(f'Número com zeros à esquerda: {num_3:0>10}')

num_4 = 1150.5345
# Formata o número com 1 casa decimal e o alinha à direita em um espaço de 20 caracteres.
print(f'Número formatado e alinhado: {num_4: >20.1f}')