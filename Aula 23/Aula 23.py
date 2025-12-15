"""
Funções - def em Python
"""

def saudacao(msg='0lá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = saudacao()

print(variavel)