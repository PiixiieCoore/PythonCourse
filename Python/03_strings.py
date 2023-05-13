### Strings ###

my_string = 'Mi Strings'
my_other_string = 'Mi otro Strings'

print(len(my_string))
print(len(my_other_string))

print(my_string + ' ' + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_escape_string = "\\tEste es un String  \\n escapado"
print(my_escape_string)

# Formateo, esto sirve principalmente para cuando estamos internacionalizando texto

name, lastname, age = 'Uriel', 'Hernandez', 27
#%s para los Strings
#%d para los integers
#%f para los floats

#con .format (forma nueva)
print("Mi nombre es {} {} y mi edad es {}".format(name, lastname,age))
# con operador % (forma antigua)
print("Mi nombre es %s %s y mi edad es %d" %(name, lastname, age))
#... para evitar hacer...
print("Mi nombre es " + name + " " + lastname + " y mi edad es " + str(age))

# Inferencia de datos (forma mas rapida)
# la F sirve para formatear rapidamente las variables en el String
print(f"Mi nombre es {name} {lastname} y mi edad es {age}")

# Desempaquetado de caracteres
# (crear variables a partir de un string y su longitud)
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Division 
#Toma el caracter en indice 1 (y) hasta antes del indice 3 (t)
language_slice = language[1:3]
print(language_slice)

#Desde el indice 1 (y) y lo restante
language_slice = language[1:]
print(language_slice)
# Imprime desde el final (el final empieza en -1)
language_slice = language[-2]
print(language_slice)
#Toma un rango (del 0 al 6) y despues elimina de dos en dos (:2)
#de la palabra PYTHON
'''
P 0 +
Y 1 -
T 2 +
H 3 -
O 4 +
N 5 -
'''
language_slice = language[0:6:2]
print(language_slice)

# Reverse (permite escribir al reves)

reversed_language = language[::-1]
print(reversed_language)

# Funciones

#Primera en Mayuscula
print(language.capitalize()) 
#Manda todo en mayuscula
print(language.upper()) 
#Cuenta cuantas T tiene
print(language.count('t'))
#Te indica si es numerico
print(language.isnumeric())
#Lo pasa a minusculas
print(language.lower())
#Lo manda todo a Mayusculas y despues pregunta si es Mayus (true)
print(language.upper().isupper())
#Preguntamos si una palabra empieza con algo que se especifica
print(language.startswith("py"))