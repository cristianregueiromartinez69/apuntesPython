def dameNumero(num):
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