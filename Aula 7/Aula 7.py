'''
iniciar com letra, pode conter números, separar_, letras minúsculas
'''

nome = 'Andrel'
idade = 20  #int
altura = 1.90  # float
e_maior = idade > 18  # bool
data_1 = True
data_atual = 2022
peso = 115
imc = peso / (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print(idade * altura)
print(nome, 'Tem', idade,'Anos de Idade', altura, e_maior, peso, imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))