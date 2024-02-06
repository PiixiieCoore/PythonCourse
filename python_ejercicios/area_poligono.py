'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
'''

########################
### AREA DE POLIGONO ###
########################


def poly_area(polygon):
    lower_case = polygon.lower()
    base = 0
    height = 0
    if (lower_case == 'triangulo'):
        base = int(input('Base >> '))
        height = int(input('Altura >> '))
        res = (base * height) / 2
        return 'Resultado: ' + str(res)
    elif (lower_case == 'cuadrado'):
        base = int(input('Base >> '))
        res = base ** 2
        return 'Resultado: ' + str(res)
    elif (lower_case == 'rectangulo'):
        base = int(input('Base >> '))
        height = int(input('Altura >> '))
        res = base * height
        return 'Resultado: ' + str(res)
    else:
        return 'Error! >> Verifica la figura'


print(poly_area('circulo'))
