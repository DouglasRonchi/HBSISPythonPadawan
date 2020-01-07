import math


def square_digits(number: int) -> int:
    list_main = list(map(int, ' '.join(str(number)).split()))
    saida = ''
    for i in list_main:
        square = int(math.pow(i, 2))
        saida += str(square)
    return int(saida)
