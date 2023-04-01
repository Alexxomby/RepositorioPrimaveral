import random
#funcion sortear palabra
#funcion pintar las letras de acuerdo al largo de la palabra
#funcion para adivinar la palabra
#Funcion para agregar la letra si se acierta
#funcion para decirte si perdiste o ganaste
#5 generos por jugar

Lista_deportes = ["natacion", "Futbol", "equitacion","atletismo", "halterofilia","surf","snowboard","buzkashi","spikeball","eukokanto"]
Lista_animales = ["zamarrito", "tlacuache", "cacomixtle", "abejaruco", "acantiza", "achichilque", "aguacuajada", "akiapolaau", "garrapata", "gorgoncefalo"]
Lista_superHeroes = ["batman","acuaman","deadpool","lobezno","amlo","carlostrejo","jminor","sergioramirez","elkomander","armandoalvarez"]
Lista_flores = ["gardenia","girasol","rosa","orquidea","violeta","acapulco","hortensia","bugambilia","nomeolvides","crisantemo"]
Lista_colores = ["navy","azul","olivo","ocre","lavanda","salmon","ciruela","melocoton","malva","trullo"]
Lista_elegida = []
def AgregrarPalabra():
        print("elige la categoria que desees; tenemos, deportes, animales, super heroes, flores y colores")
        categoriapre = input()
        categoria = categoriapre.lower()
        if categoria == "deporte":
            return Lista_elegida.extend(Lista_deportes)
        elif categoria == "animales":
            return Lista_elegida.extend(Lista_animales)
        elif categoria == "super heroes":
            return Lista_elegida.extend(Lista_superHeroes)
        elif categoria == "animales":
            return Lista_elegida.extend(Lista_animales)
        elif categoria == "flores":
            return Lista_elegida.extend(Lista_flores)
        elif categoria == "colores":
            return Lista_elegida.extend(Lista_colores)



# funcion sortear palabra
def ElegirPalabra(Lista_elegida):
        Azar = random.choice(Lista_elegida)
        print(Azar)
        return Azar

def OcultarPalabra(Azar):
        Antes_Ocultar = list(Azar)
        print(Antes_Ocultar)
        return Antes_Ocultar


AgregrarPalabra()
print(Lista_elegida)
ElegirPalabra(Lista_elegida)
OcultarPalabra(Azar)


