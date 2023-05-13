## Listas ##
# No es lo mismo lista que arreglo, con listas podemos hacer mas cosas
# Una lista tiene mas funciones que los array
# Operaciones propias de la lista

#Podemos definirlo de estas dos maneras:
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))
#No es necesario guardar siempre el mismo de dato
my_other_list = [27, 1.77, 'Uriel', 'Hernandez']
print(my_other_list)
#type(), ejecuta tipo lista

#Acceder a los valores de las listas
#para acceder al ultimo valor podemos colocar un -1
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
#Da error si nos pasamos del rango de las listas

# Retorna el numero de ocurrencias de un valor
print(my_list.count(30))
print(my_other_list.count('Uriel'))

age, height, name, lastname = my_other_list
print(lastname)

# Concatenar listas
print(my_list + my_other_list)

#Inserta nuevo elemento al final de la lista
my_other_list.append("PiixiieCoore")
print(my_other_list)

#Insertar elementos en la posicion indicada (1), un valor
my_other_list.insert(1,'Rojo')
print(my_other_list)

#Elimina el primer valor que encuentre con el valor de parametro especificado
#Elimina un valor que conocemos que se encuentra dentro
my_other_list.remove("Rojo")
print(my_other_list)

#Copiar una lista a una nueva referencia
my_new_list = my_list.copy()
print(my_list)

#Elimina el ultimo elemento de la lista
print(my_list.pop())
my_list.pop()
print(my_list)

#Especificar el elemento que queremos eliminar
my_list.pop(2)
print(my_list.pop(2))
print(my_list)

#eliminar un elemento especifico de la lista
#elimina por indice
del my_list[1]
print(my_list)

#Eliminar toda la lista
my_list.clear()
print(my_list)
print(my_new_list)

print(my_other_list)

my_other_list.insert(1,'Azul')
print(my_other_list)

#Cambiar el valor de una lista
my_other_list[1] = 'Rojo'
print(my_other_list)

#Odenar los valores al reves
my_other_list.reverse()
print(my_other_list)

#Ordenar la lista por valores
#Solo funciona con valores enteros
my_new_list.sort()
print(my_new_list)

#Imprimir entre valores, desde el valor 2 hasta antes del valor 5
print(my_new_list[2:5])
#