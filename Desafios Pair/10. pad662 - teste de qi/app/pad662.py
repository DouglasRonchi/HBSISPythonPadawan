
def teste_de_qi(dados):

    numeros = dados.split()
    numeros_impares = 0
    numeros_pares = 0
    posicao = 0

    for i in range(0, len(numeros)):
        if int(numeros[i]) % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1

    if numeros_impares > numeros_pares:
        for i in range(0, len(numeros)):
            if int(numeros[i]) % 2 == 0:
                posicao = i + 1
    else:
        for i in range(0, len(numeros)):
            if int(numeros[i]) % 2 != 0:
                posicao = i + 1
    return posicao
