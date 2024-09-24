#tipos en python
identificador = "valor"


numero = 4

print(type(numero))



real = 0.00002

print(type(real))

real2 = 2e-5


print(type(real2))

complexo = 2 + 4j

print(type(complexo))

#operadores de python

"""
+ suma 
- resta 
* multiplicacion 
/ division 
// division entera 
% modulo 
** exponente
"""

""" Operadores para números binarios 
& i logica
| o logico
^ o exclusivo
~ negacion
<< desplazamiento izquierda
>> desplazamiento derecha
"""

num = 5
print(num >> 1)
print(num << 1)
print(num & 2)

#las 2 formas valen de sobra
cadea = 'otra cadena'
cadea2 = "la utilidad es 'que puedo remarcar' con comillas dentro del texto"

print(cadea)
print(cadea2)

#comentario de una sola linea. Se utiliza para explicar notas sobre el código

''' Comentario multilinea 
Se utiliza maioritariamente para la documentacion del codigo
'''

print("concatenar " + " " + " varias cadenas" + " de " +  "texto")

print("multiplica " * 3)

print("une ", "varios", "string")

#booleanos

'''operadores booleanos

and
or
not
==
!=
>
<
>=
<=
'''

print(True and False)
print(True or False)
print(not True)