## Diccionario ##

my_dict = dict()
my_other_dict = {}

#Ingresar valores (Relacion Clave:Valor)
my_other_dict = {"Nombre": "Uriel","Apellido": "Hernandez", "Edad": 27, 1: "Python"}
#Definicion de un diccionario que dentro tiene un set
my_dict = {
    "Nombre":"Uriel",
    "Apellido":"Hernandez",
    "Edad":27,
    "Lenguajes": {"Python","Swift","Kotlin"},
    1:1.76
    }

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

#Imprimir el valor de un elemento
print(my_dict["Nombre"])

#Actualizar valores de un diccionario
my_dict["Nombre"] = "Piixiie"
print(my_dict)

#Agregar nuevo campo al diccionario
my_dict["Calle"] = "Felipe Villanueva"
print(my_dict)

#Eliminar un elemento al diccionario
del my_dict["Calle"]
print(my_dict)

#Saber si una CLAVE esta en el diccionario
print("Apellido" in my_dict)
print("Uriel" in my_dict)

#Mostrar el diccionario de items (listado de los items)
print(my_dict.items())
#Mostrar solo las keys (listado de claves sin el valor)
print(my_dict.keys())
#Mostrar solo los values (listado de todos los valores)
print(my_dict.values())

#Crear un diccionario nuevo sin valores
my_new_dict = dict.fromkeys(("Nombre", 1))
print(my_new_dict)

#Crear un diccionario vacio a partir de una lista

my_list = ["Nombre", "Apellido", "Edad", "Estatura"]
my_new_other_dict = dict.fromkeys(my_list)
print(my_new_other_dict)

#Crear una copia de un diccionario pero solo conservar claves
my_newest_dict = dict.fromkeys((my_dict))
print((my_newest_dict))
#Fijar valores en todas las claves
my_newest_dict = dict.fromkeys(my_dict, "Uriel")
print((my_newest_dict))

#Diccionario de valores transformado en una lista
print(list(my_other_dict.values()))
#Transformar un diccionario en lista, tupla y set
print(list(my_other_dict))
print(tuple(my_other_dict))
print(set(my_other_dict))