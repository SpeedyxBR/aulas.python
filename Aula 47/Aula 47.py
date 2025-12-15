# Introdução às Funções do gerador em Python
# gerador = (n para n no intervalo (1000000))

def generator(n=0, maximum= 10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(n=5, maximum=8)
for n in gen:
    print(n)
