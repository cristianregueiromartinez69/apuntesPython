#generadores

'''

La diferencia de un generador con una lista es lo siguiente:
Si trabajamos con listas muy grandes, generamos un generador a partir de una lista
Pesa mucho menos que si tuvieramos una lista de muchos muchos datos
Nosotros iteramos sobre el generador, ya que acceder a el directamente no funciona
'''
lista = [1,2,3,4,5,6,7,-3,-10,6,5,434]
x = (n**2 for n in lista)

for n in x:
    print("Mi generador sin funcion es: " + str(n))

def mi_generador(lista):
    for n in lista:
        yield n**2
print()
for n in mi_generador(lista):
    print("Mi generador con funcion es: " + str(n))

print()
lista2 = list(mi_generador(lista))
tupla = tuple(mi_generador(lista))

print(lista2)
print()
print(tupla)
'''
Podemos hacerlo mediante una funcion o mediante una variable
el yield es como un return pero no retorna al momento, si no que espera a que acabe el bucle
'''