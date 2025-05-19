lista=[12, 23, 5, 12, 92, 5, 12, 29, 92, 64, 23]
diccionario={}
for i in lista:
    diccionario.update({i:lista.count(i)})
print(diccionario)