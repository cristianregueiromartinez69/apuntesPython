#polimorfismo y encapsulacion en python
import math

class Punto:
    #clase qe define un punto bidimentsional en el priemr cuadrante
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

class Punto2:
    def __init__(self, x, y):
        #añadimos __ para hacer los atributos privados
        self.__x = x
        self.__y = y

    def get_X(self):
        return self.__x

    def get_Y(self):
        return self.__y

    def set_X(self,x):
        if x < 0:
            self.__x = 0
        else:
            self.__x = x

    def set_Y(self,y):
        if y < 0:
            self.__y = 0
        else:
            self.__y = y

    x = property(get_X, set_X)
    y = property(get_Y, set_Y)

    #lo mismo para los métodos
    def __coordenadas(self):
        return "La coordenada X es: " + str(self.__x) + "\nLa coordenada Y es: " + str(self.__y)

    def __str__(self):
        return "X: " + str(self.__x) + "\nY: " + str(self.__y)

    def __eq__(self, p2):
        if self.__x == p2.__x and self.__y == p2.__y:
            return True
        else:
            return False


punto2 = Punto2(2, 3)

# Acceder a los atributos privados usando _Punto2__x y _Punto2__y
print("X es: " + str(punto2.x))
print(punto2._Punto2__coordenadas())

punto2.y = 10
print("Y es: " + str(punto2.y))

p3 = Punto2(2,3)
p4 = Punto2(2,3)
print(p3.__eq__(p4))

