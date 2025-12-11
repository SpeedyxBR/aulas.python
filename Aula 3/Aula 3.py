# Aula 3: Variáveis e Operadores Aritméticos

# --- Variáveis ---
# Uma variável é como uma "caixa" com um nome, onde guardamos um valor.
# Isso torna o código mais legível e fácil de modificar.

# Aqui, criamos duas variáveis: `numero1` e `numero2`.
# Usamos o sinal de igual (=) para atribuir um valor a elas.
numero1 = 10
numero2 = 3

# --- Operadores Aritméticos ---
# Agora, usamos as variáveis para fazer cálculos.

# Adição (+): Soma os valores de numero1 e numero2.
soma = numero1 + numero2

# Subtração (-): Subtrai o valor de numero2 do numero1.
subtracao = numero1 - numero2

# Multiplicação (*): Multiplica os valores das duas variáveis.
multiplicacao = numero1 * numero2

# Divisão (/): Divide numero1 por numero2. O resultado pode ser um float (com casas decimais).
divisao = numero1 / numero2

# Módulo (%): Retorna o RESTO da divisão de numero1 por numero2.
# Ex: 10 dividido por 3 é 3, com resto 1. O resultado aqui será 1.
resto = numero1 % numero2

# Potência (**): Eleva numero1 à potência de numero2 (numero1 elevado a numero2).
# Ex: 10 ** 3 é o mesmo que 10 * 10 * 10.
potencia = numero1 ** numero2

# --- Imprimindo os Resultados ---
# A função print() pode exibir múltiplos valores se você os separar por vírgula.
# Aqui, mostramos um texto (string) seguido pelo valor da variável correspondente.

print("O resultado da Soma de 10 + 3 é:", soma)
print("O resultado da Subtração de 10 - 3 é:", subtracao)
print("O resultado da Multiplicação de 10 * 3 é:", multiplicacao)
print("O resultado da Divisão de 10 / 3 é:", divisao)
print("O Resto da divisão de 10 por 3 é:", resto)
print("O resultado da Potência de 10 elevado a 3 é:", potencia)
