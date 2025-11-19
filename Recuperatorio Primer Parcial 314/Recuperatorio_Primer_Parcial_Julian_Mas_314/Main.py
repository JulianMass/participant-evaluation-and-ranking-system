from Funciones import *
from Inputs import *
import os

lista_participantes = crear_array(6,"")
matriz_calificaciones = crear_matriz(6,3,None) 
bandera_participantes_cargados = False
bandera_calificaciones_cargadas = False
mensaje_error = "Primero debe cargar los participantes y sus calificaciones para poder continuar\n"
array_numeros = [7,4,9,1,5,2]


while True:
    mostrar_menu()
    opcion = ingresar_entero("\nSeleccione una opción (1-10): ","\nReingrese la opción (1-10): ",1,10)

    if opcion == 1:
        os.system("cls")
        if cargar_nombres_participantes(lista_participantes) == True:
            print("\nParticipantes cargados con éxito!\n")
            bandera_participantes_cargados = True
        else:
            print("Ocurrió un error.")    
    elif opcion == 2:
        os.system("cls")
        if bandera_participantes_cargados == False:
            print("Primero debe cargar los participantes para poder continuar\n")
        else:
            if cargar_calificaciones_participantes(lista_participantes,matriz_calificaciones) == True:
                print("Calificaciones cargadas con éxito!\n")
                bandera_calificaciones_cargadas = True
            else:
                print("Ocurrió un error.")
    if opcion == 3:
        if bandera_participantes_cargados == True and bandera_calificaciones_cargadas == True:
            mostrar_calificacion_por_participante(lista_participantes,matriz_calificaciones)
        else:
            print(mensaje_error)
    elif opcion == 4:
        if bandera_participantes_cargados == True and bandera_calificaciones_cargadas == True:
            if mostrar_participantes_por_rango_de_promedio(matriz_calificaciones,lista_participantes,4,10) == False:
                print("No hay participantes con promedio mayor a 4")
        else:
            print(mensaje_error)
    elif opcion == 5:
        if bandera_participantes_cargados == True and bandera_calificaciones_cargadas == True:
            if mostrar_participantes_por_rango_de_promedio(matriz_calificaciones,lista_participantes,8,10) == False:
                print("No hay participantes con promedio mayor a 8")
        else:
            print(mensaje_error)             
    elif opcion == 6:
        if bandera_participantes_cargados == True and bandera_calificaciones_cargadas == True:
            determinar_jurado_mas_estricto(matriz_calificaciones)
        else:
            print(mensaje_error)
    elif opcion == 7:
        if bandera_participantes_cargados == True and bandera_calificaciones_cargadas == True:
            mostrar_ganador(matriz_calificaciones,lista_participantes)
        else:
            print(mensaje_error)
    elif opcion == 8:
        if bandera_participantes_cargados == True and bandera_calificaciones_cargadas == True:
            apellido = ingresar_apellido()
            buscar_participante_por_apellido(lista_participantes,matriz_calificaciones,apellido)
        else:
            print(mensaje_error)
    elif opcion == 9:
        print(f"Lista antes de ordenamiento: {array_numeros}")
        ordenar_array_mayor_menor(array_numeros)
        print(f"Lista después de ordenamiento: {array_numeros}")
    elif opcion == 10:
        print("Saliendo...")
        break 
