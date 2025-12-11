num1 = input('Digite um número: ')
num2 = input('Digite um número: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pude converter os números para realizar contas')
    
    '''A função isdigit() em Python é um método de strings que retorna True se todos os caracteres da string forem dígitos (0-9, incluindo alguns dígitos especiais como sobrescritos) e False caso contrário, sendo muito útil para validar entradas do usuário, pois retorna False para espaços, pontos ou letras, mesmo em strings que parecem números como "123.45" ou " -10 ". 
Como funciona
Sintaxe: string.isdigit()
Retorno: True (se todos forem dígitos), False (se houver qualquer caractere não-dígito ou se a string estiver vazia). 
O que considera dígito: Caracteres numéricos como '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', e também dígitos sobrescritos (¹, ²), mas não sinais como '-' ou '.'. '''