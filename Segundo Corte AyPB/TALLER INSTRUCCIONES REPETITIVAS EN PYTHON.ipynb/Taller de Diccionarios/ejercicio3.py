def verificar_login_corto(usuarios):
    for flor in range(3):
        usuario=input("Usuario: ")
        clave=input("Contraseña: ")
        if usuario in usuarios and usuarios[usuario]["password"]==clave:
            u=usuarios[usuario]
            print(f"Bienvenido, {u['nombre']} {u['apellido']}!")
            return
        print(f"Intento fallido. Te quedan {2-flor}intentos.")
    print("Acceso denegado")

usuarios={
    "iperurena": {"nombre": "Iñaki", "apellido": "Perurena", "password": "123123"},
    "fmuguruza": {"nombre": "Fermin", "apellido": "Muguruza", "password": "654321"},
    "aolaizola": {"nombre": "Aimar", "apellido": "Olaizola", "password": "123456"}
}
verificar_login_corto(usuarios)