#diccionarios



diccionario = {
    "nombre":"Juan",
    "edad":18,
    "profesion":"carpintero",
    "soltero":True
}
'''
Los dicionarios son parecidos a los hashmaps de java
se declaran como un json y parejas clave-valor
'''
for i in diccionario.items():
    print(i)

diccionario["nombre"] = "pepe"

for i in diccionario.items():
    print(i)

'''
En Python, los diccionarios son estructuras de datos clave-valor muy útiles. Aquí te dejo algunos de los métodos más utilizados para manipular diccionarios, junto con ejemplos de cada uno:

1. dict.keys():
Este método devuelve una vista de las claves del diccionario.

Ejemplo:
python
mi_dict = {'a': 1, 'b': 2, 'c': 3}
claves = mi_dict.keys()
print(claves)  # Salida: dict_keys(['a', 'b', 'c'])


2. dict.values():
Este método devuelve una vista de los valores del diccionario.

Ejemplo:
python
mi_dict = {'a': 1, 'b': 2, 'c': 3}
valores = mi_dict.values()
print(valores)  # Salida: dict_values([1, 2, 3])

3. dict.items():
Este método devuelve una vista de los pares clave-valor del diccionario como tuplas.

Ejemplo:
python
mi_dict = {'a': 1, 'b': 2, 'c': 3}
items = mi_dict.items()
print(items)  # Salida: dict_items([('a', 1), ('b', 2), ('c', 3)])

4. dict.get(clave, valor_por_defecto):
Este método devuelve el valor asociado a la clave dada. Si la clave no existe, devuelve un valor por defecto (si no se especifica, devuelve None).

Ejemplo:
python
mi_dict = {'a': 1, 'b': 2}
valor = mi_dict.get('a')
print(valor)  # Salida: 1

valor_no_existe = mi_dict.get('c', "No existe")
print(valor_no_existe)  # Salida: No existe

5. dict.update(otro_dict):
Actualiza el diccionario con los pares clave-valor de otro diccionario. Si alguna clave ya existe, su valor será sobrescrito.
Ejemplo:
python
mi_dict = {'a': 1, 'b': 2}
mi_dict.update({'b': 3, 'c': 4})
print(mi_dict)  # Salida: {'a': 1, 'b': 3, 'c': 4}
6. dict.pop(clave, valor_por_defecto):
Elimina la clave especificada del diccionario y devuelve su valor. Si la clave no existe, devuelve el valor por defecto (o lanza una excepción si no se proporciona).

Ejemplo:
python
mi_dict = {'a': 1, 'b': 2, 'c': 3}
valor = mi_dict.pop('b')
print(valor)  # Salida: 2
print(mi_dict)  # Salida: {'a': 1, 'c': 3}

# Si la clave no existe y proporcionamos un valor por defecto
valor_inexistente = mi_dict.pop('d', 'No encontrado')
print(valor_inexistente)  # Salida: No encontrado

7. dict.popitem():
Elimina y devuelve el último par clave-valor insertado como una tupla. En Python 3.7 y versiones posteriores, los diccionarios mantienen el orden de inserción, por lo que popitem() elimina el último elemento insertado.

Ejemplo:
python
mi_dict = {'a': 1, 'b': 2, 'c': 3}
ultimo_item = mi_dict.popitem()
print(ultimo_item)  # Salida: ('c', 3)
print(mi_dict)  # Salida: {'a': 1, 'b': 2}

8. dict.clear():
Este método elimina todos los elementos del diccionario.

Ejemplo:
python
mi_dict = {'a': 1, 'b': 2, 'c': 3}
mi_dict.clear()
print(mi_dict)  # Salida: {}

9. dict.setdefault(clave, valor_por_defecto):
Devuelve el valor de una clave. Si la clave no existe, la inserta con el valor por defecto especificado.
Ejemplo:
python
mi_dict = {'a': 1, 'b': 2}
valor = mi_dict.setdefault('c', 3)
print(valor)  # Salida: 3
print(mi_dict)  # Salida: {'a': 1, 'b': 2, 'c': 3}

10. dict.fromkeys(claves, valor_por_defecto):
Crea un nuevo diccionario a partir de una secuencia de claves, todas con el mismo valor.
Ejemplo:
python
claves = ['a', 'b', 'c']
nuevo_dict = dict.fromkeys(claves, 0)
print(nuevo_dict)  # Salida: {'a': 0, 'b': 0, 'c': 0}


Resumen de los métodos más comunes:
keys(): Obtiene las claves.
values(): Obtiene los valores.
items(): Obtiene los pares clave-valor.
get(): Obtiene el valor de una clave con un valor por defecto.
update(): Actualiza el diccionario con otro diccionario.
pop(): Elimina una clave y devuelve su valor.
popitem(): Elimina y devuelve el último par clave-valor.
clear(): Vacía el diccionario.
setdefault(): Devuelve o inserta un valor por defecto si la clave no existe.
fromkeys(): Crea un diccionario con claves y un valor por defecto.
'''