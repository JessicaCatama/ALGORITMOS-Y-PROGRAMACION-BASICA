dividendo=int(input('Dividendo: '))
divisor=int(input('Divisor: '))

contador=0
while(dividendo>=divisor):
    contador=contador+1 
    dividendo=dividendo-divisor
    
print(f'Cociente: {contador}')
print(f'Residuo: {dividendo}')