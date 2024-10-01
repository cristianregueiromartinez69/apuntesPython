#definir funciones en python

def nombreFuncion(parametro1, parametro2):
    print(parametro1, parametro2)


nombreFuncion(5, 2)
nombreFuncion("pepe", True)

#se pueden poner valores por defecto en python y luego sobreescribirlo
def suma(operando1:int = 10, operando2:int = 3):
    return operando1 + operando2

print(suma(5, 2))
print(suma(10))
print(suma(5))
#tambien podemos llamar a los nombres de las variables y añadirles valores, pero no van a sobreescribir la funcion inicial
#es decir, si llamamos a la funcionj suma despues de la que tenemos a continuacion, los valores serán 5 y 2
print(suma(operando1=51, operando2=120))
print(suma())


def imprimir(texto = "<3", veces = 3):
    print(texto * veces)

imprimir("ola", 10)
imprimir(10)
imprimir(veces=20)

#funcion con numero indefinido de parametros
def variosParametros(parametro1, parametro2, *otrosparametros):
    print(parametro1, parametro2, *otrosparametros)
    for parametro in otrosparametros:
        print(parametro)

variosParametros("pepe", "pepe", 1,2,3,4,5,6)