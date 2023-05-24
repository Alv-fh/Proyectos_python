
#Librerias

import time
import os
import shutil
import glob
import random
import time
import math
import turtle
from sys import exit

#para los colores puedes poner colorama o rich, los 2 son muy utiles

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Introducción Proyecto

clear()#si ya creaste la funcion mejor usarla
print ("[*]Cargando programa.")
time.sleep(2)
clear()#si ya creaste la funcion mejor usarla
print ("[*]Cargando programa..")
time.sleep(1)
clear()#si ya creaste la funcion mejor usarla
print ("[*]Cargando programa...")
time.sleep(2)
clear()#si ya creaste la funcion mejor usarla

#Menú de herramientas
def Submenu(): #el orden es importante, no muevas esto debajo de Menu()
    print ()
    print ("_________________________________")
    print ()
    print ("    [*]MENÚ DE HERRAMIENTAS[*]      ")
    print ()
    print ("[1] Copiar Archivos")
    print ("[2] Eliminar Archivos")
    print ("[3] Calculadora")
    print ("[4] Ordenación de Archivos")
    print ("[5] Exit")
    print ()
    print ("_________________________________")


    opc1 = input ("->>> ")
    if opc1 == "1":
        fiche1 = input("Fichero Origen->> ")
        rutadestino = input("Elige en que subdirectorio lo quieres mover->> ") #a donde lo mueves
        rutaorigen = os.getcwd() #Te devuelve la carpeta donde ejecutas este codigo
        rutafinal=rutaorigen+"/"+fiche1 #

        if os.path.isdir(rutaorigen+"/"+rutadestino):#isfile mira si es directorio

            if os.path.isfile(rutafinal):#isfile mira si es archivo
                shutil.move(rutafinal, rutaorigen+"/"+rutadestino)#necesitas copiar con la ruta absoluta
                print("Fichero copiado en " + rutadestino)
            else:# si el archivo no existe
                print(str(fiche1)+" no existe en " + rutaorigen)
        else:# si la carpeta destino no existe
            print("No existe la ruta especificada")
            Submenu()
    elif opc1 == "2":
        fidir = input ("¿Fichero o Carpeta?->> ")
        if fidir == ("Fichero"):
            fiche2 = input("Fichero->> ")
            rutaorigen = os.getcwd()
            os.remove(rutaorigen+"/" + fiche2)
            Submenu()
        elif fidir == ("Carpeta"):
            fiche3 = input("Carpeta->> ")
            shutil.rmtree(fiche3)
            Submenu()
        else:
            print ("No existe la ruta especificada")
            Submenu()
    elif opc1 == "3":
        #Menú
        def submenu2():
            exitt = True
            while exitt == True:
                print("")
                print ("Menú")
                print ("")
                print ("[1] Sumar")
                print ("[2] Restar")
                print ("[3] Multiplicar")
                print ("[4] Dividir")
                print ("[5] Exit")

            #Pregunta

                opc3 = input("->> ")

            #Suma

                if opc3 == "1":
                    num1 = input("Valor 1: ")
                    num2 = input("Valor 2: ")
                    res = float(num1) + float(num2)
                    print()
                    print()
                    print("____________________________")
                    print()
                    print (f"Resultado->> {float(res)}")
                    print("____________________________")
                    print()

            #Resta

                elif opc3 == "2":
                    num1 = input("Valor 1: ")
                    num2 = input ("Valor 2: ")
                    res = float(num1) - float(num2)
                    print()
                    print()
                    print("____________________________")
                    print()
                    print (f"Resultado->> {float(res)}")
                    print("____________________________")
                    print()



            #Multiplicación

                elif opc3 == "3":
                    num1 = input("Valor 1: ")
                    num2 = input("Valor 2: ")
                    res = float(num1) * float(num2)
                    print()
                    print("____________________________")
                    print()
                    print (f"Resultado->> {float(res)}")
                    print("____________________________")
                    print()


            #División

                elif opc3 == "4":
                    num1 = input("Valor 1: ")
                    num2 = input("Valor 2: ")
                    res = float(num1) / float(num2)
                    print()
                    print("____________________________")
                    print()
                    print (f"Resultado->> {float(res)}")
                    print("____________________________")
                    print()


                elif opc3 == "5":
                    print("")
                    print("Exit")
                    print("")
                    exitt = False
                    Submenu()
            submenu2()
        submenu2()

    elif opc1 == "4":
        ruta = input("Ruta absoluta->> ")

        os.chdir(ruta)
        while(True):

            if os.path.exists("documentos") == True:
                pass
            else:
                os.mkdir("documentos")
                continue

            if os.path.exists("fotos") == True:
                pass
            else:
                os.mkdir("fotos")

            if os.path.exists("videos") == True:
                pass
            else:
                os.mkdir("videos")

            if os.path.exists("otros") == True:
                pass
            else:
                os.mkdir("otros")

            if os.path.exists("musica") == True:
                pass
            else:
                os.mkdir("musica")
            break

        #Extensiones de fotos

        png = glob.glob("*.png")
        jpg = glob.glob("*.jpg")
        jpeg = glob.glob("*.jpeg")

        #Extensiones de vídeos

        mp4 = glob.glob("*mp4")
        mkv = glob.glob("*mkv")
        avi = glob.glob("*avi")
        mov = glob.glob("*.mov")
        divx = glob.glob("*divx")

        #Extensiones de audios

        wav = glob.glob("*.wav")
        mp3 = glob.glob("*.mp3")
        aac = glob.glob("*.acc")
        aiff = glob.glob("*.aiff")
        wma = glob.glob("*.wma")
        flv = glob.glob("*.flv")

        #Extensiones de documentos

        pdf = glob.glob("*.pdf")
        doc = glob.glob("*.doc")
        docx = glob.glob("*.docx")
        odt = glob.glob("*.odt")
        txt = glob.glob("*.txt")

        #Mover archivos (fotos)
        for i in (png):
                shutil.move(i, "fotos")
        for i in (jpg):
                shutil.move(i, "fotos")
        for i in (jpeg):
                shutil.move(i, "fotos")

        #Mover archivos (videos)
        for i in (mp4):
                shutil.move(i, "videos")
        for i in (mkv):
                shutil.move(i, "videos")
        for i in (avi):
                shutil.move(i, "videos")
        for i in (mov):
                shutil.move(i, "videos")
        for i in (flv):
                shutil.move(i, "videos")
        for i in (divx):
                shutil.move(i, "videos")

        #Mover archivos (audios)
        for i in (mp3):
                shutil.move(i, "musica")
        for i in (aac):
                shutil.move(i, "musica")
        for i in (wav):
                shutil.move(i, "musica")
        for i in (aiff):
                shutil.move(i, "musica")
        for i in (wma):
                shutil.move(i, "musica")

        #Mover archivos (Documentos)

        for i in (pdf):
                shutil.move(i, "documentos")
        for i in (doc):
                shutil.move(i, "documentos")
        for i in (docx):
                shutil.move(i, "documentos")
        for i in (txt):
                shutil.move(i, "documentos")
        for i in (odt):
                shutil.move(i, "documentos")

        Submenu()

    elif opc1 == "5":
          Menu()

def Contra():
      var = input("Longitud de la contraseña->> ")
      numerocon = input("Cuántas contraseñas quieres->> ")
      letras = "abcdefghijklmnñopqrstuvwxyz"
      ma = letras.upper()
      num = "123456789"
      sim = "@_.#%"
      base = letras+ma+num+sim

      lista = []
      for _ in range(int(numerocon)):
            muestra = random.sample(base, int(var))
            password = "".join(muestra)
            print(password)
            lista.append(password)
      ruta = os.getcwd()+"/"+"Contraseñas.txt"

      file = open(ruta, "w")
      for long in lista:
        file.write(long + os.linesep)
      file.close()

      Menu()

#MENÚ DE JUEGOS

#Función que repite si no son iguales los números, hasta 6 veces, y si se repite pierdes
def Juegos():
    print("_________________________________________")
    print ()
    print ("              [*]JUEGOS[*]              ")
    print ()
    print ("          [1] Ruleta Rusa               ")
    print ("          [2] Adivinador de Contraseña  ")
    print ("          [3] Corazón                   ")
    print ("          [4] Ahorcado                  ")
    print ("          [5] Exit")
    print ()
    print ("________________________________________")

    juego = input ("Juego->> ")
    if juego == "5":
        Menu()

    if juego == "1":
        mesa = random.randint(1,5)
        veces = 0
        while veces < 6:
            tunumero = random.randint(1,5)
            print("")
            print (f"Has disparado y ...")
            if tunumero == mesa:
                print("Has muerto")
                veces = 6
            else:
                print ("Has sobrevivido")
                time.sleep (1)
                veces = veces + 1
        Juegos()

    elif juego == "2":
        contra = "josebenavente"
        contraseña = input("Escriba tu contraseña: ")
        while contraseña != contra:
            contraseña = input("Escriba tu contraseña: ")
        if contraseña == contra:
            print("Contraseña correcta")
    elif juego == "3":
        def xt(t):
            return 16*math.sin(t)**3

        def yt(t):
            return 13*math.cos(t)-5*\
                math.cos(2*t)-2*\
                math.cos(3*t)-\
                math.cos(4*t)
        t = turtle.Turtle()
        t.speed(500)
        turtle.bgcolor("black")

        for i in range (2500):
            t.goto((xt(i)*20, yt(i)*20))
            t.pencolor('red')
            t.goto(0,0)
    elif juego == "4":
         

        palabras = ["alvaro", "khalid", "jose", "pedro", "ruben", "felix", "dani", "herrero", "guti", "david", "alejandro", "jaime", "nicolas", "miguel", "diego","zakaria","pablo"]
        equipos = ["betis", "barcelona", "sevilla", "madrid", "valencia", "celta", "villareal", "girona", "athletic", "osasuna", "sociedad", "mallorca", "almeria", "cadiz", "valladolid", "elche", "espanyol"]
        colores = ["verde","amarillo", "rojo", "naranja", "negro", "blanco", "marron", "azul", "rosa"]

        print("palabras,  equipos, colores")
        opcion = input("¿Qué lista quieres escoger?->> ")
        if opcion == "palabras":
            eleccion = random.choice(palabras)
        elif opcion == "equipos":
            eleccion = random.choice(equipos)
        elif opcion == "colores":
            eleccion = random.choice(colores)

        letras = list(eleccion)
        lediste = [False] * len(eleccion)

        contador = len(eleccion)
        palabra = ""
        print("La palabra tiene", contador, "caracteres")
        def preg(s, listp):
            sino = input("¿Quieres decir la palabra?->> ")
            if sino == "si" or sino == "s":
                palabra = input("Palabra->> ")
                if palabra == eleccion:
                    print("Correcto!!!" + "")
                    exit()
                else:
                    print("Incorrecto")
                    preg(s, listp)
            elif sino == "no" or sino == "n":
                letras2(s, listp)
            else:
                preg(s, listp)
        def letras2(s, listp):

            letra1 = input("Letra->> ")
            if letra1 in listp:
                letras2(s, listp)
            listp.append(letra1)
            sacarletra = eleccion.count(letra1)
            if letra1 != "":
                for i in range(len(eleccion)):
                    if letra1 == letras[i]:
                        lediste[i] = True
            for i in range(len(eleccion)):
                if lediste[i] == True:
                    print(f" {str(letras[i])} ", end='')
                else:
                    print(f" _ ", end=''),
            print()
            
            print("\nTiene", sacarletra, "de su letra", letra1)
            s = s+1
            print(f"Contador->> { s }/10")
            if s != 10:
                #repetir()
                preg(s, listp)
            else:
                print("\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480")
                print("\U0001f480" + "Has sido ahorcado " + "\U0001f480")
                print("\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480" + "\U0001f480")
                print()
                exit()

        letras2(0, [""])

        Juegos()

#menu principal

def Menu():
                print ()
                print("CREATED BY:Álvaro Falcón")
                print ()
                print ("______________________________________")
                print ()
                print ("             [*]MENÚ[*]               ")
                print ()
                print ("[1] Menú de herramientas del sistema")
                print ("[2] Generador de contraseñas")
                print ("[3] Minijuegos interactivos")
                print ("[4] Exit")
                print ()
                print ("_______________________________________")

                opc = input("->>> ")
                if opc == "1":
                    time.sleep(1)
                    Submenu()

                if opc == "2":
                    time.sleep(1)
                    Contra()
                if opc == "3":
                    time.sleep(1)
                    Juegos()
                if opc == "4":
                     time.sleep(1)
                     print("Programa cerrado")
Menu()#necesitas esto para que te ejecute el def, recuerda, esto se llama despues de haber puesto el def
