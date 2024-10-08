#cadenas e caracteres

cadena = "El patio del colegio es cerrado"
otra_cadena = ", pero huele a pis de perro"

#contar el numero de veces que se encuentra algo en la cadena
#podemos marcar el inicio y el final de donde empiezan a buscar
print(cadena.count("io"))
print(cadena.count("io", 0, 12))
print(cadena.count("io", 8, 12))

#metodo find, donde empieza lo que queremos buscar
#tambien podemos indicar el inidico y el final
print(cadena.find("io"))
print(cadena.find("io", 10, 12))

print(cadena  + otra_cadena)

#metodo capitalize. Convierte la primera letra de la cadena en mayúscula.
cadena1 = "python es genial"
print(cadena1.capitalize())  # Python es genial

#metodo upper() Convierte todas las letras de la cadena a mayúsculas.
cadena2 = "hola"
print(cadena2.upper())  # HOLA

#metodo lower() Convierte todas las letras de la cadena a minúsculas.
cadena3 = "HOLA"
print(cadena3.lower())  # hola

#metodo title() Convierte la primera letra de cada palabra en mayúscula.
cadena4 = "python es genial"
print(cadena4.title())  # Python Es Genial

#metodo strip() Elimina los espacios en blanco al principio y al final de la cadena.
cadena5 = "  hola  "
print(cadena5.strip())  # "hola"

#metodo replace(old, new) Reemplaza todas las ocurrencias de una subcadena con otra.
cadena6 = "hola mundo"
print(cadena6.replace("mundo", "Python"))  # hola Python

#metodo split() Divide la cadena en una lista usando el separador sep.
cadena7 = "uno,dos,tres"
print(cadena7.split(','))  # ['uno', 'dos', 'tres']

#metodo join(iterable) Une los elementos de un iterable (como una lista) en una cadena usando el separador especificado
lista1 = ['Python', 'es', 'genial']
print(' '.join(lista1))  # Python es genial

#metodo find(sub) Devuelve la posición de la primera aparición de la subcadena sub. Si no la encuentra, devuelve -1.
cadena8 = "hola mundo"
print(cadena8.find("mundo"))  # 5
print(cadena8.find("Python"))  # -1

#metodo index(sub) Devuelve la posición de la primera aparición de la subcadena sub. Si no la encuentra, lanza un error ValueError.
cadena9 = "hola mundo"
print(cadena9.index("mundo"))  # 5

#metodo startswith(prefix) Devuelve True si la cadena comienza con el prefijo especificado.
cadena10 = "hola mundo"
print(cadena10.startswith("hola"))  # True

#metodo endswith(suffix) Devuelve True si la cadena termina con el sufijo especificado.
cadena11 = "hola mundo"
print(cadena11.endswith("mundo"))  # True

#metodo isalpha() Devuelve True si todos los caracteres de la cadena son letras.
cadena12 = "Python"
print(cadena12.isalpha())  # True

#metodo isdigit() Devuelve True si todos los caracteres de la cadena son dígitos.
cadena13 = "12345"
print(cadena13.isdigit())  # True

#metodo islower() Devuelve True si todos los caracteres de la cadena son minúsculas.
cadena14 = "python"
print(cadena14.islower())  # True

#metodo isupper() Devuelve True si todos los caracteres de la cadena son mayúsculas.
cadena15 = "PYTHON"
print(cadena15.isupper())  # True


















