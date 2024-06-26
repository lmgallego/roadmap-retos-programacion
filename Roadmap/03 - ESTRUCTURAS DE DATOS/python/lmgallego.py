
# Estructura de datos

# LISTAS

nombres = ["Luisma", "Pedro", "Juan"] # Estructura de datos con strincs
numeros = [1, 2, 3, 4] # Estructura de datos numérica

nombres[1] # Acceder al índice correspondiente
nombres[0] = "Juan" # Sustituimos el índice 0 por otro string, esto elimina el índice anterior
numeros.append(6.7) # Agregamos un número, se agregará al final de la lista
numeros.append([9, 10]) # Agregamos una lista dentro de la lista original
nombres.append(["Jose", "Enrique"]) # Agregamos múltiples strings a la lista, se añaden al final
nombres.insert(1, "Antonio") # Agrega en el índice 1 el strint Antonio

# Borrado listas
nombres.remove("Juan") # Eliminación del primer registro encontrado en la lista, si hay otro se mantendrá
nombres.pop() # Elimina el último registro de la lista
nombres.pop(3) # Elimina el índice 3 de la lista
nombres.clear() # Limpia completamente una lista

# Búsqueda lista
numeros.count(2) # Indica cuantas veces está el valor en la lista
numeros.index(1) # Nos indica que elemento está en el índice 1
2 in numeros # Devuelve True o False si el elemento está en la lista

# TUPLAS 
colores = () # Tupla vacía
colores ("Azul", "Verde", "Rojo", "Amarillo") # Creación de una tupla con elementos

colores[2] # Accede al índice que le pongas entre corchetes

# DICCIONARIOS

edad = {"Pedro": 24, "Juan": 15, "Ana": 30} # Diccionario clave-valor
edad["Pedro"] # Acceso al valor a través de la clave
edad.get("Ana") # Devuelve el valor de Ana si no existe nos devolverá None
edad["Jose"] = 67 # Añade un nuevo elemento clave-valor al diccionario
'Jose' in edad # Nos comprueba si pertenece a una lista, devuelve True o False
"Alvaro" not in edad # Nos devolverá True o False si se cumple la condición
len(edad) # Longitud de un diccionario
edad # Obtener todos los datos del diccionario
edad.keys() # Obtener todas las claves de un diccionario
edad.values() # Obtener todos los valroes de un diccionario
edad.items() # Obtener los pares clave-valor del diccionario
del edad('Pedro') # Borrar por clave
edad.pop('Ana') # Extraer elemento del diccionario
edad.clear() # Elimina el diccionario completo

# CONJUNTOS

conjunto = {21, 45, 67, 89} # Creacion de conjunto (valores únicos y sin orden)
set("hola") # Convierte el dato en un conjunto h,o,l,a
conjunto.add(40) # Añade al conjunto sin saber la posición
conjunto.remove(21) # Elimina el valor del conjunto
len(conjunto) # Número de elementos del conjunto




agenda = dict() 

def insertar():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre.lower()] = telefono
    print(f"\nContacto {nombre} insertado correctamente")

def buscar():
    while True:
        nombre = input("\nNombre a buscar (0 - Salir): ")
        if nombre == '0':
            return
        elif nombre in agenda:
            print(f"\nEl telefono de {nombre.capitalize()} es {agenda[nombre]}")
        else:
            print(f"\nEl contacto {nombre.capitalize()} no existe")
        
def eliminar():
    for x, y in agenda.items():
        print(x, y)
    nombre_a_eliminar = input("\nIntroduzca contacto a eliminar (0 - Salir): ")
    if nombre_a_eliminar == '0':
        return
    elif nombre_a_eliminar in agenda.keys():
        agenda.pop(nombre_a_eliminar)
        print(f"\nEl registro ha sido eliminado correctamente")
    else:
        print("No se encuentra ningún registro en la agenda")
        menu()
        
def actualizar():
    for x, y in agenda.items():
        print(x, y)
    while True:
        reg_actualizar = input("\nIntroduzca registro a actualizar (0 - Salir): ").lower()
        if reg_actualizar == '0':
            return
        elif reg_actualizar in agenda.keys():
            tel_nuevo = input("\nIntroduce teléfono nuevo: ")
            agenda[reg_actualizar] = tel_nuevo
            print("\nRegistro actualizado correctamente")
            return
        else:
            print("\nRegistro no")
    

def menu():
    while True:
        print("\n--- Agenda Personal ---")
        print('''\nOpciones:
                1. Buscar
                2. Insertar
                3. Actualizar
                4. Eliminar
                0. Salir
                ''')
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            buscar()
        elif opcion == 2:
            insertar()
            
        elif opcion == 3:
            actualizar()
        elif opcion == 4:
            eliminar()
        elif opcion == 0:
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        
menu()