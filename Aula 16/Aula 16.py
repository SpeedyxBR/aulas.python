# AULA 16 - Aprofundando em Laços: 'continue' e 'for/else'

# --- A Palavra-Chave 'continue' ---
# 'continue' é usada dentro de um laço para pular o restante do código
# na iteração atual e passar imediatamente para a próxima iteração.

print("--- Exemplo com 'continue' ---")
nomes = ['Andrel', 'Maria', 'João', 'Inutil']

for nome in nomes:
    # Vamos pular a impressão do nome 'Inutil'
    if nome.lower() == 'inutil':
        print("Encontrei a palavra 'Inutil', pulando para a próxima iteração...")
        continue  # Pula para o próximo nome na lista

    # Este print só será executado se o 'continue' não for acionado.
    print(f"Olá, {nome}")


# --- A Estrutura 'for/else' ---
# O bloco 'else' em um laço 'for' é uma particularidade do Python.
# Ele é executado SOMENTE se o laço 'for' terminar todas as suas iterações
# sem ser interrompido por uma instrução 'break'.

# É muito útil para lógicas de busca: "procure por algo e, se não encontrar
# depois de verificar tudo, faça outra coisa".

print("\n--- Exemplo com 'for/else' e 'break' (Buscando um nome) ---")
lista_nomes = ['Carlos', 'Ana', 'Beatriz']
nome_buscado = 'Ana'

for nome in lista_nomes:
    print(f"Verificando: {nome}")
    if nome == nome_buscado:
        print(f"Encontrei o nome '{nome_buscado}'!")
        break  # Interrompe o laço, pois já encontramos o que queríamos.

# Como o 'break' foi executado, o bloco 'else' abaixo NÃO será executado.
else:
    print(f"O nome '{nome_buscado}' não foi encontrado na lista.")


print("\n--- Exemplo com 'for/else' (Quando o nome não é encontrado) ---")
nome_buscado_2 = 'Marcos'

for nome in lista_nomes:
    print(f"Verificando: {nome}")
    if nome == nome_buscado_2:
        print(f"Encontrei o nome '{nome_buscado_2}'!")
        break

# O laço 'for' vai terminar todas as iterações, pois 'Marcos' não está na lista.
# Como o 'break' NUNCA foi executado, o bloco 'else' será acionado.
else:
    print(f"Após verificar toda a lista, o nome '{nome_buscado_2}' não foi encontrado.")