Usuario = "1smra"
Contraseña = "usuario"

login = input("Nombre de Usuario->> ")
loginp = input("Contraseña de Usuario->> ")

if login == Usuario and loginp == Contraseña:
    print("ACCESO CONCEDIDO")   
elif login != Usuario and loginp == Contraseña:
    print("ACCESO DENEGADO")


