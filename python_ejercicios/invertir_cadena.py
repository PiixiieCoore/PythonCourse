'''
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
'''

########################
### INVERTIR CANDENA ###
########################

# Primera forma de invertir cadena de caracteres
text1 = 'Abecedario'
inver_text1 = text1[::-1]
print(inver_text1)

# Segunda forma de invertir cadena de caracteres
text2 = 'Pete Seguro'
invert_text2 = reversed(text2)
for i in invert_text2:
    print(i, end='')
print('')

# Tercera forma de invertir cadedna de caracteres (MEJOR OPCION)
text3 = 'Hola Mundo'
reversed_string = ''
for index in text3:
    reversed_string = index + reversed_string
print(reversed_string)

# Cuarta forma de invertir cadedna de caracteres
text4 = 'Piixiie Coore'
for index in range(len(text4) - 1, -1, -1):
    print(text4[index], end='')
print('')

# Quinta forma de invertir cadedna de caracteres


def invert_string(cadena):
    inver_list = []
    for i in cadena:
        inver_list.append(i)
    inver_list.reverse()
    new_invert_string = ''
    for i in inver_list:
        new_invert_string += i
    print(new_invert_string)


invert_string('Uriel Hernandez')
