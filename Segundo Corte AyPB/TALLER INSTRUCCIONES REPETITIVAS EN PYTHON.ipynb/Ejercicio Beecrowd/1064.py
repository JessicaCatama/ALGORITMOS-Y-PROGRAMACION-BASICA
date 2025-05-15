positivos=[]
for hola in range(6):
    numero=float(input())
    if numero>0:
        positivos.append(numero)

cant_positivos=len(positivos)
print(f"{cant_positivos} valores positivos")

if cant_positivos>0:
    prom_positivos=sum(positivos)/cant_positivos
    print(f"{prom_positivos:.1f}")