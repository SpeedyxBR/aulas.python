# Empacotamento e desempacotamento de dicionários
a , b  =  1 , 2
a , b  =  b , a
print(a, b)


# (a1, a2), (b1, b2) = pessoa.itens()
# print(a1, a2)
# print(b1, b2)

# para chave, valor em pessoa.items():
# print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa  = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa }
# print(pessoas_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.item():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
#args e kwargs
# args (já vimos)
# kwargs - argumentos de palavra-chave (argumentos nomeados)




# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

