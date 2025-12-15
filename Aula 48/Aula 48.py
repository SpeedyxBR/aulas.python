# Rendimento de
def  gen1 ():
    print ( 'COMECOU GEN1' )
    yield 1
    rendimento  2
    rendimento  3
    print ( 'ACABOU GEN1' )


def  gen3 ():
    print ( 'COMECOU GEN3' )
    rendimento  10
    rendimento  20
    rendimento  30
    print ( 'ACABOU GEN3' )


def  gen2 ( gen = Nenhum ):
    print ( 'COMECOU GEN2' )
    se  gen  não for  Nenhum :
        rendimento  da  geração
    rendimento  4
    rendimento  5
    rendimento  6
    print ( 'ACABOU GEN2' )


g1  =  gen2 ( gen1 ())
g2  =  gen2 ( gen3 ())
g3  =  gen2 ()
para  numero  em  g1 :
    imprimir ( número )
imprimir ()
para  numero  em  g2 :
    imprimir ( número )
imprimir ()
para  numero  em  g3 :
    imprimir ( número )
imprimir ()