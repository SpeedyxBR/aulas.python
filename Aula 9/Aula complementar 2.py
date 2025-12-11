'''
Operadores Lógicos - Aula 9
and, or, not
in e not in
'''

num_1 = 0
num_2 = 0

if not num_1 != num_2:
    print('Retorno 1')
else:
    print('Retorno 2') 

'''Operadores Lógicos Explicados
Os operadores lógicos trabalham com valores booleanos (True ou False) e retornam um resultado booleano, permitindo que você crie expressões condicionais complexas. 
and (E Lógico)
O operador and retorna True (Verdadeiro) somente se ambas as condições avaliadas forem verdadeiras. Se qualquer uma das condições for falsa, o resultado será False. 
Exemplo: (idade >= 18) and (possui_cnh == True) só será verdadeiro se a pessoa tiver 18 anos ou mais e possuir CNH. 
or (OU Lógico)
O operador or retorna True (Verdadeiro) se pelo menos uma das condições avaliadas for verdadeira. Ele só retorna False se ambas as condições forem falsas. 
Exemplo: (tem_desconto == True) or (cliente_vip == True) será verdadeiro se o cliente tiver desconto ou for VIP (ou ambos).
not (NÃO Lógico)
O operador not é um operador de negação unário, o que significa que ele inverte o resultado lógico da expressão que o segue. 
Exemplo: not (esta_chovendo == True) retorna True se não estiver chovendo, e False se estiver chovendo. 
not in (Não Está Em)
Embora in e not in sejam tecnicamente operadores de associação em algumas linguagens (como Python), eles são frequentemente ensinados junto com operadores lógicos, pois também retornam um valor booleano. 
O operador in verifica se um valor está presente em uma coleção (como uma lista, tupla ou string).
O operador not in verifica se um valor não está presente em uma coleção.
Exemplo: 'banana' not in lista_de_frutas retornará True se a palavra 'banana' não estiver na lista. 
Precedência
Em expressões que misturam operadores, a ordem de precedência geralmente é: not (primeiro), and (segundo) e or (por último). Recomenda-se o uso de parênteses () para garantir a ordem de avaliação desejada e tornar o código mais legível. '''