print('Bem vindo ao validador de cpf')
print('lembrando que deve conter 11 digitos e sem (.) ou (-)')
cpf = input('Digite o cpf que deseja validar: ')

while len(cpf) < 11 or len(cpf) > 11:
    cpf = input('Digite o cpf que deseja validar: ')

cpf_lista = list(cpf)
valores = [int(val) for val in cpf_lista]
digito_1 = int
digito_2 = int
resultado = int
acumulo = 0
resultado_2 = int
acumulo_2 = 0

# print(cpf)
# parte 1

for n, y in enumerate(range(10, 1, -1)):
    resultado = valores[n] * y
    acumulo = acumulo + resultado

parte_2 = 11 - (acumulo % 11)

for n, y in enumerate(range(11, 1, -1)):
    resultado_2 = valores[n] * y
    acumulo_2 = acumulo_2 + resultado_2

del valores[10]
del valores[9]

parte_3 = 11 - (acumulo_2 % 11)

digito_2 = parte_3
digito_1 = parte_2

if parte_2 > 9:
    digito_1 = 0

if parte_3 > 9:
    digito_2 = 0

valores.insert(9, digito_1)
valores.insert(10, digito_2)

valores = str = ''.join(str(e) for e in valores)

cpf = int(cpf)

novo_cpf = int(valores)

print(novo_cpf)
print(cpf)

if cpf == 11 * '9' or cpf == 11 * '8' or cpf == 11 * '7' or cpf == 11 * '6' or cpf == 11 * '5' or cpf == 11 * '4' or cpf == 11 * '3' or cpf == 11 * '2' or cpf == 11 * '1' or cpf == 11 * '0':
    print('cpf invalido')
    while True:
        break

if cpf == novo_cpf:
    print('Cpf valido')
elif cpf != novo_cpf:
    print('Cpf invalido')