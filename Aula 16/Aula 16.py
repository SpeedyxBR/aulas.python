'''
For / Else em Python
'''

variavel = ['Andrel Carvalho', 'Esqueça', 'Aí Preto']

for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)
else:
    print('Não existe uma Palavra que começa com essa Letra A.')