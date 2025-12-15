# Escopo de Classes e de Metodos de Classes

class Animal:
    #nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

leao = Animal(nome='Leão')
print(leao.nome)


