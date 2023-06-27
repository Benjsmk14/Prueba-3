import numpy
import FUNCIONES as fn
import os
import time
import msvcrt



while True:
    print("""   
        1.Ver Guarderia
        2.Ingresar Mascota
        3.Buscar Mascota
        4.Retirar Mascota
        5.Salir
    """)
    opcion = fn.validar_opcion()
    if opcion == 1:
        fn.ver_guarderia()
    elif opcion == 2:
        fn.ingresar_mascota()
    elif opcion == 3:
        fn.buscar_mascota()
    elif opcion == 4:
        pass
    else:
        break



