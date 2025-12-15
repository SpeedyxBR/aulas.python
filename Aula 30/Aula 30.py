
# Manipulando chaves e valores em dicionários
pessoa  = {}

##
##

chave  =  'nome'

pessoa [ chave ] =  'Luiz Otávio'
pessoa [ 'sobrenome' ] =  'Miranda'


print ( pessoa [ chave ])

pessoa [ chave ] =  'Maria'

del  pessoa [ 'sobrenome' ]
imprimir ( pessoa )
print ( pessoa [ 'nome' ])

# print(pessoa.get('sobrenome'))
se  pessoa . get ( 'sobrenome' ) é  Nenhum :
    print ( 'NÃO EXISTE' )
senão :
    print ( pessoa [ 'sobrenome' ])

# print('ISSO Não vai')