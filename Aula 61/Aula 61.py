import random

def aposta_robo(saldo, aposta):
    resultado = random.randint(0, 36) # gerando um número aleatório de 0 a 36

    # Verificando o resultado da aposta
    if resultado == aposta:
        saldo += 36 * aposta # ganhando 36 vezes o valor da aposta
        print("Parabéns! Você acertou o número e ganhou 36 vezes sua aposta.")
    else:
        saldo -= aposta # perdendo o valor da aposta
        print("Infelizmente você não acertou o número desta vez.")

    return saldo

# Iniciando o saldo do robô
saldo = 100

# Executando o robô de apostas
while saldo > 0:
    print("Seu saldo atual é de:", saldo)
    aposta = int(input("Quantos você gostaria de apostar? "))
    saldo = aposta_robo(saldo, aposta)

print("O robô de apostas agora está sem saldo.")


