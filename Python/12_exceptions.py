### Manejo de excepciones ###

#Si no manejamos un error el programa se cierra, es por ello que usamos excepciones
'''
Try: Corre el codigo que puede generar error
Exception: Ejecuta codigo cuando existe la excepcion
Else: Sino hay excepcion ejecuta esta bloque
Finally: Siempre ejecuta este bloque (si o si)
'''
#Este print genera error porque un int no puede sumar un str
#print(5 + "5")

#Comentar y descomentar numberTwo string
numerOne = 5
numberTwo = 1 
numberTwo = "1"

#Try except:
try:
    print(numerOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

#A diferencia de try-except, if-else se podria utilizar en manejo de errores muy concretos
print("####################################################")
#Try except else:
try:
    print(numerOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecucion continua correctamente")

print("########################################################")
#Try except else finally:
try:
    print(numerOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecucion continua correctamente")
finally:
    print("La ejecucion continua...")

#Si hay un try SIEMPRE debe de ir un except
#Opcionalmente puede tener un else y un finally

# Exceptiones por tipo: 
try:
    print(numerOne + numberTwo)
    print("No se ha producido un error")
    #En este caso es de tipo TypeError
except TypeError:
    print("Se ha producido un TypeError")
    #Se puede poner varios except para diferentes tipos en este caso ValueError
except ValueError:
    print("Se ha producido un ValueError")

#Captura de informacion de la excepcion
#Dar mas informacion al usuario sobre el error
try:
    print(numerOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
    #Si el error no es ValueError nos manda al bloque except Exception (excepcion generica, cualquiera)
    #Si queremos capturar la info de la except metemos el Exception con su variable (as 'cualquierCosa')
except Exception as error:
    print(error)