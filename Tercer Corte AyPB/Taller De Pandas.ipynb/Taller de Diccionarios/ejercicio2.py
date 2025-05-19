diccionario={'Mike':3, 'Ane':8, 'Amaia':12, 'Unai':5, 'Jon':8, 'Ainhoa':7, 'Maite':5}
lista=[]
for key in diccionario.keys():
    if(lista.count(diccionario[key])==0):
        lista.append(diccionario[key])
print(lista)