### Modulos ###

#Modulo = Libreria (codigo externo a nuestro proyecto)
#Utilizar codigo de funciones (externo)
#Podemos trabajar con ficheros con funciones dentro de otro fichero

#Si queremos llamar un modulo externo NO DEBE empezar con numeros
import module
#podemos hacer uso de la funcion nombrando el fichero y el nombre de la funcion
module.sum_value(1,2,3)

#si queremos importar una funcion concreta utilizamos from
#from functions import sum_two_values

module.print_value(13254)
module.print_value("Hola Python!")

'''
from module import sum_value
#de module importar solamente la funcion 'sum_value'
#Aqui podemos usar sum solo sin utilizar la palabra module antes
sum_value(5, 3, 1)

#si queremos importar las dos funciones por separado podemos:
from module import sum_value, print_value
'''

'''
import math
print(math.pi)
print(math.pow(2,8))

from math import pi
print(pi)

#si le queremos poner un alias a lo importado
from math import pi as PI_VALUE

print(PI_VALUE)
'''
