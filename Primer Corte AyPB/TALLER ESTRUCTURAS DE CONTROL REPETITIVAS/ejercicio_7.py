estudiante=int(input('Número de estudiante: '))
max_altura=0

for N in range(estudiante):
    estatura=float(input(f'Estatura del estudiante {N+1}: '))
    if estatura>max_altura:
        max_altura=estatura
print(f'Altura más alta: ', {max_altura})