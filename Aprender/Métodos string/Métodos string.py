hola = "hola mi amigo es Alvaro "   

#Pone todo en minúsculas
print(hola.lower())

#Pone todo en mayúsculas
print(hola.upper())

#Pone la primera letra en mayúsculas
print(hola.capitalize())

#Pone la primera letra de cada palabra en mayúsculas
print(hola.title())

#Elimina espacios del lado izquierdo y derecho
print(hola.strip())
print(hola.lstrip()) #Izquierda
print(hola.rstrip()) #Derecha

#Elimina espacios y pone primera letra de cada palabra en mayúsculas
print(hola.strip().title())

#Busca caracteres específicos
opc = hola.find("mi")

if opc == -1:
    print ("La has liado")
else:
    print ("Bienn")

#Cambia las letras que tu quieras
print(hola.replace("ola", "perro"))

#Busca ola y si está te da "True" un boolean, si no la encuentra "False"
comp = ("olas" in hola)
if comp == True:
    print(hola)
else:
    print(hola.title())



