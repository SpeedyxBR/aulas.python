# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
 
  #Definir uma Função
    def __init__(self, nome):         
        self.nome = nome
    
    #Elaborando o Motor
    def motor_carro(self, m1):
        print(f'{self.nome} tem o motor {m1.nome}')
    
    def fabricante_carro(self, f1):
        print(f'{self.nome} foi fabricado por {f1.nome}')
    
class Motor:
 
    def __init__(self, nome):
        self.nome = nome
    
class Fabricante:
    #Unindo fuções
    def __init__(self, nome):
        self.nome = nome
        
carro1 = Carro("Celta")
carro2 = Carro("Cruze")
motor1 = Motor("V6 1.0")
fabricante1 = Fabricante("Chevrolet")
 
carro1.motor_carro(motor1)
carro2.fabricante_carro(fabricante1)
carro2.motor_carro(motor1)
 