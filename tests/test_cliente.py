import pytest
from src.cliente import Cliente

def test_creacion_cliente_valido():
    """Prueba que un cliente se crea correctamente con datos válidos."""
    cliente = Cliente("123", "Juan Perez", "juan@axanet.com", "1234567890", "Calle Falsa 123")
    assert cliente.nombre == "Juan Perez"
    assert cliente.correo == "juan@axanet.com"

def test_correo_invalido():
    """Prueba la validación de fallo para correos incorrectos."""
    with pytest.raises(ValueError):
        Cliente("123", "Juan Perez", "correo-malo.com", "1234567890", "Calle Falsa")

def test_telefono_invalido():
    """Prueba la validación de fallo para teléfonos demasiado cortos o con letras."""
    with pytest.raises(ValueError):
        Cliente("123", "Juan Perez", "juan@axanet.com", "12345", "Calle Falsa")
    
    with pytest.raises(ValueError):
        Cliente("123", "Juan Perez", "juan@axanet.com", "letras1234", "Calle Falsa")
