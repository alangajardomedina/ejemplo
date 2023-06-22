#funciones del ejercicio:
import os
import msvcrt
import time

def mostrar_menu():
    os.system('cls')
    print("""RESTAURANT
    1. Ver restaurant
    2. Reservar mesa
    3. Ver carta
    4. Pagar
    5. Cancelar reserva
    6. Salir""")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4,5,6):
                #no se usa break en una función de validación break
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

#en el archivo de funciones crear el arreglo:
import numpy
restaurant = numpy.zeros((3,3), int)

lista_ruts = []
lista_nombres = []
lista_correos = []
lista_filas = []
lista_columnas = []

def ver_restaurant():
    os.system('cls')
    print("VER RESTAURANT\n")
    contador = 1
    for x in range(3):
        print(f"mesa para {(x+1)*2}:",end=" ")
        for y in range(3):
            print(f"Mesa {contador}:",restaurant[x][y], end=" ")
            contador += 1
        print()
    print("\npresione una tecla para continuar...")
    msvcrt.getch()

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! RUT INCORRECTO! DEBE ETAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
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

def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de personas(1-6): "))
            if cantidad >= 1 and cantidad <= 6:
                return cantidad
            else:
                print("ERROR! LA CANTIDAD DE PERSONAS DEBE ESTAR ENTRE 1 y 6!")
        except:
            print("ERROR! DEBE INGREAR UN NÚMERO ENTERO")

def validar_mesa():
    while True:
        try:
            mesa = int(input("Ingrese número de mesa(1-9): "))
            if mesa >= 1 and mesa <= 9:
                return mesa
            else:
                print("ERROR! NÚMERO DE MESA INCORRECTO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def reservar():
    os.system('cls')
    print("RESERVAR MESA\n")
    rut = validar_rut()
    nombre = validar_nombre()
    correo = validar_correo()
    cant_personas = validar_cantidad()
    #vamos a recorrer el restaurant y mostrar mesas disponibles:
    contador = 1
    print("MESAS DISPONIBLES:", end=" ")
    for x in range(3):
        for y in range(3):
            if restaurant[x][y] == 0:
                if cant_personas <= 2:
                    print(contador, end=" ")
                elif cant_personas >= 3 and cant_personas <= 4 and x in(1,2):
                    print(contador, end=" ")
                elif cant_personas >=5 and cant_personas <= 6 and x == 2:
                    print(contador, end=" ")
            contador+=1
    mesa_elegida = validar_mesa()
    #vamos a ocupar la mesa:
    contador = 1
    for x in range(3):
        for y in range(3):
            if contador == mesa_elegida:
                restaurant[x][y] = 1
                lista_ruts.append(rut)
                lista_nombres.append(nombre)
                lista_correos.append(correo)
                lista_filas.append(x)
                lista_columnas.append(y)
                print("RESERVA EFECTUADA CON ÉXITO!")
                time.sleep(3)
            contador+=1
    print("\npresione una tecla para continuar...")
    msvcrt.getch()
