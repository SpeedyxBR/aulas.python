# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    print('Abrindo arquivo')
    arquivo = open(caminho_arquivo, modo, encoding='utf8')
    yield arquivo
    print('Fechando Arquivo')
    arquivo.close()


with my_open('aula85,txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n')
    print('WITH', arquivo)