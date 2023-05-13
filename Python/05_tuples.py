## Tuples ##

#La estructura de una lista es con corchetes[]
#La estructura de una tupla es con parentesis()
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (27, 1.76, 'Uriel', 'Hernandez', 'Uriel')
print(my_tuple)
my_other_tuple = (25, 60, 30) 
#Accedemos a los elementos con corchetes
print(my_tuple[0])
print(my_tuple[-1])

#Cuenta el numero de incidencias
print(my_tuple.count('Uriel'))
#Nos dice el indice en donde se encuentra el elemento
print(my_tuple.index('Hernandez'))

# PRIMERA DIFERENCIA: Las tuplas no mutan (no se puede cambiar los valores de una tupla)

#Concatenar tuplas
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
#Slice de una tupla
print(my_sum_tuple[3:6])

# del my_tuple no solo borra la tupla sino elimina toda la variable