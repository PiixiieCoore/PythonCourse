'''
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
'''

#######################
### ES UN ANAGRAMA? ###
#######################

# va a ser necesario usar len (tamano del string)
# condicionales if

'''
def anagrama(first_string, second_string):
    if (first_string == second_string):
        return False
    elif (len(first_string) == len(second_string)):
        if (sorted(first_string) == sorted(second_string)):
            return True
        else:
            return False
    else:
        return False


print(anagrama('mora', 'ramo'))
'''

#####################################################################
#####################################################################
#####################################################################
#####################################################################


def anagrama2():
    first_string = input('Ingrese primer palabra >> ')
    second_string = input('Ingrese segunda palabra >> ')
    if (first_string == second_string):
        print("ES LA MISMA PALABRA >:(")
    elif (len(first_string) == len(second_string)):
        if (sorted(first_string) == sorted(second_string)):
            print("Es un anagrama! :D")
        else:
            print("No es un anagrama! :(")
    else:
        print("No es un anagrama! :(")


anagrama2()
