# Aula 9: Introdução à Formatação de Strings com F-Strings

# F-Strings (ou strings formatadas) são uma maneira moderna e muito legível
# de incluir o valor de variáveis diretamente dentro de uma string.

# --- Como usar F-Strings ---
# Para criar uma f-string, basta colocar a letra `f` antes das aspas de abertura da string.
# Dentro da string, você pode colocar variáveis ou expressões dentro de chaves `{}`.

# --- Exemplo Básico ---
nome = "Andrel"
idade = 20

# Criando uma frase usando f-string
frase = f"Olá, meu nome é {nome} e eu tenho {idade} anos."
print(frase)

# --- Exemplo com Cálculos ---
# Você pode colocar expressões e cálculos diretamente dentro das chaves.

salario = 5000
impostos = 0.275 # 27.5%

salario_liquido = salario * (1 - impostos)

print(f"O salário bruto é R${salario}, e o salário líquido é R${salario_liquido}.")

# --- Exemplo com o IMC da aula anterior ---
peso = 115
altura = 1.90
imc = peso / (altura ** 2)

# Note que o IMC tem muitas casas decimais. Vamos resolver isso na próxima aula.
print(f"Com peso {peso}kg e altura {altura}m, o IMC resultante é {imc}.")
