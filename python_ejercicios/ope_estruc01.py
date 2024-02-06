# 01 OPERADORES Y ESTRUCTURAS DE CONTROL

'''
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
'''

# Operadores aritmeticos:
'''
valor_uno = 7
valor_dos = 3
valor_tres = 5
valor_cuatro = 5
res_sum = valor_uno + valor_dos
print(res_sum)

res_rest = valor_uno - valor_dos
print(res_rest)

res_div = valor_uno / valor_dos
print(res_div)

res_mul = valor_uno * valor_dos
print(res_mul)

if (valor_uno > valor_dos):
    print("uno")
else:
    print("dos")

if (valor_cuatro < valor_uno):
    print("es menor")
else:
    print("es mayor")

if (valor_cuatro == valor_tres):
    print("son iguales")
else:
    print("naah")
'''

for i in range(10, 56):
    if (i % 2 == 0 or i == 55):
        if (not (i % 3 == 0 or i == 16)):
            print(i)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
