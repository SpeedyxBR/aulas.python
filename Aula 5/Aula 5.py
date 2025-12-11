# Aula 5: Exercício - Variáveis e Tipos de Dados

# O objetivo deste exercício é praticar a criação de variáveis
# e a atribuição de diferentes tipos de dados a elas.

# --- Instruções ---
# Crie variáveis para armazenar as seguintes informações sobre uma pessoa:
# 1. Nome (string)
# 2. Sobrenome (string)
# 3. Idade (inteiro)
# 4. Ano de Nascimento (inteiro)
# 5. É maior de idade? (booleano)
# 6. Altura em metros (float)

# --- Resolução do Exercício ---

# 1. Variável para o Nome
nome = "Andrel"

# 2. Variável para o Sobrenome
sobrenome = "Luis"

# 3. Variável para a Idade
idade = 20

# 4. Variável para o Ano de Nascimento
ano_nascimento = 2024 - idade  # Podemos calcular o ano de nascimento

# 5. Variável para verificar se é maior de idade
# Uma pessoa é maior de idade se tiver 18 anos ou mais.
# A expressão `idade >= 18` retorna True se for verdade, e False caso contrário.
maior_de_idade = idade >= 18

# 6. Variável para a Altura
altura_metros = 1.90

# --- Exibindo os Resultados ---
# Agora, vamos usar a função print() para mostrar os valores armazenados
# em cada variável, junto com o tipo de dado de cada uma.

print("Nome:", nome, type(nome))
print("Sobrenome:", sobrenome, type(sobrenome))
print("Idade:", idade, type(idade))
print("Ano de Nascimento:", ano_nascimento, type(ano_nascimento))
print("É maior de idade?", maior_de_idade, type(maior_de_idade))
print("Altura em metros:", altura_metros, type(altura_metros))
