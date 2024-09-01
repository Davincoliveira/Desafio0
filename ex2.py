def pares_menor_diferenca(lista):
    lista.sort()
    
    menor_diferenca = float('inf')
    pares = []

    # Percorre lista e calcula
    for i in range(len(lista) - 1):
        diff = lista[i + 1] - lista[i]
        if diff < menor_diferenca:
            menor_diferenca = diff
            pares = [(lista[i], lista[i + 1])]
        elif diff == menor_diferenca:
            pares.append((lista[i], lista[i + 1]))

    return pares

print(pares_menor_diferenca([4, 2, 1, 3, 7, 8, 6]))
