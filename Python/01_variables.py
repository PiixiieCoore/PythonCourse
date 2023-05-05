# Variables
#CamelCase no es correcto en python
'''
MyVariable = "My String Variable"
print(MyVariable)
'''
#SnakeCase es buena practica en python

my_string_variable = "My String Variable"
print(my_string_variable)

'''
No esta permitido usar nombre de variables
con simbolos como - @ $ o que 
las variables empiecen con algun numero
'''

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

#Los argumentos se los pasamos a print separados por coma
print(my_string_variable, my_int_variable)

print(my_string_variable, my_int_variable, my_bool_variable)

my_int_to_str_variable = str(my_int_variable)

print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Algunas funciones del sistema
print(len(my_int_to_str_variable))

print(len(my_string_variable))

print("Este es el valor de my_bool_variable: ", my_bool_variable)

#Variables en una sola linea (No abusar de esta sintaxis)

name, lastname, alias, age = 'Uriel', 'Hernandez', 'Pixiie', 27

print('Me llamo:',name, lastname,'mi edad es:', age, 'y mi alias es:',alias)

#Inputs
'''
first_name = input('Cual es tu nombre:')
age = input('Cuantos años tienes?')
print(first_name)
print(age)
'''

#Cambiamos su tipo (Python no es de tipado fuerte)
name = 27
age = 'Uriel'
print(name)
print(age)