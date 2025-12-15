"""
exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (voltar 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorno 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros  = [
    [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ],
    [ 9 , 1 , 8 , 9 , 9 , 7 , 2 , 1 , 6 , 8 ],
    [ 1 , 3 , 2 , 2 , 8 , 6 , 5 , 9 , 6 , 7 ],
    [ 3 , 8 , 2 , 8 , 6 , 7 , 7 , 3 , 1 , 9 ],
    [ 4 , 8 , 8 , 8 , 5 , 1 , 10 , 3 , 1 , 7 ],
    [ 1 , 3 , 7 , 2 , 2 , 1 , 5 , 1 , 9 , 9 ],
    [ 10 , 2 , 2 , 1 , 3 , 5 , 10 , 5 , 10 , 1 ],
    [ 1 , 6 , 1 , 5 , 1 , 1 , 1 , 4 , 7 , 3 ],
    [ 1 , 3 , 7 , 1 , 10 , 5 , 9 , 2 , 5 , 7 ],
    [ 4 , 7 , 6 , 5 , 2 , 9 , 2 , 1 , 2 , 1 ],
    [ 5 , 3 , 1 , 8 , 5 , 7 , 1 , 8 , 8 , 7 ],
    [ 10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 ],
]

def duplicado(lista_duplicado):
    # cria um set da lista para obter só os numeros unicos
    set_duplicado = set(lista_duplicado)
    # cria uma cópia da lista para poder fazer modificações
    lista_copiados = lista_duplicado.copy()
    # remove cada número unico da lista, deixando só as duplicatas
    for num_unico in set_duplicado:
        lista_copiados.remove(num_unico)
    if lista_copiados: # verifica se sobrou alguma coisa na lista
        return lista_copiados[0] # se sim, retorna a primeira cópia
    else: # se não tiver nada retorna -1
        return -1

for lista in lista_de_listas_de_inteiros:
    print(lista, duplicado(lista))