AXANET - Sistema de Gestión de Clientes (Migración POO)

Descripción del Proyecto

Este proyecto forma parte de la iniciativa de modernización tecnológica de la empresa de manufactura AXANET. Consiste en la migración de un sistema heredado (scripts de Bash/PowerShell) hacia una arquitectura robusta desarrollada en Python.

El sistema implementa Programación Orientada a Objetos (POO) y principios de Domain-Driven Design (DDD) para gestionar un sistema CRUD (Create, Read, Update, Delete) de clientes. La persistencia de los datos se maneja mediante archivos JSON para garantizar operaciones rápidas y una separación clara entre la lógica de negocio y el almacenamiento.

Tecnologías y Herramientas Integradas

1. Lenguaje: Python 3.9+

2. Arquitectura: POO, Microservicios simulados.

3. Control de Versiones: Git con metodología GitFlow (main, develop, feature/*).

4. CI/CD: Automatización con GitHub Actions (Testing, Linting, Despliegue simulado).

5. Calidad de Código: Flake8 (Linting) y Pytest (Pruebas Unitarias).

Estructura del Repositorio

proyecto_axanet/
├── .github/
│   └── workflows/
│       ├── testing.yml      # Pipeline: Ejecuta tests en Pull Requests a develop
│       ├── lint.yml         # Pipeline: Valida calidad de código (Flake8)
│       └── deploy.yml       # Pipeline: Simula despliegue al integrar en main
├── src/
│   ├── __init__.py          # Inicializador del módulo
│   ├── cliente.py           # Entidad principal y validaciones (Value Objects)
│   ├── gestor.py            # Lógica de persistencia en sistema de archivos JSON
│   └── app.py               # Punto de entrada y CLI interactivo
├── data/
│   └── clientes.json        # Base de datos local (Excluido del repositorio remoto)
├── tests/
│   └── test_cliente.py      # Suite de pruebas automatizadas (Pytest)
├── requirements.txt         # Listado de dependencias del entorno
├── .gitignore               # Archivos omitidos en el control de versiones
└── README.md                # Documentación oficial


Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. Clonar el repositorio:

git clone [https://github.com/Alex150855AR/AXANET.git](https://github.com/Alex150855AR/AXANET.git)
cd AXANET


2. Crear y activar un Entorno Virtual (Recomendado):

En Windows:

python -m venv venv
venv\Scripts\activate


En macOS y Linux:

python3 -m venv venv
source venv/bin/activate


3. Instalar las dependencias:

pip install -r requirements.txt


Guía de Uso

Una vez activado el entorno, el sistema se ejecuta a través de una Interfaz de Línea de Comandos (CLI) intuitiva.

Para iniciar la aplicación, ejecuta:

python -m src.app


Funcionalidades del Menú:

Añadir nuevo cliente (Create): Solicita la información del cliente. Valida en tiempo real que el formato de correo electrónico y la longitud del teléfono sean correctos.

Listar clientes (Read): Muestra un resumen tabular de todos los clientes almacenados en la base local.

Visualizar cliente por ID (Read): Búsqueda específica que devuelve todos los atributos detallados de un cliente.

Modificar datos de cliente (Update): Permite actualizar atributos individuales (ej. Nombre, Teléfono) sin afectar el resto del registro.

Eliminar cliente (Delete): Borra permanentemente un registro del archivo JSON utilizando su ID único.

Salir: Finaliza el proceso de manera segura.

Pruebas Unitarias y Calidad

Para correr las pruebas manualmente en tu entorno de desarrollo y verificar que la lógica de validación funcione correctamente:

# Ejecutar suite de pruebas con nivel de detalle verbose:
pytest tests/ -v

# Ejecutar revisión de sintaxis y estilo de código:
flake8 src/ tests/


Estas mismas pruebas se ejecutan de manera automatizada en los servidores de GitHub cada vez que un desarrollador hace un push o un pull request.