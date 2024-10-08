#funciones de orden superior, funciones que puedan devolver otras funciones

def saludar(lengua):
    def saludo_en():
        print("Hi")

    def saludo_fr():
        print("salut")

    def saludo_gl():
        print("ola")

    def saludo_jp():
        print("konichiwa")

    def saludo_es():
        print("Hola")

    lengua_func={
        "en": saludo_en,
        "fr": saludo_fr,
        "gl": saludo_gl,
        "jp": saludo_jp,
        "es": saludo_es
    }

    return lengua_func[lengua]

saludo = saludar("es")()

#funciones lambda (funciones anonimas, que no tiene nombre)
area_cuadrado = lambda a: a*a
print(area_cuadrado(10))

def cuadrado(n):
    return n*n

#compresiones de listas
lista = [1,2,3,4]
nueva_lista = [num*2 for num in lista]
print(nueva_lista)
nueva_lista2 = [cuadrado(n) for n in nueva_lista]
print(nueva_lista2)
nueva_lista3 = [n for n in lista if n > 2]
print(nueva_lista3)

l = [0,1,2,3]
m = ['a','b','c','d']
n = [r*s for s in l
     for r in m
     if s > 0]

print(n)





