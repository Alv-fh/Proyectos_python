#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

dividendo = int(input("Número1->> "))
divisor = int(input("Número2->> "))

if divisor != 0:
    resul = dividendo / divisor
    print(resul)
else:
    print("Error")
