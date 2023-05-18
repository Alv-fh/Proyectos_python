# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre
# posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario
# su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

sexo = input("masculino o femenino->> ")
nombre = input("nombre->> ")

if sexo == "masculino":
    if nombre.lower() > "n":
        groupa = "A"
        print (f"Perteneces al grupo {(groupa)}")
    else:
        groupb = "B"
        print (f"Perteneces al grupo {(groupb)}")
elif sexo == "femenino":
    if nombre.lower() < "m":
        group2 = "A" 
        print (f"Perteneces al grupo {(group2)}")
    else:
        group3= "B"
        print (f"Perteneces al grupo {(group3)}")