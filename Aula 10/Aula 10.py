# Aula 10: Formatação de Números com F-Strings

# Uma das grandes vantagens das f-strings é a capacidade de formatar
# como os números (e outros valores) são exibidos.

# --- Formatando Casas Decimais ---
# Para controlar o número de casas decimais de um float, usamos `:.<N>f`,
# onde <N> é o número de casas desejado.

numero = 123.456789

# Formatando para exibir com 2 casas decimais.
# O valor será arredondado.
print(f"O número com 2 casas decimais é: {numero:.2f}")

# Formatando para exibir com 3 casas decimais.
print(f"O número com 3 casas decimais é: {numero:.3f}")

# --- Aplicando ao Exercício do IMC ---
peso = 115
altura = 1.90
imc = peso / (altura ** 2)

print(f"O IMC sem formatação é: {imc}")
print(f"O IMC formatado com 2 casas decimais é: {imc:.2f}")

# --- Outras Formatações Úteis ---

# Adicionar zeros à esquerda (útil para códigos, senhas, etc.)
# :0<N>d -> onde N é o número total de dígitos
codigo = 5
print(f"Código do produto: {codigo:04d}") # Exibirá "0005"

# Formatação de moeda (adiciona vírgulas como separador de milhar)
valor_grande = 1234567.89
print(f"O valor formatado como moeda é: {valor_grande:,.2f}") # Exibirá "1,234,567.89"
