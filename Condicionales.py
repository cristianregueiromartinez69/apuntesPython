def dameNumero(num1):
    if num > 0:
        print("este numero es mayor que 0")
    elif num < 0:
        print("este numero es menor que 0")
    else:
        print("este numero es igual a 0")


num = int(input("introduce un numero"))
dameNumero(num)

#parecido con el ? en java
par = True if num % 2 == 0 else False
print(par)

#bucle while
variable = 4

while variable >= 4:
    variable = int(input("introduce un numero"))

'''
En Python, el bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera. El ciclo se ejecuta repetidamente hasta que la condición se vuelva falsa.

Sintaxis del bucle while en Python:
python
while condicion:
    # Bloque de código a ejecutar mientras la condición sea verdadera
condicion: Una expresión que se evalúa como True o False. Mientras sea True, el bucle continúa.
Bloque de código: El código indentado dentro del while que se ejecuta en cada iteración.
Ejemplo básico:
python
contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador += 1  # Incrementa el valor de contador en 1

# Salida:
# Contador: 1
# Contador: 2
# Contador: 3
# Contador: 4
# Contador: 5
En este ejemplo:

El bucle while continúa ejecutándose mientras la condición contador <= 5 sea verdadera.
Cada vez que se ejecuta el bucle, se incrementa contador en 1.
El bucle se detiene cuando contador es mayor que 5.
Control de flujo en while:
break: Rompe el ciclo, incluso si la condición es verdadera.
continue: Salta el resto del bloque de código y vuelve a la siguiente iteración.
else: Un bloque opcional que se ejecuta cuando la condición se vuelve falsa, a menos que se haya roto el ciclo con break.
Ejemplo con break:
python
contador = 1

while contador <= 5:
    if contador == 3:
        break  # Rompe el ciclo cuando contador es 3
    print("Contador:", contador)
    contador += 1

# Salida:
# Contador: 1
# Contador: 2
Ejemplo con continue:
python
contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue  # Salta a la siguiente iteración cuando contador es 3
    print("Contador:", contador)

# Salida:
# Contador: 1
# Contador: 2
# Contador: 4
# Contador: 5
Bucle while con else:
El bloque else se ejecuta cuando la condición del while es falsa y el ciclo ha terminado normalmente (sin un break).

python
contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador += 1
else:
    print("El bucle ha terminado.")

# Salida:
# Contador: 1
# Contador: 2
# Contador: 3
# Contador: 4
# Contador: 5
# El bucle ha terminado.
Ejemplo con entrada del usuario:
Un caso típico de uso es cuando quieres que el programa siga solicitando entrada hasta que el usuario proporcione algo específico.

python
respuesta = ""

while respuesta != "salir":
    respuesta = input("Escribe algo (escribe 'salir' para terminar): ")
    print("Has escrito:", respuesta)

# El bucle termina cuando el usuario escribe "salir".
Conclusión:
El bucle while es útil cuando no sabes de antemano cuántas veces quieres repetir un bloque de código, pero sí tienes una condición que debes cumplir para seguir iterando.
Puedes controlar su comportamiento con break, continue y else para manejar distintos casos durante la ejecución.
'''

#simulacion del bucle do-while
while True:
    numero = int(input("Introduce un número positivo: "))

    # El código dentro del "do" se ejecuta al menos una vez
    if numero > 0:
        print(f"Número ingresado: {numero}")
        break  # Salir del bucle cuando la condición se cumple
    else:
        print("Por favor, introduce un número positivo.")

'''
Explicación:
while True: El bucle es infinito, lo que significa que se ejecutará continuamente hasta que una condición interna lo detenga.
if-else y break: Dentro del bucle, se verifica si el número es positivo. Si lo es, se ejecuta break para detener el bucle. Si no, el ciclo se repite.
Esto simula el comportamiento de un do-while, ya que el código dentro del bucle se ejecuta al menos una vez.
'''

#otro ejemplo
while True:
    opcion = input("Escribe 'salir' para terminar: ")

    if opcion == "salir":
        print("Terminando el bucle.")
        break  # Salir del bucle
    else:
        print("Todavía en el bucle.")



#bucle for python
listas = [1,2,3,4,5]

for lista in listas:
    print(lista)


#bucle for con cadenas de texto
texto = "Python"

for letra in texto:
    print(letra)

# Salida:
# P
# y
# t
# h
# o
# n


#bucle for con diccionarios
mi_dict = {'a': 1, 'b': 2, 'c': 3}

for clave in mi_dict:
    print(clave)

# Salida:
# a
# b
# c
#Si quieres iterar tanto sobre las claves como sobre los valores, puedes usar el método items():

mi_dict = {'a': 1, 'b': 2, 'c': 3}

for clave, valor in mi_dict.items():
    print(f"Clave: {clave}, Valor: {valor}")

# Salida:
# Clave: a, Valor: 1
# Clave: b, Valor: 2
# Clave: c, Valor: 3

#uso de range
#range() es una función muy útil que genera una secuencia de números.
# A menudo se usa con for para iterar un número específico de veces.

'''
range(inicio, fin, paso)
inicio: El valor inicial (por defecto es 0).
fin: El valor final, no inclusivo.
paso: El valor a incrementar en cada iteración (por defecto es 1).
'''
for i in range(5):
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4

#ejemplo de inicio y paso
for i in range(1, 10, 2):
    print(i)

# Salida:
# 1
# 3
# 5
# 7
# 9

#for con el else
for i in range(5):
    print(i)
else:
    print("El bucle ha terminado.")

# Salida:
# 0
# 1
# 2
# 3
# 4
# El bucle ha terminado.


#for con el break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("El bucle ha terminado.")

# Salida:
# 0
# 1
# 2


lista3 = ["jaimito", "pepito", 1, 2 ,3, 4, "fulanito"]

for i in range(0, len(lista3), 1):
    print(lista3[i])



for indice, valor in enumerate(lista3):
    print(indice, valor)


'''
Ejemplo con start:
Puedes especificar un índice de inicio diferente si no quieres empezar desde 0
'''
frutas = ['manzana', 'banana', 'cereza']

for indice, fruta in enumerate(frutas, start=1):
    print(f"Índice: {indice}, Fruta: {fruta}")

# Salida:
# Índice: 1, Fruta: manzana
# Índice: 2, Fruta: banana
# Índice: 3, Fruta: cereza


'''
Modificar una lista mientras iteras: enumerate() es útil cuando necesitas modificar 
o actualizar elementos en una lista basándote en su índice.

Ejemplo: Cambiar todos los valores en posiciones pares de una lista:
'''

numeros = [10, 20, 30, 40, 50]

for indice, numero in enumerate(numeros):
    if indice % 2 == 0:  # Si el índice es par
        numeros[indice] = numero * 2

print(numeros)

