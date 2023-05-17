## Bucles ##

# While, se le pasa una condicion (Mientras sea verdadero, haz algo)
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
#Se le puede agregar un else al while, al no cumplirse la condicion
#Se ejecuta en automatico el else (el else pertenece al while)
else: #Es opcional
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        #detenemos el bucle abruptamente con el break
        print("Se detiene la ejecucion")
        break
    print(my_condition)
print("La ejecucion continua")

# For, itera listado de elementos 

my_list = [35, 24, 62, 52, 30, 30, 17]
#element es la variable para el for (Cualquier estructura que tenga la capacidad de almacenar elementos va a ser iterable)
for element_list in my_list:
    print(element_list)
print("Termina iteracion del list")

#Iterar una tupla
my_tuple = (27, 1.76, 'Uriel', 'Hernandez', 'Uriel')
for element_tuple in my_tuple:
    print(element_tuple)
print("Termina iteracion de la tupla")

#Iterar un set
my_set = {'Uriel', 'Hernandez', 27}
for element_set in my_set:
    print(element_set)
print("Termina iteracion del set")

#Iterar un diccionario
my_dict = {
    "Nombre":"Uriel",
    "Apellido":"Hernandez",
    "Edad":27,
    "Lenguajes": {"Python","Swift","Kotlin"},
    1:1.76
    }
#al igual que en while podemos poner un else y un break para detener el programa
for elements_dict in my_dict:
    print(elements_dict)
    if elements_dict == "Edad":
        break
else:
    print("Termina iteracion del diccionario")

#Podemos colocar en lugar de un break un continue para que continue la ejecucion del programa
for elements_dict in my_dict:
    print(elements_dict)
    if elements_dict == "Edad":
        #Continue se salta la siguiente instruccion (el print de "Se ejecuta") y regresa al for
        continue
    print("Se ejecuta")
else:
    print("Termina iteracion del diccionario")