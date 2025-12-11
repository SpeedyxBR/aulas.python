"""
Formatando Valoresd com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO) f - Quantidade de Casas decimais (float)
: (Caractere) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print( f'{divisao:.2f}' )