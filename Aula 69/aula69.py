# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023  # Atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def uma_variavel():
        print('Hey')

    @classmethod
    def metro_metodo_idade(cls, nome):
        return cls(nome, 35)
    
p1 = Pessoa('Jão', 22)
p2 = Pessoa.metro_metodo_idade('Marcos')

print(p2.nome, p2.idade)
print(p1.nome, p1.idade)