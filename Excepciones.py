#excepciones
#herencia en python
import math

class Punto:
    #clase qe define un punto bidimentsional en el priemr cuadrante
    def __init__(self, x, y):
        if x >= 0:
             self.x = x
        else:
            raise Errores()
        if y >= 0:
            self.y = y
        else:
            raise Errores()

#podemos utilizar los getter y los setter como en java, pero son innecesarios

    '''def set_X(self, x):
        self.x = x

    def set_Y(self, y):
        self.y = y


    def get_Y(self):
        return self.y

    def get_X(self):
        return self.x'''



    def __str__(self):
        return "La coordenada x es: " + str(self.x) + "\nla coordenada y es: " + str(self.y)


#creacion del objeto de la clase punto
punto1 = Punto(2,3)

#llamamos al metodo __str__ de la clase
print(punto1)

punto1.x = 20
print(punto1)

#metemos entre parentesis la clase de la cual hereda
class Circulo(Punto):

#llamamos al super de la clase con el metodo super()
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        self.radio = radio

    def perimetro(self):
        return 2 * math.pi * self.radio

    def area(self):
        return math.pi * self.radio ** 2

#lo mismo llamamos con el metodo str a traves de la clase de la cual heredamos
    def __str__(self):
        return Punto.__str__(self) + "\nEl radio es: " + str(self.radio)

circulo1 = Circulo(2,3,5)
print(circulo1)
print("El perímetro del círulo es: " + str(circulo1.perimetro()))
print("El area del círulo es: " + str(circulo1.area()))


class Errores(Exception):
    def __str__(self):
        return "Ups, ha ocurrido un error"
