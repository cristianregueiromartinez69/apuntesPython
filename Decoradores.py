'''

La funcion decorada funciona de la siguiente manera:
1. Hace unas funciones de antes de empezar la primera funcion
2. Realiza la prpia funcion que estamos decorando
3. Le añadimos unas operaciones posteriores despues de la función a decorar
4. Para imprimirla hacemos que una variable sea igual a la funcion decorador
5. Luego la llamamos
'''

def funcion_necesita_decorador():
    print("Decorador, por favor!")

def mi_decorador(funcion_a_decorar):
    def funcion_envolvente():
        print("Operaciones antes de la función a decorar")
        funcion_a_decorar()
        print("Operaciones posteriores a la ejecución de la función a decorar")
    return funcion_envolvente


funcion_decorada = mi_decorador(funcion_necesita_decorador)

funcion_decorada()

#Podemos hacerlo así también
@mi_decorador
def funcion2_necesita_decorador():
    print("Decorame hijo de la gram perra")

otra_funcion = funcion2_necesita_decorador
otra_funcion()

'''
En este caso vemos que llamamos a una función con el @
la decoramos añadiendo lo que queramos
para ejecutarla, mismo metodo que en lo anterior
'''