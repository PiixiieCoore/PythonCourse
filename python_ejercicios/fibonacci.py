'''
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
'''

#############################
### SUCESIÓN DE FIBONACCI ###
#############################


def fibonacci(n):
    my_list = [0, 1]
    for i in my_list:
        if (len(my_list) - 1 == n):
            break
        else:
            new_value = my_list[-1] + my_list[-2]
            my_list.append(new_value)
    print(my_list)


fibonacci(7)
