# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y
# todos los ingredientes que lleva.

pizza = input("¿Pizza vegetariana?->> ")
if pizza == "si":
    opc = input("Añadir pimiento o tofu?->> ")
    if opc == "pimiento":
        print("        Pizza vegetariana    ")
        print("   [*]Ingredientes[*]        ")
        print()
        print("   -Mozzarella               ")
        print("   -Tomate                   ")
        print("   -Pimiento                 ")
    elif opc == "tofu":
        print("        Pizza vegetariana    ")
        print("   [*]Ingredientes[*]        ")
        print()
        print("   -Mozzarella               ")
        print("   -Tomate                   ")
        print("   -tofu                     ")
        print()
elif pizza == "no":
    opc2 = input("¿Añadir jamón peperoni o salmón?-->> ")
    if opc2 == "jamón":
        print("     Pizza no vegetariana    ")
        print("   [*]Ingredientes[*]        ")
        print()
        print("   -Mozzarella               ")
        print("   -Tomate                   ")
        print("   -jamón                    ")
        print()
    elif opc2 == "peperoni":
        print("     Pizza no vegetariana    ")
        print("   [*]Ingredientes[*]        ")
        print()
        print("   -Mozzarella               ")
        print("   -Tomate                   ")
        print("   -peperoni                 ")
        print()
    elif opc2 == "salmón":
        print("     Pizza no vegetariana    ")
        print("   [*]Ingredientes[*]        ")
        print()
        print("   -Mozzarella               ")
        print("   -Tomate                   ")
        print("   -salmón                   ")
        print()