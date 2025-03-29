saldo = 1_000_000
while True:
    print("1. Depositar Dinero\n 2. Retirar \n 3. Consultar Saldo\n 4. Salir:")
    opcion=int(input("Ingrese opción: "))
    if(opcion==4):
        break
    elif(opcion==1):
        deposito=float(input("Ingrese monto a depositar: "))
        saldo=saldo+deposito
    elif(opcion==2):
        retiro=float(input("Ingrese monto a retirar: "))
        if(saldo<retiro):
            print("Saldo insuficiente: ")
        else:
            saldo=saldo-retirar
    elif(opcion==3):
        print ("Saldo",saldo) 