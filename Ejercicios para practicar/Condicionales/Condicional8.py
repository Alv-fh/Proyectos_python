# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Escribir un programa que pregunte al usuario su renta anual y 
# muestre por pantalla el tipo impositivo que le corresponde.

renta = int(input("Renta anual->> "))

if renta <= 10000:
    print("5%")
elif renta <= 20000:
    print("15%")
elif renta <= 35000:
    print("20%")
elif renta <= 60000:
    print("30%")
elif renta > 60000:
    print("45%")