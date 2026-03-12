import re

class Cliente:
    """
    Representa la entidad Cliente en el sistema AXANET.
    Aplica validaciones (Value Objects) para asegurar la integridad de los datos.
    """

    def __init__(self, id_cliente: str, nombre: str, correo: str, telefono: str, direccion: str):
        """
        Inicializa un nuevo cliente con sus datos básicos.
        """
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = self._validar_correo(correo)
        self.telefono = self._validar_telefono(telefono)
        self.direccion = direccion

    def _validar_correo(self, correo: str) -> str:
        """Valida que el correo tenga un formato correcto."""
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(patron, correo):
            raise ValueError("Formato de correo electrónico inválido.")
        return correo

    def _validar_telefono(self, telefono: str) -> str:
        """Valida que el teléfono contenga al menos 10 dígitos numéricos."""
        if not telefono.isdigit() or len(telefono) < 10:
            raise ValueError("El teléfono debe contener al menos 10 dígitos numéricos.")
        return telefono

    def to_dict(self) -> dict:
        """Convierte la entidad Cliente en un diccionario para su serialización."""
        return {
            "id": self.id_cliente,
            "nombre": self.nombre,
            "correo": self.correo,
            "telefono": self.telefono,
            "direccion": self.direccion
        }

    """
    Simulacion decambio
    """