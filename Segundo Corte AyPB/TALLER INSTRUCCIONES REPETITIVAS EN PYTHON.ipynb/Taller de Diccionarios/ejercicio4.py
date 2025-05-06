def gestionar_notas_estilo_login():
    estudiantes={}
    num_estudiante=1
    while num_estudiante<=10:
        nombre=input(f"Nombre del estudiante {num_estudiante} (o 'fin' para terminar): ")
        if nombre.lower()=='fin':
            break
        nota_str=input(f"Nota de {nombre}: ")
        nota=float(nota_str)
        estudiantes[str(num_estudiante)]={"nombre": nombre, "nota": nota}
        num_estudiante=num_estudiante+1

    aprobados=[]
    suspendidos=[]
    suma_notas=0
    for estudiante_info in estudiantes.values():
        suma_notas=suma_notas+estudiante_info["nota"]
        if estudiante_info["nota"]>=5:
            aprobados.append(estudiante_info["nombre"])
        else:
            suspendidos.append(estudiante_info["nombre"])

    media=suma_notas/len(estudiantes) if estudiantes else 0

    print("\nEstudiantes aprobados:", ", ".join(aprobados) or "Ninguno")
    print("Estudiantes suspendidos:", ", ".join(suspendidos) or "Ninguno")
    print(f"Nota media de la clase: {media:.2f}")

gestionar_notas_estilo_login()