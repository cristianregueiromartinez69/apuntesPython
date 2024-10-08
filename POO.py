#instanciar objetos

class Punto:
    #clase qe define un punto bidimentsional en el priemr cuadrante
    def __init__(self, x, y):
        self.x = x
        self.y = y

#podemos utilizar los getter y los setter como en java, pero son innecesarios

    def set_X(self, x):
        self.x = x

    def set_Y(self, y):
        self.y = y


    def get_Y(self):
        return self.y

    def get_X(self):
        return self.x



    def __str__(self):
        return "La coordenada x es: " + str(self.x) + "\nla coordenada y es: " + str(self.y)


#creacion del objeto de la clase punto
punto1 = Punto(2,3)

#llamamos al metodo __str__ de la clase
print(punto1)

punto1.x = 20
print(punto1)

'''
metodos de la clase Object:
__init__ -> similar al constructor
__str__ -> similar al toString de java
__new__ -> el constructor, cuando usamos init, llamamos a este metodo
__del__ -> el destructor, similar a en C# eliminar variables por la memoria
__len__ -> devuelve la longitud de un objeto
__eq__ -> compara la posicion de memoria de 2 objetos 
'''
