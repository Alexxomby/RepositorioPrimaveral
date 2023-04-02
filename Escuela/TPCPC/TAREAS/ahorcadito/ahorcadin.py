import random
import os
import datetime
#funcion sortear palabra
#funcion pintar las letras de acuerdo al largo de la palabra
#funcion para adivinar la palabra
#Funcion para agregar la letra si se acierta
#funcion para decirte si perdiste o ganaste
#5 generos por jugar

Lista_deportes = ["natacion", "futbol", "equitacion","atletismo", "halterofilia","surf","snowboard","buzkashi","spikeball","eukokanto"]
Lista_animales = ["zamarrito", "tlacuache", "cacomixtle", "abejaruco", "acantiza", "achichilque", "aguacuajada", "akiapolaau", "garrapata", "gorgoncefalo"]
Lista_superHeroes = ["batman","acuaman","deadpool","lobezno","amlo","carlostrejo","jminor","sergioramirez","elkomander","armandoalvarez"]
Lista_flores = ["gardenia","girasol","rosa","orquidea","violeta","acapulco","hortensia","bugambilia","nomeolvides","crisantemo"]
Lista_colores = ["navy","azul","olivo","ocre","lavanda","salmon","ciruela","melocoton","malva","trullo"]
Lista_elegida = []
def AgregrarPalabra():
        print("elige la categoria que desees; tenemos, deportes, animales, super heroes, flores y colores")
        categoriapre = input()
        categoria = categoriapre.lower()
        if categoria == "deportes":
            return Lista_elegida.extend(Lista_deportes)
        elif categoria == "animales":
            return Lista_elegida.extend(Lista_animales)
        elif categoria == "super heroes":
            return Lista_elegida.extend(Lista_superHeroes)
        elif categoria == "flores":
            return Lista_elegida.extend(Lista_flores)
        elif categoria == "colores":
            return Lista_elegida.extend(Lista_colores)

# funcion sortear palabra
def ElegirPalabra(Lista_elegida):
        global azar
        azar = random.choice(Lista_elegida)
        print(azar)
        return azar

def Guardar_palabra (azar):
    global diccionario_respuesta
    diccionario_respuesta = {}
    global letra
    for i, letra in enumerate(azar):
        diccionario_respuesta[i + 1] = letra
    print(diccionario_respuesta)
    return diccionario_respuesta

def OcultarPalabra(azar):
        global diccionario_palabra
        diccionario_palabra = {}
        for posicion, letra in enumerate(azar):
            diccionario_palabra[posicion + 1] = "_"
        print(diccionario_palabra)
        return diccionario_palabra

def Num_vidas():
    joker = 3
    batman = 2
    gatubela = 9

    print("En que dificultad quisieras jugar: gatubela, joker o batman")
    eleccion = input()
    global vida
    if eleccion == "gatubela":
        vida = gatubela
        print("tendras {} vidas, no las malgastes".format(gatubela))
        return vida
    elif eleccion == "joker":
        vida = joker
        print("tendras {} vidas, mi loco".format(joker))
        return vida
    elif eleccion == "batman":
        vida = batman
        print("tendras {} vidas, el joker no estaria tan loco,en fin".format(batman))
        return vida

def hora():
    hora_juego = datetime.datetime.now().time()
    if hora_juego.hour >= 6 and hora_juego.hour < 12:
        hora_juego = "aurora"
        return hora_juego
    elif hora_juego.hour >= 12 and hora_juego.hour < 18:
        hora_juego = "poniente"
        return hora_juego
    else:
        hora_juego = "noctambulo"
        return hora_juego

def saludo(hora_juego):
    usuario = os.getlogin()
    print(f"hola, que tal te va en tu {hora_juego} resplandeciente como el lucero del alba {usuario}")

def A_jugar(letra,diccionario_respuesta,vida,diccionario_palabra):

        lista_posiciones = []
        global aciertos
        aciertos = 0
        while vida > 0 and aciertos < len(diccionario_respuesta):
            print("que letra crees que se encuentre en esta bella palabra")
            print(f"aprovecha que aun te quedan {vida} vidas")
            comillas = input().lower()
            letraxadivinar = comillas
            if letraxadivinar in diccionario_respuesta.values():
                for id , letra in diccionario_respuesta.items():
                    if letra.lower() == letraxadivinar:
                        #diccionario_respuesta[id] = letraxadivinar
                        diccionario_palabra[id] = letraxadivinar
                        aciertos += 1
                print("Adivinasteeee siuu")
                print("antes estaba asi la palabra", diccionario_palabra)
                print(f"afortunadamente la {letraxadivinar} si era")
                print()
                print(f"ya actualizado quedo asi", diccionario_palabra)
            else:
                vida -= 1
                print("letra incock")
                print(diccionario_palabra)
            if aciertos == len(diccionario_respuesta):
                print("ganaste")
            else:
                print("ahi pa la otra mi loco")




hora_juego = hora()
saludo(hora_juego)
Num_vidas()
AgregrarPalabra()
print(Lista_elegida)
ElegirPalabra(Lista_elegida)
Guardar_palabra(azar)
OcultarPalabra(azar)
A_jugar(letra,diccionario_respuesta,vida,diccionario_palabra)

#clonar la lista que tiene las letras, comparar con una funcionm si dicho diccionario
#tiene ese letra, si si , va a guardar el indice donde se detecto la coicidencia
#y lo sustituira en la lista oculta,(quitara el "_"
#falta variable que cuente las vidas que se podran tener

