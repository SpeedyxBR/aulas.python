# Exercício - Adiando a execução de funções
def  soma ( x , y ):
    retornar  x  +  y


def  multiplica ( x , y ):
    retorna  x  *  y


def  criar_funcao ( funcao , x ):
    def  interna ( y ):
        return  função ( x , y )
    retorno  interno


soma_com_cinco  =  criar_funcao ( soma , 5 )
multiplica_por_dez  =  criar_funcao ( multiplica , 10 )

print ( soma_com_cinco ( 10 ))
print ( multiplica_por_dez ( 10 ))