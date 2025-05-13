inventario = []
# Muestra menu
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar producto al inventario")
    print("2. Ver inventario")
    print("3. Eliminar producto del inventario")
    print("4. Salir")

def agregar_producto():
    while True:
        print("\n--- AGREGAR PRODUCTO ---")
        nombre = input("Ingrese el nombre del producto: ")
        
        # Validación del precio
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio <= 0:
                    print("El precio debe ser mayor que cero.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el precio.")
        
        producto = {
            "id": len(inventario) + 1,
            "nombre": nombre,
            "precio": precio
        }
        
        inventario.append(producto)
        print(f"\nProducto '{nombre}' agregado con éxito! (ID: {producto['id']})")
        
        continuar = input("\n¿Desea agregar otro producto? (s/n): ").lower()
        if continuar != 's':
            break

def ver_inventario():
    while True:
        print("\n--- INVENTARIO ACTUAL ---")
        if not inventario:
            print("El inventario está vacío.")
        else:
            print("{:<5} {:<20} {:<10}".format("ID", "NOMBRE", "PRECIO"))
            print("-" * 35)
            for producto in inventario:
                print("{:<5} {:<20} ${:<10.2f}".format(
                    producto['id'], 
                    producto['nombre'], 
                    producto['precio']
                ))
        
        opcion = input("\nPresione 'm' para volver al menú principal: ").lower()
        if opcion == 'm':
            break

def eliminar_producto():
    while True:
        print("\n--- ELIMINAR PRODUCTO ---")
        if not inventario:
            print("El inventario está vacío. No hay productos para eliminar.")
            input("\nPresione Enter para volver al menú principal...")
            break
        
        print("\nProductos disponibles:")
        print("{:<5} {:<20} {:<10}".format("ID", "NOMBRE", "PRECIO"))
        print("-" * 35)
        for producto in inventario:
            print("{:<5} {:<20} ${:<10.2f}".format(
                producto['id'], 
                producto['nombre'], 
                producto['precio']
            ))
        
        try:
            id_eliminar = int(input("\nIngrese el ID del producto a eliminar (0 para cancelar): "))
            
            if id_eliminar == 0:
                break
                
            producto_encontrado = None
            for producto in inventario:
                if producto['id'] == id_eliminar:
                    producto_encontrado = producto
                    break
            
            if producto_encontrado:
                confirmacion = input(f"¿Está seguro de eliminar '{producto_encontrado['nombre']}'? (s/n): ").lower()
                if confirmacion == 's':
                    inventario.remove(producto_encontrado)
                    print("Producto eliminado con éxito!")
                else:
                    print("Eliminación cancelada.")
            else:
                print("No se encontró un producto con ese ID.")
            
            continuar = input("\n¿Desea eliminar otro producto? (s/n): ").lower()
            if continuar != 's':
                break
                
        except ValueError:
            print("Por favor, ingrese un ID numérico válido.")

def main():
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE INVENTARIO")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            
            if opcion == 1:
                agregar_producto()
            elif opcion == 2:
                ver_inventario()
            elif opcion == 3:
                eliminar_producto()
            elif opcion == 4:
                print("\nGracias por usar el sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
                
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()