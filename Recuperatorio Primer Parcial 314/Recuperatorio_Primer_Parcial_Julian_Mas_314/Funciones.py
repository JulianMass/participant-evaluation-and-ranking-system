from Inputs import *

def mostrar_menu():
    print("MENÚ DE OPCIONES")
    print("\n1. Cargar nombres y apellidos\n2. Cargar calificaciones\n3. Mostrar calificaciones\n4. Participantes con promedio mayor a 4\n5. Participantes con promedio mayor a 8\n6. Jurado más estricto\n7. Mostrar ganador/a\n8. Buscar participante por apellido\n9. Ordenar array hardcodeado\n10. Salir")


def crear_array(cantidad_elementos:int,valor_inicial:int) -> list:
    array = [valor_inicial] * cantidad_elementos
    return array


def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]

    return matriz


def cargar_calificaciones_participantes(array_participantes:list,matriz_calificaciones:list) -> bool:
    if type(matriz_calificaciones) == list:
        retorno = True

        for fil in range(len(matriz_calificaciones)):
            print(f"Cargando puntuación participante {fil + 1} ({array_participantes[fil]})")
            for col in range(len(matriz_calificaciones[fil])):
                calificacion = ingresar_entero(f"Ingrese la calificación del jurado {col + 1}: ","Error,el número debe estar entre 1 y 10",1,10)
                matriz_calificaciones[fil][col] = calificacion
    else:
        retorno = False

    return retorno


def mostrar_calificacion(lista_participantes:list,matriz_calificaciones:list,indice_participante:int) -> bool:
    if type(lista_participantes) == list and type(matriz_calificaciones) == list:
        retorno = True
        if type(matriz_calificaciones) == list and len(matriz_calificaciones) > 0 and type(lista_participantes) == list and len(lista_participantes) > 0 and type(matriz_calificaciones[indice_participante]) == list:
            cantidad_calificacion_participante = sumar_fila(matriz_calificaciones,indice_participante)
            promedio_calificacion = calcular_promedio(cantidad_calificacion_participante)
            nombre, apellido = separar_nombre_apellido(lista_participantes[indice_participante])
            print(f"Nombre: {nombre}")
            print(f"Apellido: {apellido}")
            print(f"Puntuación jurado 1: {matriz_calificaciones[indice_participante][0]}")
            print(f"Puntuación jurado 2: {matriz_calificaciones[indice_participante][1]}")
            print(f"Puntuación jurado 3: {matriz_calificaciones[indice_participante][2]}")
            print(f"Promedio de notas: {promedio_calificacion}/10\n")
    else:
        retorno = False

    return retorno


def mostrar_calificacion_por_participante(lista_participantes:list,matriz_calificaciones:list) -> bool:
    if type(lista_participantes) == list and type(matriz_calificaciones) == list and (len(lista_participantes) == len(matriz_calificaciones)):
        retorno = True
        for i in range(len(lista_participantes)):
            print(f"Participante {i + 1} \n")
            mostrar_calificacion(lista_participantes,matriz_calificaciones,i)
            print("")
    else:
        retorno = False

    return retorno


def sumar_fila(matriz_calificaciones:list,indice_fila:int) -> int:
    suma = 0
    if type(matriz_calificaciones) == list and indice_fila < len(matriz_calificaciones) and indice_fila >= 0:
            if type(matriz_calificaciones[indice_fila]) == list:
                for col in range(len(matriz_calificaciones[indice_fila])):
                    if type(matriz_calificaciones[indice_fila][col]) == int:
                        suma += matriz_calificaciones[indice_fila][col]

    return suma


def sumar_matriz(matriz_calificaciones:list) -> int:
    suma = 0
    if type(matriz_calificaciones) == list:
        for fil in range(len(matriz_calificaciones)):
            suma += sumar_fila(matriz_calificaciones,fil)

    return suma


def calcular_promedio(valor_parcial:int) -> int | float:
        promedio = round((valor_parcial / 3),2) #Puse 3 porque son la cantidad de jurados que hay

        return promedio


def separar_nombre_apellido(nombre_apellido:str) -> str:
    pos_espacio = -1
    for i in range(len(nombre_apellido)):
        if nombre_apellido[i] == " ":
            pos_espacio = i
            break

    nombre = ""
    for i in range(pos_espacio):
        nombre += nombre_apellido[i]

    apellido = ""
    for i in range(pos_espacio + 1, len(nombre_apellido)):
        apellido += nombre_apellido[i]

    return nombre, apellido


def mostrar_participantes_por_rango_de_promedio(matriz_calificaciones:list,lista_participantes:list,promedio_minimo:int | float,promedio_maximo:int | float) -> bool:
    if type(matriz_calificaciones) == list and len(matriz_calificaciones) > 0 and type(lista_participantes) == list and len(lista_participantes) > 0:
        for i in range(len(matriz_calificaciones)):
            promedio = calcular_promedio_calificaciones(matriz_calificaciones,i)

            if promedio_minimo < promedio <= promedio_maximo:
                mostrar_calificacion(lista_participantes,matriz_calificaciones,i)
                retorno = True
            else:
                retorno = False          
    
    return retorno
            

def calcular_promedio_calificaciones(matriz_calificaciones:list,indice_participante:int) -> int | float:
    cantidad_calificacion_participante = sumar_fila(matriz_calificaciones,indice_participante)
    promedio_calificacion = calcular_promedio(cantidad_calificacion_participante)

    return promedio_calificacion


def sumar_columna(matriz_calificaciones:list,indice_columna:int) -> int | float:
    suma = 0
    if type(matriz_calificaciones) == list:
        for fil in range(len(matriz_calificaciones)):
            if indice_columna < len(matriz_calificaciones[fil]) and indice_columna >= 0 and type(matriz_calificaciones[fil]) == list:
                if type(matriz_calificaciones[fil][indice_columna]) == int or type(matriz_calificaciones[fil][indice_columna]) == float:
                    suma += matriz_calificaciones[fil][indice_columna]
    return suma    

 
def calcular_minimo_columna(matriz_calificaciones:list) -> int:
    bandera = False
    
    if type(matriz_calificaciones) == list:
        for col in range(len(matriz_calificaciones[0])):
            suma = sumar_columna(matriz_calificaciones,col)

            if bandera == False:
                minimo = suma
                bandera = True
            else:
                if suma < minimo:
                    minimo = suma
    
    return minimo


def determinar_jurado_mas_estricto(matriz_calificaciones:list) -> bool:
    if type(matriz_calificaciones) == list:
        retorno = True
        valor_minimo = calcular_minimo_columna(matriz_calificaciones)

        print("El jurado más estricto fue: ")

        for col in range(len(matriz_calificaciones[0])):
            suma = sumar_columna(matriz_calificaciones,col)
            if valor_minimo == suma:
                print(f"Jurado {col + 1}")
    else:
        retorno = False

    return retorno


def mostrar_ganador(matriz_calificaciones:list,lista_participantes:list) -> bool:
    max_promedio = None
    indices_ganadores = []

    if type(matriz_calificaciones) == list and len(matriz_calificaciones) > 0 and type(lista_participantes) == list and len(lista_participantes) > 0:
        retorno = True
        for i in range(len(matriz_calificaciones)):
            promedio = calcular_promedio_calificaciones(matriz_calificaciones,i)

            if max_promedio is None or promedio > max_promedio:
                max_promedio = promedio

        print(f"Promedio más alto: {max_promedio}")

        cantidad_ganadores = 0
        ultimo_ganador = 1

        for i in range(len(matriz_calificaciones)):
            promedio = calcular_promedio_calificaciones(matriz_calificaciones,i)
            if promedio == max_promedio:
                mostrar_calificacion(lista_participantes,matriz_calificaciones,i)
                cantidad_ganadores += 1
                ultimo_ganador = i

        if cantidad_ganadores > 1:
            print("Hubo un empate. Todavía no hay un ganador definitivo hasta poder desempatar")
        else:
            print(f"El/La ganador/a es: {lista_participantes[ultimo_ganador]}")

    else:
        retorno = False

    return retorno


def buscar_participante_por_apellido(lista_participantes: list, matriz_calificaciones: list, apellido_busqueda: str) -> bool:
    if type(matriz_calificaciones) == list and len(matriz_calificaciones) > 0 and type(lista_participantes) == list and len(lista_participantes) > 0:
        encontrados = 0
        retorno = True

        for i in range(len(lista_participantes)):
            nombre, apellido = separar_nombre_apellido(lista_participantes[i])
            if apellido_busqueda in apellido:
                mostrar_calificacion(lista_participantes,matriz_calificaciones,i)
                encontrados += 1
        if encontrados == 0:
            print("No se encontró ningún participante con ese apellido.")
    else:
        retorno = False

    return retorno


def ingresar_apellido() -> str:
    apellido = input("\nIngrese el apellido o parte del apellido a buscar: \n")
    return apellido


def intercambiar_lugares(array:list,izq:int,der:int) -> None:
    if type(array) == list:
        temp = array[izq]
        array[izq] = array[der]
        array[der] = temp     


def ordenar_array_mayor_menor(array:list) -> bool:
    if type(array) == list:
        retorno = True
        for izq in range(len(array) - 1):
            for der in range(izq + 1,len(array)):
                if array[izq] < array[der]:
                    intercambiar_lugares(array,izq,der)     
    else:
        retorno = False
        
    return retorno