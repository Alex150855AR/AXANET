import json
import os
from .cliente import Cliente

class GestorClientes:
    """
    Clase encargada de manejar la persistencia y las operaciones CRUD 
    para los clientes de AXANET.
    """

    def __init__(self, filepath: str = "data/clientes.json"):
        """
        Inicializa el gestor, asegurando que el directorio y archivo existan.
        """
        self.filepath = filepath
        self._asegurar_directorio()
        self.clientes = self._cargar_datos()

    def _asegurar_directorio(self):
        """Crea el directorio y el archivo JSON si no existen."""
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump([], f)

    def _cargar_datos(self) -> list:
        """Lee los datos del archivo JSON en disco."""
        with open(self.filepath, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def _guardar_datos(self):
        """Persiste la lista actual de clientes en el archivo JSON."""
        with open(self.filepath, 'w') as f:
            json.dump(self.clientes, f, indent=4)

    def crear_cliente(self, cliente: Cliente):
        """Añade un nuevo cliente al sistema."""
        self.clientes.append(cliente.to_dict())
        self._guardar_datos()

    def leer_clientes(self) -> list:
        """Devuelve la lista completa de clientes."""
        return self.clientes

    def leer_cliente_por_id(self, id_cliente: str) -> dict:
        """Busca y devuelve un cliente por su ID."""
        for c in self.clientes:
            if c["id"] == id_cliente:
                return c
        return None

    def actualizar_cliente(self, id_cliente: str, nuevos_datos: dict) -> bool:
        """Actualiza los datos de un cliente existente."""
        for c in self.clientes:
            if c["id"] == id_cliente:
                c.update(nuevos_datos)
                self._guardar_datos()
                return True
        return False

    def eliminar_cliente(self, id_cliente: str) -> bool:
        """Elimina un cliente del sistema mediante su ID."""
        clientes_inicial = len(self.clientes)
        self.clientes = [c for c in self.clientes if c["id"] != id_cliente]
        if len(self.clientes) < clientes_inicial:
            self._guardar_datos()
            return True
        return False

    """
    Simulacion de cambio
    """