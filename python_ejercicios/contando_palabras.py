'''
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
'''

#########################
### CONTANDO PALABRAS ###
#########################

lista_palabras = ['Perro', 'gato', 'perro', 'GATO', 'arbol',
                  'nino', 'nina', 'Nino', 'Carro', 'Casa', 'carro', 'Arbol', 'PERRO']


def count_string(initial_list):
    lower_list = list()
    stringed_list = list()
    ready_set = set()
    for i in initial_list:
        lower_list.append(i.lower())
    for i in lower_list:
        count_list = lower_list.count(i)
        string_plus_num = i + ' = ' + str(count_list)
        stringed_list.append(string_plus_num)
    for i in stringed_list:
        ready_set.add(i)
    return ready_set


print(count_string(lista_palabras))
