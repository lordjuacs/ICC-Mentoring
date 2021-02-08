def contar_omitidos(lista):
    total = ord(lista[len(lista) - 1]) - ord(lista[0]) + 1
    return total - len(lista)
print (contar_omitidos (['a', 'd', 'e', 'i']))
print ( contar_omitidos ([ 'a', 'f', 'p']))
print ( contar_omitidos ([ 'f', 'p']))