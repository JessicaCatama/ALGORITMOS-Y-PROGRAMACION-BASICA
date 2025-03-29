nombre=[]
puntaje=[]
 
while True:
    nombre=input('Introduzca su nombre del estudiante: (O ('fin') para acabar): ')
    if nombre == 'fin':
        break 
    
    while True:
            puntajes = int(input(f"Introduzca el puntaje de {nombre}: "))
            if 0 <= puntajes <= 100:
                puntaje.append(puntajes)
                nombre.append(nombre)
                break
            else:
                print("ERROR: Puntaje inválido. Debe estar entre 0 y 100.")
            print("ERROR: Ingrese un valor numérico válido.")

if not puntaje:
    print('No se registraron')
else:
    puntaje_maximo=max(puntaje)
    puntaje_minimo=min(puntaje)
    promedio=sum(puntaje)/len(puntaje)
    nombre_maximo=nombre[puntaje.index(puntaje_maximo)]
    nombre_minimo=nombre[puntaje.index(puntaje_minimo)]
    estudiantes_bajo_promedio=sum(1 for p in puntaje if p<promedio)
    estudiantes_sobre_promedio=sum(1 for p in puntaje if p>=promedio)
    porcentaje_bajo_promedio=(estudiantes_bajo_promedio/len(puntaje))*100
    porcentaje_sobre_promedio=(estudiantes_sobre_promedio/len(puntaje))*100
    
    print('Resultados del Análisis')
    print(f'Nombre del estudiante con puntaje más alto: {nombre_maximo}')
    print(f'Puntaje máximo: {puntaje_maximo}')
    print(f'Nombre del estudiante con puntaje más bajo: {nombre_minimo}')
    print(f'Puntaje mínimo: {puntaje_minimo}')
    print(f'Promedio de puntajes: {promedio:.2f}')
    print(f'Porcentaje de estudiantes bajo el promedio: {porcentaje_bajo_promedio:.2f}%')
    print(f'Porcentaje de estudiantes sobre el promedio: {porcentaje_sobre_promedio:.2f}%')
