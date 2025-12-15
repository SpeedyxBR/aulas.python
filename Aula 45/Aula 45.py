# dir, hasattr e getattr em Python
string  =  'Luiz'
método  =  'tirar'

if hasattr(string, metodo ):
    print ( 'Existe superior' )
    print ( getattr ( string , metodo )())
else:
    print ( 'Não existe o método' , método )