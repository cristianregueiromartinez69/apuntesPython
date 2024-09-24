#colecciones en python

#listas
lista = [1, 2, 3, 4, 5]

print(lista[3])

l2 = list()
for i in lista:
    print(i)

l3 = [1, 'dous', 3.0, [4, 'Y'], 6, 7, 8]
l3[5:7] = ["siete", "VIII"]
for i in l3:
    print(i)

print(l3[1][1])
print(l3[3][1])
print(l3 [-2])
print(l3[1:3])
print(l3[0:-1:2])

l3 = [1,2,3,4,5]
for i in l3:
    print(i)

l4 = [5]
print(type(l4))

#tuplas

miTupla = (1, 2, "tresdostrescuatrosiete", [4, "V"])

for i in miTupla:
    print(i)

''' No se pueden reasignar los valores de una tupla
cuidado con las comas
si pones una tupla de un solo elemento, tienes que ponerlo con la coma
'''
miTupla2 = (3,)
print(type(miTupla2))

miTupla3 = tuple((2,3,4,5,6,67))
for i in miTupla3:
    print(i)

print(miTupla[2][::3])