def ingresar_entero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    while True:
        entrada = input(mensaje)
        try:
            opcion = int(entrada)
            while opcion < minimo or opcion > maximo:
                opcion = int(input(mensaje_error))
            return opcion
        except ValueError:
            print("Error, debe ingresar un número válido")



def cargar_nombres_participantes(participantes: list) -> bool:
    if type(participantes) != list:
        retorno = False

    print("Por favor, ingrese los nombres y apellidos de los 6 participantes")

    i = 0
    while i < 6:
        nombre_apellido = input(f"Ingrese el nombre y apellido del participante #{i + 1}: ")
        retorno = True

        while True:
            if len(nombre_apellido) < 3:
                mensaje_error = "El nombre y apellido debe tener al menos 3 caracteres."
            else:
                espacios = 0
                for caracter in nombre_apellido:
                    if caracter == " ":
                        espacios += 1
                if espacios != 1:
                    mensaje_error = "El nombre y el apellido debe contener solamente 1 espacio."
                else:
                    solo_letras = True
                    for caracter in nombre_apellido:
                        if not (("A" <= caracter <= "Z") or ("a" <= caracter <= "z") or caracter == " "):
                            solo_letras = False
                            break
                    if not solo_letras:
                        mensaje_error = "El nombre sólo puede contener letras y un sólo espacio."
                    else:
                        repetido = False
                        for j in range(i):
                            if nombre_apellido == participantes[j]:
                                repetido = True
                                break
                        if repetido:
                            mensaje_error = "Éste participante ya fue ingresado."
                        else:
                            break  

            print(mensaje_error)
            nombre_apellido = input("Por favor, reingrese el nombre y apellido del participante: ")

        participantes[i] = nombre_apellido
        i += 1

    return retorno