estudiantes={}

num_estudiantes=0
while num_estudiantes<10:
    num_estudiantes=num_estudiantes+1
    codigo=str(num_estudiantes)
    nombre=input(f"Ingrese el nombre del estudiante {num_estudiantes}: ")
    nota_str=input(f"Ingrese la nota de {nombre}: ")
    nota=float(nota_str)
    estudiantes[codigo]={"nombre": nombre, "nota": nota}

aprobados=[]
suspendidos=[]
suma_notas=0
total_estudiantes=0

for codigo in estudiantes:
    info_estudiante=estudiantes[codigo]
    nombre_estudiante=info_estudiante["nombre"]
    nota_estudiante=info_estudiante["nota"]
    suma_notas=suma_notas+nota_estudiante
    total_estudiantes=total_estudiantes+1
    if nota_estudiante>=5:
        aprobados.append(nombre_estudiante)
    else:
        suspendidos.append(nombre_estudiante)

nota_media=suma_notas/total_estudiantes

print("\n Resultados ")
print("Estudiantes aprobados:")
for nombre in aprobados:
    print(nombre)

print("\nEstudiantes suspendidos:")
for nombre in suspendidos:
    print(nombre)

print(f"\nLa nota media de la clase es: {nota_media}")