suma=0
k=1
l=1000
while((k**2+1)/k)<l:
    suma=suma+(k**2+1)/k
    k=k+1
    print(f'El número de términos necesarios: ', {k})
