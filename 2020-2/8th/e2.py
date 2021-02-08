def validacion(contra, user = "Test"):
    num = 0
    voc = 0
    esp = 0
    for i in range(len(contra)):
        if contra[i].isnumeric():
            num += 1
        elif contra[i] in ['A', 'E', 'I', 'O', 'U']:
            voc += 1
        elif contra[i] in ['$','#','&','*','!','?']:
            esp += 1
    if num > 2 and voc > 1 and esp > 0:
        return user + " buena contrasena"
    return user + " contrasena debil"

user = input("Ingrese nombre del usuario: ")
contra = input("Ingrese contrasena (tamano 9): ")

while len(contra) != 9 or ' ' in contra:
    contra = input("Ingrese contrasena (tamano 9): ")
if user != "":
    print(validacion(contra, user))
else:
    print(validacion(contra))