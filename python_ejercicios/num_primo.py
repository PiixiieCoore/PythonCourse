'''
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
'''

####################
### Numero primo ###
####################


def num_prime(num):
    if (num < 1 or num == 1):
        return False
    else:
        for i in range(2, num):
            if (num % i == 0):
                return False
        return True


in_key = int(input("Ingrese un numero >> "))

print(num_prime(in_key))

for i in range(1, in_key + 10):
    if (num_prime(i)):
        print(i, end=' ')
