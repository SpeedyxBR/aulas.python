# AULA 23 - Funções (def) em Python

"""
Uma função é um bloco de código que só é executado quando é chamado.
Você pode passar dados, conhecidos como parâmetros, para uma função.
Uma função pode retornar dados como resultado.

A palavra-chave `def` é usada para definir uma função.
"""

# --- Definindo a Função `saudacao` ---
# Esta função aceita dois parâmetros: `msg` e `nome`.
# Ambos têm valores padrão ('Olá' e 'usuário'), que serão usados se nenhum valor for fornecido na chamada.
def saudacao(msg='Olá', nome='usuário'):
    # O método .replace() cria uma nova string, substituindo todas as ocorrências
    # de um caractere por outro.
    # Aqui, trocamos todas as letras 'e' por '3' no nome e na mensagem.
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    
    # A palavra-chave `return` envia um valor de volta para onde a função foi chamada.
    # Usamos uma f-string para combinar a mensagem e o nome modificados.
    return f'{msg} {nome}'

# --- Chamando a Função ---
# Chamamos a função `saudacao()` sem passar nenhum argumento.
# Portanto, ela usará os valores padrão para `msg` e `nome`.
# O valor retornado pela função (a string formatada) é armazenado na variável `variavel`.
variavel = saudacao()

# Imprimimos o conteúdo da variável, que é o resultado da execução da função.
print(variavel)