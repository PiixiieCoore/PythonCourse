## Sets ##

my_set = set()
#Se define igual que un diccionario vacio con llaves
my_other_set = {}

#type de un set definido con set() es de tipo 'set'
#type de un set definido con llaves {} es de tipo 'dict'
print(type(my_set))
print(type(my_other_set))

my_other_set = {'Uriel', 'Hernandez', 27}
#el type cambia al ingresar elementos a set
print(type(my_other_set))

#PRIMERA DIFERENCIA: No se puede acceder a los elementos como en las listas y tuplas
# Ej. ERROR: print(my_other_set[0])

#SEGUNDA DIFERENCIA: No es una estructura ordenada, los ordena como quiere
my_other_set.add('PiixiieCoore')
print(my_other_set)
#TERCERA DIFERENCIA: No admite elementos repetidos
my_other_set.add('PiixiieCoore')
print(my_other_set)

#Podemos realizar busquedas con la palabra 'in'
print("Uriel" in my_other_set)
print("Urial" in my_other_set)

#Eliminar elementos
my_other_set.remove('Hernandez')
print(my_other_set)

#Eliminar todos los elementos del set
my_other_set.clear()
print(len(my_other_set))

#Para eliminar toda la variable utilizamos la palabra reservada del

#Unir dos sets
my_other_set = {'Uriel', 'Hernandez', 27}
my_set = {'C++', 'C#', 'Java', 'JavaScrip'}

my_new_set = my_other_set.union(my_set)
print(my_new_set)
print(my_new_set.union({'Python', 'Piixie'}))

# Muestra los elementos diferentes con respecto a otro set
print(my_new_set.difference(my_set))