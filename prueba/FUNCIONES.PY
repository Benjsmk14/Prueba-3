import numpy
import os
import time
import msvcrt

guarderia = numpy.zeros((2,5),int)

lista_rut = []
lista_Habitaciones = []
lista_mascota = []


def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_opcionH():
    while True:
        try:
            habitacion = int(input("Ingrese la habitacion que desea reservar: "))
            if habitacion >= 1 and habitacion <= 10:
                lista_Habitaciones.append(habitacion)
                return habitacion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                lista_rut.append(rut)
                return rut
            else:
                print("ERROR! EL RUT DEBE TENER 7 DIGITOS !")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre del dueño: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@" in correo:
            return correo
        else:
            print("ERROR! CORREO INCORRECTO!")


def validar_mascota():
    while True:
        mascota = input("Ingrese nombre de mascota: ")
        if len(mascota.strip()) >= 3 and mascota.isalpha():
            lista_mascota.append(mascota)
            return mascota
        else:
            print("ERROR! EL NOMBRE DE SU MASCOTA DEBE TENER AL MENOS 3 LETRAS!")

def validar_telefono():
    while True:
        try:
            telefono = int(input("Ingrese telfono"))
            if len(str(telefono)) == 9:
                return telefono
            else:
                print("ERROR! EL TELEFONO DEBE TENER 9 NUMEROS!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_dias():
    while True:
        try:
            cantidad_dias = int(input("Ingrese cantidad de dias que permanecera su mascota en la guarderia: "))
            if cantidad_dias >= 1:
                return cantidad_dias
            else:
                print("ERROR! Debe ingresar una cantidad de dias superior a 1")
        except:
            print("ERROR! Debe ingresar números enteros!")
def ver_guarderia():
    contador = 1
    print("\t\t\tGuarderias disponibles \n(Si esta marcada como 0 esta disponible. Si esta marcada con 1 esta ocupada)")
    print(" ")
    for x in range(2):
        for y in range(5):
            print("Habitacion",contador,guarderia[x][y], end="|")
            contador += 1
        print(" ")

def reservar_habitacion(validar_habitacionh):
                contador = 1
                for x in range(2):
                    for y in range(5):
                        contador +=1 
                        if validar_habitacionh == contador:
                            guarderia[x][y] = 1  
    
def ingresar_mascota():
     validar_rut()
     validar_nombre()
     validar_mascota()
     validar_dias()
     ver_guarderia()
     validar_opcionH()
     reservar_habitacion(validar_opcionH)
     print("Habitacion reservada con exito!")
     return
  



def buscar_mascota():
    validar_rut()
    if validar_rut() not in lista_rut:
        print("Usted no ha ingresado ninguna mascota a la guarderia")
        return
    for x in range (lista_rut):
        if 

    

     

