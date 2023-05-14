## Condicionales ##

my_condition = True
# if definido con dos puntos

if my_condition:
    print("Se ejecuta la condicion del if")
print("La ejecucion continua")

# Condicion con numero
my_second_condition = 5 * 2
if my_second_condition == 10:
    print("Se ejecuta la condicion del segundo if")
print("La ejecucion continua nuevamente")

# con else siempre ejecuta una linea de codigo
if my_second_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")
print("La ejecucion continua")

# Operadores logicos para concatenar condiciones
if my_second_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor 10 o mayor que 20")
print("...")

# elif sirve para comprovar nuevamente la condicion
# else caso por defecto (si la condicion no se cumple se va al else)
# elif necesita una condicion
if my_condition == 10:
    print("Condicion igual a 10")

if my_second_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor 10 o mayor que 20")
print("...")
#