#programa para guardar/modificar/borrar/ver datos de estudiantes
#comparado con la primera version este usa un diccionario para que su funcionamiento sea mas eficiente
estudiantes = []

contador_id = 0

def agregar_datos():
    global contador_id
    
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido_agregar = input("Ingrese el apellido del estudiante: ")
    edad_agregar = int(input("Ingrese la edad: "))
    dni_agregar = int(input("Ingrese el dni: "))
    curso_agregar = int(input("Ingrese el curso del estudiante: "))
    
    
    estudiante = {
        "nombre": nombre,
        "apellido": apellido_agregar,
        "edad": edad_agregar,
        "dni": dni_agregar,
        "curso": curso_agregar,
        "identificador": contador_id
    }
    
    estudiantes.append(estudiante)
    contador_id =contador_id + 1

def modificar_datos(identificador_respuesta):
    for estudiante in estudiantes:
        if estudiante["identificador"] == identificador_respuesta:
            print("¿Qué desea modificar?")
            print("1: Nombre del estudiante")
            print("2: Apellido")
            print("3: Edad")
            print("4: DNI")
            print("5: Curso")
            print("6: Cancelar")
            opcion_modificar = int(input("Ingrese opción: "))
            
            if opcion_modificar == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                estudiante["nombre"] = nuevo_nombre
            elif opcion_modificar == 2:
                nuevo_apellido = input("Ingrese el nuevo apellido: ")
                estudiante["apellido"] = nuevo_apellido
            elif opcion_modificar == 3:
                nueva_edad = int(input("Ingrese la nueva edad: "))
                estudiante["edad"] = nueva_edad
            elif opcion_modificar == 4:
                nuevo_dni = int(input("Ingrese el nuevo DNI: "))
                estudiante["dni"] = nuevo_dni
            elif opcion_modificar == 5:
                nuevo_curso = int(input("Ingrese el nuevo curso: "))
                estudiante["curso"] = nuevo_curso
            elif opcion_modificar == 6:
                print("Cancelando modificación")
            else:
                print("Opción ingresada no válida")

def borrar_datos(identificador_respuesta):
    for estudiante in estudiantes:
        if estudiante["identificador"] == identificador_respuesta:
            estudiantes.remove(estudiante)
            print(f"Estudiante con identificador {identificador_respuesta} borrado.")

while True:
    print("Bienvenido! Presione:")
    print("1 para agregar datos")
    print("2 para modificar datos")
    print("3 para ver la información de estudiantes")
    print("4 para borrar datos")
    print("5 para salir de la aplicación")
    
    opcion = int(input("Ingrese su opción: "))
    
    if opcion == 1:
        agregar_datos()
        
    elif opcion == 2:
        identificador_respuesta = int(input("Ingrese el identificador del alumno que desea modificar: "))
        modificar_datos(identificador_respuesta)
        
    elif opcion == 3:
        print("Información de estudiantes:")
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Apellido: {estudiante['apellido']}")
            print(f"Edad: {estudiante['edad']}")
            print(f"DNI: {estudiante['dni']}")
            print(f"Curso: {estudiante['curso']}")
            print(f"Identificador: {estudiante['identificador']}")
            print("___________________________")
        
    elif opcion == 4:
        identificador_respuesta = int(input("Ingrese el identificador del alumno que desea borrar: "))
        borrar_datos(identificador_respuesta)
        
    elif opcion == 5:
        print("Programa finalizado")
        break
    
    else:
        print("Número ingresado no válido. Por favor, intente de nuevo.")