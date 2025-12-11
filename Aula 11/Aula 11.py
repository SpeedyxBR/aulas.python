# AULA 11 - Verificando se a entrada do usuário é um número

# A função input() sempre retorna o que o usuário digita como uma string (texto).
# Aqui, pedimos ao usuário para digitar o primeiro número e o armazenamos na variável num1.
num1 = input('Digite um número: ')

# Pedimos ao usuário para digitar o segundo número e o armazenamos na variável num2.
num2 = input('Digite um número: ')

# O método .isdigit() verifica se todos os caracteres em uma string são dígitos (0-9).
# Ele retorna True (verdadeiro) se a condição for satisfeita e False (falso) caso contrário.
# Usamos 'and' para garantir que AMBAS as variáveis, num1 e num2, contenham apenas dígitos.
if num1.isdigit() and num2.isdigit():
    # Se a condição for verdadeira, convertemos as strings num1 e num2 para o tipo inteiro (int).
    # Isso é necessário para realizar cálculos matemáticos.
    num1 = int(num1)
    num2 = int(num2)

    # Agora que num1 e num2 são números, podemos somá-los e exibir o resultado.
    print(f"A soma de {num1} + {num2} é: {num1 + num2}")

# Se a condição do 'if' for falsa (ou seja, se uma ou ambas as entradas não forem compostas apenas por dígitos)...
else:
    # ...exibimos uma mensagem de erro informando ao usuário que a conversão não foi possível.
    # Isso evita que o programa quebre ao tentar somar textos.
    print('Entrada inválida. Não pude converter os números para realizar a conta.')