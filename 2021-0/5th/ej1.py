def insertionSort(lista):
    arr = lista
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


ventas = {" Xiaomi ": 96, " Oppo ": 119, "LG ": 55.9, " Lenovo": 49.9,
          " Nokia ": 7.7, " TecnoPro ": 13.1, " Dell ": 6.1,
          " IBM ": 0.6, " Sahito ": 34.6, " Samsung ": 318.1, " Apple ": 215.8, " Vivo ": 100.2, " Huawei ": 153.1,
          " Aio ": 45.6, " FirePhone ": 29.7, " Motorola ": 20.3}

ordenada = insertionSort(list(ventas.values()))

mayor = ordenada[len(ordenada) - 1]
menor = ordenada[0]
print(ordenada)
print(mayor)
print(menor)
