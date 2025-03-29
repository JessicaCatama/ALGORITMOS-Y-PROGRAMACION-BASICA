saldo=1500000
depositos=[]
retiros=[]

while True:
    cajero=input('¿Depositar, retirar o salir? (D/R/S): ')
    if cajero=='D':
        monto=int(input('Ingrese el monto a depositar: '))
        depositos.append(monto)
        saldo+=monto
        print(f'Depósito exitoso. Saldo actual: {saldo}')
    elif cajero=='R':
        monto=int(input('Ingrese el monto a retirar: '))
        if monto<=saldo:
            retiros.append(monto)
            saldo-=monto
            print(f'Retiro exitoso. Saldo actual: {saldo}')
        else:
            print('Saldo insuficiente')
    elif cajero=='S':
        print(f'Saldo final: {saldo}')
        break
    
    else:
        print('Opción no válida, intenta nuevamente')
