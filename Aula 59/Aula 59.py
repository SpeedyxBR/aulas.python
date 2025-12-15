# Problema dos parâmetros mutáveis ​​em funções Python
def  adiciona_clientes ( nome , lista = Nenhum ):
    se  a lista  for  Nenhuma :
        lista  = []
    lista . anexar ( nome )
    retornar  lista


cliente1  =  adiciona_clientes ( 'luiz' )
adiciona_clientes ( 'Joana' , cliente1 )
adiciona_clientes ( 'Fernando' , cliente1 )
cliente1 . anexar ( 'Edu' )

cliente2  =  adiciona_clientes ( 'Helena' )
adiciona_clientes ( 'Maria' , cliente2 )

cliente3  =  adiciona_clientes ( 'Moreira' )
adiciona_clientes ( 'Vivi' , cliente3 )

imprimir ( cliente1 )
imprimir ( cliente2 )
imprimir ( cliente3 )