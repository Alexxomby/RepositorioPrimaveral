#programa con funciones
# utlilizar archivos
#crear archivo
#Anadir al archico
#USUAIO entre que frases quiere agregar el texto nuevo
#leer archivo



def CrearArchivo():
    print("hola chaval, que deseareas agregar")
    palaStop = "."
    ListArchivo = []
    while True:
        palabra = input()
        if palabra == palaStop:
            break
        ListArchivo.append(palabra)
        print(ListArchivo)
    return ListArchivo




#ya esta la parte que abre el archivo
def Abrir():
    with open("archivo", "r", encoding = "uft-8") as archivito :

        contenido = archivito.read()
        print(contenido)

    archivito.close

CrearArchivo()
