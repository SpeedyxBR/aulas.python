# -*- coding: utf-8 -*-

"""
ATIVIDADE COMPLETA: Calculadora de Orçamento Pessoal

Bem-vindo, aluno! Esta atividade foi projetada para revisar e aplicar
todos os conceitos que aprendemos das Aulas 1 a 23. Você criará uma
ferramenta de linha de comando para gerenciar um orçamento pessoal.

OBJETIVO:
Construir um script que:
1.  Solicita ao usuário seu nome e renda mensal.
2.  Permite que o usuário insira várias despesas (nome e valor).
3.  Calcula o total de despesas.
4.  Calcula o saldo final (Renda - Total de Despesas).
5.  Exibe um relatório detalhado e formatado.

CONCEITOS APLICADOS:
- Variáveis e Tipos de Dados (str, int, float, list)
- Entrada do Usuário (input)
- Laços de Repetição (while)
- Condicionais (if, else)
- Funções (def, return, parâmetros)
- Manipulação de Strings (f-strings, .replace)
- Manipulação de Listas (append)
- Operadores Aritméticos (+, -, *)
- Validação de Dados (.isdigit)
"""

# --- FUNÇÃO 1: Coletar Despesas ---
# Esta função será responsável por perguntar ao usuário sobre suas despesas
# e retornará uma lista com todas elas.
def coletar_despesas():
    """
    Usa um laço 'while' para pedir ao usuário o nome e o valor de cada despesa.
    Armazena cada despesa como uma tupla (nome, valor) dentro de uma lista.
    O laço termina quando o usuário digita 'sair'.
    Retorna a lista de despesas.
    """
    despesas = []  # Inicializa uma lista vazia para guardar as despesas
    while True:
        nome_despesa = input("Digite o nome da despesa (ou 'sair' para terminar): ")

        # Condição de parada do laço
        if nome_despesa.lower() == 'sair':
            break

        valor_despesa_str = input(f"Digite o valor da despesa '{nome_despesa}': ")

        # Validação da entrada do valor
        # DICA: Precisamos garantir que o valor seja um número válido.
        # O método .replace() ajuda a aceitar tanto '10.50' quanto '10,50'.
        if valor_despesa_str.replace('.', '', 1).replace(',', '', 1).isdigit():
            valor_despesa = float(valor_despesa_str.replace(',', '.'))
            despesas.append((nome_despesa, valor_despesa))  # Adiciona a tupla à lista
        else:
            print("Valor inválido. Por favor, insira um número.")

    return despesas

# --- FUNÇÃO 2: Calcular Totais e Saldo ---
# Esta função recebe a renda e a lista de despesas e faz os cálculos.
def calcular_saldo(renda, despesas):
    """
    Calcula o total das despesas e o saldo final.
    Retorna dois valores: o total de despesas e o saldo.
    """
    total_despesas = 0
    # DICA: Um laço 'for' é perfeito para percorrer a lista de despesas.
    for despesa in despesas:
        # despesa é uma tupla, ex: ('Aluguel', 1500.0). O valor está no índice 1.
        total_despesas += despesa[1]

    saldo = renda - total_despesas
    return total_despesas, saldo

# --- FUNÇÃO 3: Gerar o Relatório ---
# Esta função cria o texto final que será exibido para o usuário.
def gerar_relatorio(nome_usuario, renda, despesas, total_despesas, saldo):
    """
    Formata e exibe um relatório financeiro completo e legível.
    Usa f-strings para formatar os números e apresentar os resultados.
    """
    print("\n" + "="*40)
    print(f"      RELATÓRIO FINANCEIRO DE {nome_usuario.upper()}      ")
    print("="*40)
    print(f"Renda Mensal: R$ {renda:,.2f}")
    print("-"*40)

    print("Despesas Detalhadas:")
    if not despesas:
        print("Nenhuma despesa registrada.")
    else:
        for nome, valor in despesas:
            # DICA: F-strings com alinhamento deixam o relatório mais bonito.
            print(f"- {nome:<20}: R$ {valor:>10,.2f}")

    print("-"*40)
    print(f"Total de Despesas: R$ {total_despesas:,.2f}")
    print(f"Saldo Final: R$ {saldo:,.2f}")
    print("="*40)

    # DICA: Use 'if/elif/else' para dar um feedback sobre o saldo.
    if saldo > 0:
        print("Parabéns! Seu orçamento está positivo. Você economizou dinheiro este mês!")
    elif saldo == 0:
        print("Atenção! Você gastou exatamente o que ganhou.")
    else:
        print("Cuidado! Seu orçamento está negativo. É hora de rever os gastos.")
    print("="*40)


# --- PROGRAMA PRINCIPAL ---
# Esta é a parte do código que orquestra a execução das funções.
def main():
    """
    Função principal que executa o programa.
    """
    print("--- Calculadora de Orçamento Pessoal ---")
    nome_usuario = input("Qual é o seu nome? ")
    
    renda_mensal_str = input("Qual é a sua renda mensal? R$ ")
    # Validação da renda
    if renda_mensal_str.replace('.', '', 1).replace(',', '', 1).isdigit():
        renda_mensal = float(renda_mensal_str.replace(',', '.'))
    else:
        print("Renda inválida. Encerrando o programa.")
        return # Encerra a função main se a renda for inválida

    # 1. Chamar a função para coletar as despesas
    lista_de_despesas = coletar_despesas()

    # 2. Chamar a função para realizar os cálculos
    total_gasto, saldo_final = calcular_saldo(renda_mensal, lista_de_despesas)

    # 3. Chamar a função para exibir o relatório final
    gerar_relatorio(nome_usuario, renda_mensal, lista_de_despesas, total_gasto, saldo_final)

# Executa o programa principal
# A linha abaixo garante que a função main() só será executada quando
# este arquivo for rodado diretamente.
if __name__ == "__main__":
    main()

"""
### DICAS =O ###

1.  **Entendendo o Fluxo:**
    - O programa começa na função `main()`.
    - `main()` chama `coletar_despesas()` para obter a lista de gastos.
    - Depois, `main()` chama `calcular_saldo()` para processar os números.
    - Finalmente, `main()` chama `gerar_relatorio()` para mostrar tudo na tela.

2.  **Validação de Números:**
    - A linha `valor.replace('.', '', 1).replace(',', '', 1).isdigit()` é um truque.
    - Ela remove temporariamente um ponto ou uma vírgula para que `.isdigit()` funcione
      corretamente com números decimais digitados como string.

3.  **Tuplas `(nome, valor)`:**
    - Usamos tuplas para garantir que cada despesa sempre tenha um nome e um valor juntos,
      e que eles não sejam alterados por acidente.

4.  **`if __name__ == "__main__":`**
    - Esta é uma convenção em Python. Ela permite que você importe funções deste arquivo
      para outros scripts sem que o código principal (a chamada para `main()`) seja
      executado automaticamente. É uma boa prática de organização.

5.  **Desafio Extra:**
    - Tente modificar a função `gerar_relatorio` para também calcular e mostrar
      a porcentagem que cada despesa representa do total da renda.
      Fórmula: `(valor_despesa / renda_mensal) * 100`
"""
