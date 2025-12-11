# Aula 6: Concatenação e Repetição com Strings

# --- Concatenação (+) ---
# O operador de soma (+) quando usado com strings, serve para "juntar" ou "concatenar" textos.

parte1 = "Olá"
parte2 = "Mundo"

# Juntando as duas partes. Note que não há espaço entre elas.
saudacao_sem_espaco = parte1 + parte2
print("Concatenação sem espaço:", saudacao_sem_espaco)

# Para adicionar um espaço, precisamos concatená-lo também.
saudacao_com_espaco = parte1 + " " + parte2
print("Concatenação com espaço:", saudacao_com_espaco)

# --- Repetição (*) ---
# O operador de multiplicação (*) quando usado com uma string e um número, repete a string.

texto = "Python "

# Repetindo a string `texto` 3 vezes.
texto_repetido = texto * 3
print("String repetida 3 vezes:", texto_repetido)

# Outro exemplo: criando uma linha de separação.
linha = "-" * 20  # Repete o traço 20 vezes
print(linha)

# Importante: Não é possível usar outros operadores aritméticos como -, / com strings.
# Tentar fazer `"texto" - 3` ou `"texto" / 2` resultará em um erro.
