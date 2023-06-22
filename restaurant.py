#EJERCICIO PRINCIPAL:
import funciones_restaurant as fn

while True:
    fn.mostrar_menu()
    opcion = fn.validar_opcion()
    if opcion==1:
        fn.ver_restaurant()
    elif opcion==2:
        fn.reservar()
    elif opcion==3:
        pass
        #fn.carta()
    elif opcion==4:
        pass
        #fn.pagar()
    elif opcion==5:
        pass
        #fn.cancelar()
    else:
        print("GRACIAS, ADIOS!")
        break