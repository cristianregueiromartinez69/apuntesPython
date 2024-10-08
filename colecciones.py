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


'''
Metodos de listas

1. append()
Añade un elemento al final de la lista.

mi_lista = [1, 2, 3]
mi_lista.append(4)
print(mi_lista)  # Salida: [1, 2, 3, 4]


2. extend()
Extiende la lista agregando todos los elementos de otra lista o iterable.

mi_lista = [1, 2, 3]
mi_lista.extend([4, 5, 6])
print(mi_lista)  # Salida: [1, 2, 3, 4, 5, 6]


3. insert()
Inserta un elemento en una posición específica.


mi_lista = [1, 2, 4]
mi_lista.insert(2, 3)  # Inserta el 3 en la posición 2
print(mi_lista)  # Salida: [1, 2, 3, 4]


4. remove()
Elimina el primer elemento que coincide con el valor dado.


mi_lista = [1, 2, 3, 2]
mi_lista.remove(2)
print(mi_lista)  # Salida: [1, 3, 2]  (elimina la primera aparición del 2)


5. pop()
Elimina y devuelve el último elemento de la lista (o un elemento en un índice específico).
mi_lista = [1, 2, 3]
elemento = mi_lista.pop()
print(mi_lista)  # Salida: [1, 2]
print(elemento)  # Salida: 3 (devuelve el valor eliminado)


6. clear()
Elimina todos los elementos de la lista, dejándola vacía.
mi_lista = [1, 2, 3]
mi_lista.clear()
print(mi_lista)  # Salida: []

7. index()
Devuelve el índice del primer elemento que coincide con el valor dado.
mi_lista = [1, 2, 3, 2]
indice = mi_lista.index(2)
print(indice)  # Salida: 1 (el índice de la primera aparición del 2)


8. count()
Devuelve el número de veces que un valor aparece en la lista.
mi_lista = [1, 2, 2, 3]
conteo = mi_lista.count(2)
print(conteo)  # Salida: 2 (el número 2 aparece dos veces)


9. sort()
Ordena los elementos de la lista de menor a mayor (por defecto) o según una clave personalizada.
mi_lista = [3, 1, 4, 2]
mi_lista.sort()
print(mi_lista)  # Salida: [1, 2, 3, 4]
Para orden descendente:
mi_lista.sort(reverse=True)
print(mi_lista)  # Salida: [4, 3, 2, 1]


10. reverse()
Invierte el orden de los elementos de la lista.
mi_lista = [1, 2, 3, 4]
mi_lista.reverse()
print(mi_lista)  # Salida: [4, 3, 2, 1]


11. copy()
Devuelve una copia superficial de la lista.
mi_lista = [1, 2, 3]
mi_lista_copia = mi_lista.copy()
print(mi_lista_copia)  # Salida: [1, 2, 3]


12. len()
Devuelve el número de elementos en la lista.
mi_lista = [1, 2, 3, 4]
longitud = len(mi_lista)
print(longitud)  # Salida: 4


13. in
Verifica si un elemento está en la lista.
mi_lista = [1, 2, 3]
print(2 in mi_lista)  # Salida: True
print(5 in mi_lista)  # Salida: False


14. list()
Convierte un iterable (como una cadena o un rango) en una lista.
cadena = "hola"
lista = list(cadena)
print(lista)  # Salida: ['h', 'o', 'l', 'a']
rango = range(5)
lista_rango = list(rango)
print(lista_rango)  # Salida: [0, 1, 2, 3, 4]
'''


