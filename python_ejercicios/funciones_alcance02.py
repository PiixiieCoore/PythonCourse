# 02 FUNCIONES Y ALCANCE

'''
/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
'''

# definicion de funcion sin parametros ni retorno

'''
def funcion1():
    print('Hola mundo')


funcion1()


# variante de Hola mundo en funcion

def funcion2():
    saludo = 'Hola mundo 2'
    return saludo


print(funcion2())


# definicion de funcion sin parametros con retorno (true)

def funcion3():
    return True


print(funcion3())


# definicion de funcion con un parametro sin retorno
def funcion4(valor):
    print('Hola', valor)


funcion4('Piixiie')

# definicion de funcion con dos parametros y retorno
# Variables locales y globales


def funcion5(a, b):
    suma = a + b
    return suma


valor_uno = 22
valor_dos = 11
print(funcion5(valor_uno, valor_dos))
'''

##########################################################

#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
#  */


def my_function(first_string, second_string):
    count = 0
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print(first_string.upper(), second_string.upper(), end=', ')
        elif (i % 3 == 0):
            print(first_string, end=', ')
        elif (i % 5 == 0):
            print(second_string, end=', ')
        else:
            print(i, end=', ')
            count += 1
    return '\n\n' + 'Numero de veces que se imprime los numero >> ' + str(count)


print(my_function('pato', 'ganzo'))
