# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# sistema de importação

# plataforma = 'A MINHA'
# print(sys.platform)
# print(plataforma)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform

# print(plataforma)

# alias 1 - importa nome_modulo como apelido
# importa sistema como s

# sys = 'alguma coisa'
# print(s.platform)
# print(sys)


# alias 2 - de nome_modulo importa objeto como apelido
# from sys import exit as ex
# da plataforma de importação sys como pf

# imprimir(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import exit, platform

# print(plataforma)
# saída()