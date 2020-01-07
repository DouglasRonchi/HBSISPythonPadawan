
def descending_order(number: int) -> int:
    saida = ''
    lista = list(map(int,' '.join(str(number)).split()))
    lista.sort(reverse=True)
    for dado in lista:
        saida += str(dado)
    return int(saida)
