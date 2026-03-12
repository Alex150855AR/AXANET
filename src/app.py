import uuid
from src.cliente import Cliente
from src.gestor import GestorClientes

def mostrar_menu():
    """Muestra el menú interactivo en la consola."""
    print("\n" + "="*40)
    print("   AXANET - GESTIÓN DE CLIENTES (POO)")
    print("="*40)
    print("1. Añadir nuevo cliente")
    print("2. Listar clientes")
    print("3. Visualizar cliente por ID")
    print("4. Modificar datos de cliente")
    print("5. Eliminar cliente")
    print("6. Salir")
    print("="*40)
    return input("Seleccione una opción (1-6): ")

def main():
    """Función principal que ejecuta el bucle de la aplicación CLI."""
    gestor = GestorClientes()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            print("\n--- NUEVO CLIENTE ---")
            id_cliente = str(uuid.uuid4())[:8] # Genera ID corto
            nombre = input("Nombre: ")
            correo = input("Correo electrónico: ")
            telefono = input("Teléfono (10 dígitos): ")
            direccion = input("Dirección: ")
            
            try:
                cliente = Cliente(id_cliente, nombre, correo, telefono, direccion)
                gestor.crear_cliente(cliente)
                print(f"✅ Cliente creado exitosamente con ID: {id_cliente}")
            except ValueError as e:
                print(f"❌ Error de validación: {e}")
                
        elif opcion == '2':
            print("\n--- LISTADO DE CLIENTES ---")
            clientes = gestor.leer_clientes()
            if not clientes:
                print("No hay clientes registrados.")
            else:
                for c in clientes:
                    print(f"[{c['id']}] {c['nombre']} | {c['correo']} | {c['telefono']}")
                    
        elif opcion == '3':
            id_cliente = input("\nIngrese el ID del cliente: ")
            c = gestor.leer_cliente_por_id(id_cliente)
            if c:
                print("\n--- DATOS DEL CLIENTE ---")
                for key, value in c.items():
                    print(f"{key.capitalize()}: {value}")
            else:
                print("❌ Cliente no encontrado.")
                
        elif opcion == '4':
            id_cliente = input("\nIngrese el ID del cliente a modificar: ")
            c = gestor.leer_cliente_por_id(id_cliente)
            if c:
                print("Deje el campo en blanco para no modificarlo.")
                nombre = input(f"Nuevo nombre ({c['nombre']}): ")
                telefono = input(f"Nuevo teléfono ({c['telefono']}): ")
                
                nuevos_datos = {}
                if nombre.strip(): nuevos_datos['nombre'] = nombre
                if telefono.strip(): nuevos_datos['telefono'] = telefono
                
                if gestor.actualizar_cliente(id_cliente, nuevos_datos):
                    print("✅ Cliente actualizado.")
            else:
                print("❌ Cliente no encontrado.")
                
        elif opcion == '5':
            id_cliente = input("\nIngrese el ID del cliente a eliminar: ")
            if gestor.eliminar_cliente(id_cliente):
                print("✅ Cliente eliminado del sistema.")
            else:
                print("❌ Cliente no encontrado.")
                
        elif opcion == '6':
            print("Saliendo del sistema AXANET...")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
