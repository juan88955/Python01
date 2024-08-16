'''
#Calculadora
def suma(a, b):
    # Función para sumar dos números
    return a + b

def resta(a, b):
    # Función para restar el segundo número del primero
    return a - b

def multiplicacion(a, b):
    # Función para multiplicar dos números
    return a * b

def division(a, b):
    # Función para dividir el primer número por el segundo
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
def mostrar_menu():
    # Función para mostrar el menú de opciones
    print("Calculadora Básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        # Salir del programa
        print("Saliendo del programa.")
        break

    if opcion in ["1", "2", "3", "4"]:
        # Solicitar números al usuario
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        # Realizar la operación correspondiente
        if opcion == "1":
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado: {division(num1, num2)}")
    else:
        # Manejar opción no válida
        print("Opción no válida. Inténtalo de nuevo.")



#gestión de contactos
class Contacto:
    def __init__(self, nombre, telefono):
        # Constructor de la clase Contacto
        self.nombre = nombre
        self.telefono = telefono

def mostrar_menu():
    # Función para mostrar el menú de opciones
    print("Gestión de Contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

contactos = []

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        # Salir del programa
        print("Saliendo del programa.")
        break

    if opcion == "1":
        # Agregar un nuevo contacto
        nombre = input("Ingresa el nombre: ")
        telefono = input("Ingresa el teléfono: ")
        contacto = Contacto(nombre, telefono)
        contactos.append(contacto)
        print("Contacto agregado.")
    elif opcion == "2":
        # Mostrar todos los contactos
        for c in contactos:
            print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}")
    elif opcion == "3":
        # Buscar un contacto por nombre
        nombre = input("Ingresa el nombre a buscar: ")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado.")
    elif opcion == "4":
        # Eliminar un contacto por nombre
        nombre = input("Ingresa el nombre a eliminar: ")
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)
                print("Contacto eliminado.")
                break
    else:
        # Manejar opción no válida
        print("Opción no válida. Inténtalo de nuevo.")


#Sistema de Inventario
class Producto:
    def __init__(self, nombre, cantidad, precio):
        # Constructor de la clase Producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def mostrar_menu():
    # Función para mostrar el menú de opciones
    print("Sistema de Inventario")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar cantidad")
    print("5. Eliminar producto")
    print("6. Salir")
    
inventario = []

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "6":
        # Salir del programa
        print("Saliendo del programa.")
        break

    if opcion == "1":
        # Agregar un nuevo producto
        nombre = input("Ingresa el nombre del producto: ")
        try:
            cantidad = int(input("Ingresa la cantidad: "))
            precio = float(input("Ingresa el precio: "))
            producto = Producto(nombre, cantidad, precio)
            inventario.append(producto)
            print("Producto agregado.")
        except ValueError:
            # Manejar errores de entrada no válida
            print("Error: Entrada no válida.")
    elif opcion == "2":
        # Mostrar todos los productos
        for p in inventario:
            print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
    elif opcion == "3":
        # Buscar un producto por nombre
        nombre = input("Ingresa el nombre del producto a buscar: ")
        encontrado = False
        for p in inventario:
            if p.nombre == nombre:
                print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == "4":
        # Actualizar la cantidad de un producto
        nombre = input("Ingresa el nombre del producto a actualizar: ")
        try:
            nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
            for p in inventario:
                if p.nombre == nombre:
                    p.cantidad = nueva_cantidad
                    print("Cantidad actualizada.")
                    break
        except ValueError:
            # Manejar errores de entrada no válida
            print("Error: Entrada no válida.")
    elif opcion == "5":
        # Eliminar un producto por nombre
        nombre = input("Ingresa el nombre del producto a eliminar: ")
        for p in inventario:
            if p.nombre == nombre:
                inventario.remove(p)
                print("Producto eliminado.")
                break
    else:
        # Manejar opción no válida
        print("Opción no válida. Inténtalo de nuevo.")
'''

#Sistema de Gestión de Tareas

# Voy a crear una clase para las tareas
class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "pendiente"  # Todas las tareas empiezan pendientes

# Ahora necesito una lista para guardar todas las tareas
tareas = []

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Mi Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Buscar tarea")
    print("4. Marcar tarea como completada")
    print("5. Borrar tarea")
    print("6. Salir")

# Función para agregar una tarea
def agregar_tarea():
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción de la tarea: ")
    nueva_tarea = Tarea(titulo, descripcion)
    tareas.append(nueva_tarea)
    print("Tarea agregada!")

# Función para ver todas las tareas
def ver_tareas():
    if not tareas:
        print("No hay tareas todavía.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea.titulo} - {tarea.estado}")

# Función para buscar una tarea
def buscar_tarea():
    titulo = input("Título de la tarea a buscar: ")
    for tarea in tareas:
        if tarea.titulo.lower() == titulo.lower():
            print(f"Tarea: {tarea.titulo}")
            print(f"Descripción: {tarea.descripcion}")
            print(f"Estado: {tarea.estado}")
            return
    print("No encontré esa tarea.")

# Función para marcar una tarea como completada
def completar_tarea():
    titulo = input("Título de la tarea completada: ")
    for tarea in tareas:
        if tarea.titulo.lower() == titulo.lower():
            tarea.estado = "completada"
            print("Tarea marcada como completada!")
            return
    print("No encontré esa tarea.")

# Función para borrar una tarea
def borrar_tarea():
    titulo = input("Título de la tarea a borrar: ")
    for tarea in tareas:
        if tarea.titulo.lower() == titulo.lower():
            tareas.remove(tarea)
            print("Tarea borrada!")
            return
    print("No encontré esa tarea.")

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            buscar_tarea()
        elif opcion == "4":
            completar_tarea()
        elif opcion == "5":
            borrar_tarea()
        elif opcion == "6":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    main()
