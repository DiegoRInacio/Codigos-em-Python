from random import randint
num = list()
def sorteia():
    for c in range(0,5):
        num.append(randint(0,9))
    print(f'Os valores sorteados foram {num}')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares obtemos {soma}')


sorteia()
somaPar(num)