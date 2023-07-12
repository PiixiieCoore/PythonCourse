### Clases ###

#La clase se definen con Camel Case
class MyEmptyPerson:
    pass
#Pass evita que de error el codigo (fuerza a la clase a no mostrar mensaje de error)
#Se puede imprimir la clase con o sin parentesis
print(MyEmptyPerson)
print(MyEmptyPerson())

#Podemos crear metodo contructor con __init__
class Person:
    def __init__(self, name, lastname):
        #El primer valor (a lado del self) indica el atributo
        #El segundo valor indica el parametro del metodo contructor
        self.name = name
        self.lastname = lastname
#Para poder hacer uso de la clase es necesario ingresar valores
#Con sus parametros y asi poder imprimirlos
my_person = Person("Uriel", "Hernandez")
print(my_person.name)
#Una vez instanciado el objeto se puede imprimir sus valores
print (f"{my_person.name} {my_person.lastname}")

#Se puede colocar valores por defecto dentro del constructor
'''
class Person:
    def __init__(self):
        self.name = "Uriel"
        self.lastname = "Hernandez"
my_person = Person()
print(f"{my_person.name} {my_person.lastname}")
'''

#Podemos crear un metodo constructor que su propiedad este unida a otras
class SecondPerson:
    #Podemos agregar atributos a los parametros del contructor
    #que sean por defecto: ejemplo: def __init__ (self, name, lastname, alias ="sin alias")
    #a la hora de instanciar un objeto nuevo este valor puede modificarse
    def __init__(self, name, lastname):
        self.fullname = f"{name} {lastname}" #Propiedad publica
#Podemos crear metodos que posteriormente se pueden llamar para su uso
    def walk(self):
        print(f"{self.fullname} esta caminando")
my_second_person = SecondPerson("Piixiie", "Coore")
print(my_second_person.fullname)
my_second_person.walk()

#Para definir atributos privados de las clases se colocan con dos guiones bajos despues del self
#Ejemplo: self.__name
#Para acceder a ellos es necesario un get
'''
def get_name (self):
    return self.__name #propiedad privada
'''
#Hacerlo privado implica ya no poder modificar el valor colocado
#print(persona.get_name())
