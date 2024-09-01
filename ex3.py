def subconjuntos(nums):
    resultado = [[]]

    for num in nums:
        # Para cada subconjunto existente, cria um novo subconjunto incluindo o número atual
        novos_subconjuntos = [subconjunto + [num] for subconjunto in resultado]
        # Adiciona esses novos subconjuntos ao resultado
        resultado.extend(novos_subconjuntos)
    
    return resultado

print(subconjuntos([1, 2, 3]))
