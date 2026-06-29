# Funciones de Validación
def validar_titulo(titulo):
    # Retorna True si el título no está vacío y no contiene solo espacios
    return bool(titulo and titulo.strip())

def validar_copias(copias):
    # Retorna True si es un número entero mayor o igual a cero
    try:
        valor = int(copias)
        return valor >= 0
    except ValueError:
        return False

def validar_prestamo(prestamo):
    # Retorna True si es un número entero mayor a cero
    try:
        valor = int(prestamo)
        return valor > 0
    except ValueError:
        return False

# Funciones del Menú
def mostrar_menu():
    # Muestra las opciones sin recibir ni retornar nada
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("====================================")

def leer_opcion():
    # Lee y retorna la opción validada del usuario
    while True:
        opcion = input("Ingrese una opción (1-6): ")
        if opcion in ['1', '2', '3', '4', '5', '6']:
            return int(opcion)
        print("Opción inválida. Por favor, ingrese un número del 1 al 6.")

# Funciones de Operación
def agregar_libro(biblioteca):
    titulo = input("Ingrese el título del libro: ")
    copias_str = input("Ingrese la cantidad de copias disponibles: ")
    prestamo_str = input("Ingrese el período de préstamo (en días): ")

    # Se llama a las funciones de validación separadas. Los errores se muestran aquí.
    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío ni ser solo espacios en blanco.")
        return
    if not validar_copias(copias_str):
        print("Error: La cantidad de copias debe ser un número entero mayor o igual a cero.")
        return
    if not validar_prestamo(prestamo_str):
        print("Error: El período de préstamo debe ser un número entero mayor que cero.")
        return

    # Si todo es válido, se crea el diccionario y se agrega a la lista general
    nuevo_libro = {
        "titulo": titulo,
        "copias": int(copias_str),
        "prestamo": int(prestamo_str),
        "disponible": False  # Se asigna False al registrar, según requerimiento
    }
    biblioteca.append(nuevo_libro)
    print("Libro registrado exitosamente.")

def buscar_libro(biblioteca, titulo_buscar):
    # Recorre la lista y retorna la posición, o -1 si no existe
    for i in range(len(biblioteca)):
        if biblioteca[i]["titulo"] == titulo_buscar:
            return i
    return -1

def actualizar_disponibilidad(biblioteca):
    # Recorre la lista y actualiza el campo "disponible" según las copias
    for libro in biblioteca:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

# Programa Principal
def main():
    # La colección general inicia como una lista vacía
    biblioteca = []
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            agregar_libro(biblioteca)
            
        elif opcion == 2:
            titulo = input("Ingrese el título del libro a buscar: ")
            posicion = buscar_libro(biblioteca, titulo)
            
            # El programa principal decide qué hacer con el valor retornado
            if posicion != -1:
                libro = biblioteca[posicion]
                print(f"\nLibro encontrado en la posición {posicion}:")
                print(f"Título: {libro['titulo']} | Copias: {libro['copias']} | Préstamo: {libro['prestamo']} días | Disponible: {libro['disponible']}")
            else:
                print("El libro no se encuentra registrado.")
                
        elif opcion == 3:
            titulo = input("Ingrese el título del libro que desea eliminar: ")
            posicion = buscar_libro(biblioteca, titulo)
            
            if posicion != -1:
                biblioteca.pop(posicion)
                print("El libro fue eliminado con éxito.")
            else:
                print(f"El libro '{titulo}' no se encuentra registrado.")
                
        elif opcion == 4:
            actualizar_disponibilidad(biblioteca)
            print("La disponibilidad de todos los libros ha sido actualizada.")
            
        elif opcion == 5:
            # Primero actualiza la disponibilidad haciendo el llamado a la función anterior
            actualizar_disponibilidad(biblioteca)
            
            print("\n=== LISTA DE LIBROS ===")
            if len(biblioteca) == 0:
                print("No hay libros registrados en el sistema.")
            else:
                # Recorre la lista mostrando los datos con el formato de salida exigido
                for libro in biblioteca:
                    estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
                    print(f"Título: {libro['titulo']}")
                    print(f"Copias: {libro['copias']}")
                    print(f"Préstamo: {libro['prestamo']}")
                    print(f"Estado: {estado}")
                    print("****************************************")
                    
        elif opcion == 6:
            # Termina la ejecución de forma limpia
            print("Gracias por usar el sistema. Vuelva Pronto")
            break

# Ejecución del programa
if __name__ == "__main__":
    main()
