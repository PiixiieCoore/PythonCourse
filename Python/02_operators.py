### Operadores Artimeticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2)
print(2 ** 3 + 3 - 7 / 1 // 4)
#Aproxima al numero entero mas proximo //
print(10 // 3 )
#Exponente
print(2 ** 3)
#Concatenacion
print("Hola " + "Python" + " Que tal?")
#Concatenando un String con un int parseado a str
print("Hola " + str(5))
#Podemos usar operando por (*) para multiplicar el String
print("Hola " * 5)

#No permite multiplicar un string con float a menos que se convierta en int
my_float = 2.5 * 2
print("Hola " * int(my_float))

## Operadores comparativos ##

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#Comparativa de ordenacion alfabetica (Tiene en cuenta las mayusculas)
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Zola") 
print("aaaa" >= "abaa") #Ordenacion alfabetica por ASCII
print(len("aaaa") >= len("abaa")) #Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

print("xxxxxxxxxx")
## Operadores Logicos ##
#False && False == False
print(3 > 4 and "Hola" > "Python") # (&&)
#False || False == False
print(3 > 4 or "Hola" > "Python") # (||)
# True && True == True
print(3 < 4 and "Hola" < "Python") # (&&)
# True || True == True
print(3 < 4 or "Hola" < "Python") # (||)

print(3 < 4 or ("Hola" < "Python" and 4 == 4)) #Con parentesis los prioriza

print(not(3 > 4)) # (!) #No False == True