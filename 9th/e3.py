def ingresar_datos(dic):
    n = int(input("Ingrese la cantidad de datos a agregar: "))
    for i in range(n):
        s = input("Ingrese la fecha: ")
        t = int(input("Ingrese la temperatura: "))
        dic[s] = t

def get(dic, opcion = 0):
    values = list(dic.values())
    keys = list(dic.keys())
    if opcion:
        op = min(values)
    else:
        op = max(values)
    return keys[values.index(op)]




lima = {"22/05/2019":17 , "23/05/2019":17 , "24/05/2019":19 ,
    "25/05/2019":23 , "26/05/2019":20 , "27/05/2019":18 ,
    "28/05/2019":20 , "29/05/2019":19 , "30/05/2019":22 ,
    "31/05/2019":19 , "01/06/2019":20 , "02/06/2019":19 ,
    "03/06/2019":17 , "04/06/2019":16 , "05/06/2019":18 ,
    "06/06/2019":21 , "07/06/2019":19 , "08/06/2019":15 ,
    "09/06/2019":17 , "10/06/2019":20 , "11/06/2019":15 ,
    "12/06/2019":22 , "13/06/2019":14 , "14/06/2019":16 }


ingresar_datos(lima)
print("La fecha donde la temperatura fue mas baja fue:", get(lima, 1))
print("La fecha donde la temperatura fue mas alta fue:", get(lima))