## Funciones ##

#Definicion de una funcion
def my_function():
    print("Esto es una funcion")

#Si se llama muchas veces se ejecuta la funcion
my_function()
my_function()

#Funciones que requieren dos valores
def sum_two_values(first_value, second_value):
    print(first_value + second_value)

#En la llamada de la funcion requeriremos los valores
sum_two_values(5, 7)
sum_two_values(123, 6113)
#concatenar cadenas de texto dentro de la funcion definida
sum_two_values("5","5")
#asignar a una variable el resultado y hacerle un print 
#generar un none
my_result = sum_two_values(1,2)
print(my_result)

#funcion que recibe parametros y retorna los parametros
def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

def print_name(name, lastname):
    print(f"{name} {lastname}")

#Reordenar los parametros de la funcion
print_name(lastname= "Hernandez", name= "Uriel")

#Valor de parametro por defecto
def print_name_with_default(name, lastname, alias = "Sin alias"):
    print(f"{name} {lastname} {alias}")
#No requiere de ingresar el tercer parametro
print_name_with_default("Uriel", "Hernandez")
#Si le ingresas tercer parametro lo cambia 
print_name_with_default("Uriel", "Hernandez", "Piixiie")

#N cantidad de parametros (con el asterisco)
def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hola", "Python", "Piixiie", "...")
print_texts("Hola")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "Piixiie", "...")
print_upper_texts("Hola")

