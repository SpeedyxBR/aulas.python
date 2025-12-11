# Aula 8: Exercício - Cálculo do IMC (Índice de Massa Corporal)

# O IMC é um cálculo que avalia se a pessoa está com o peso ideal.
# A fórmula é: IMC = Peso / (Altura * Altura)

# --- Coleta de Dados ---
# Vamos criar variáveis para armazenar o nome, peso e altura de uma pessoa.

nome = 'Andrel Luis'
peso = 115  # em quilogramas
altura = 1.90  # em metros

# --- Cálculo do IMC ---
# Para calcular a altura ao quadrado, podemos usar `altura * altura` ou o operador de potência `altura ** 2`.
# Usaremos parênteses na parte da altura para garantir a ordem correta do cálculo, embora não seja estritamente
# necessário aqui devido à precedência de operadores (potência vem antes da divisão).

imc = peso / (altura ** 2)

# --- Exibindo o Resultado ---
# Agora, vamos mostrar o resultado de forma clara para o usuário.

print("--- Calculadora de IMC ---")
print("Nome:", nome)
print("Peso:", peso, "kg")
print("Altura:", altura, "m")
print("Seu IMC é:", imc)

# O resultado do IMC pode ter muitas casas decimais. Em aulas futuras,
# aprenderemos a formatar este número para que ele fique mais legível (ex: 25.19).
