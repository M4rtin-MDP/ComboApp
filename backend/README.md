# Backend Structure (FastAPI)

## Estructura de Carpetas

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                          # Punto de entrada de la aplicación
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py                      # Dependencias compartidas (get_db, get_current_user)
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py                   # Agrupa todos los routers de v1
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── auth.py              # Login, logout, refresh token
│   │           ├── users.py             # CRUD de usuarios
│   │           └── items.py             # CRUD de items (ejemplo)
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py                    # Settings con Pydantic BaseSettings
│   │   ├── security.py                  # JWT, password hashing, permisos
│   │   └── logging.py                   # Configuración de logs
│   │
│   ├── models/                          # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── base.py                      # Base declarativa
│   │   ├── user.py                      # Modelo de Usuario
│   │   └── item.py                      # Modelo de Item
│   │
│   ├── schemas/                         # Pydantic schemas (validación)
│   │   ├── __init__.py
│   │   ├── user.py                      # UserCreate, UserUpdate, UserResponse
│   │   ├── item.py                      # ItemCreate, ItemUpdate, ItemResponse
│   │   └── token.py                     # Token, TokenPayload
│   │
│   ├── crud/                            # Operaciones CRUD con la DB
│   │   ├── __init__.py
│   │   ├── base.py                      # CRUD Base genérico
│   │   ├── crud_user.py                 # CRUD específico de usuarios
│   │   └── crud_item.py                 # CRUD específico de items
│   │
│   ├── services/                        # Lógica de negocio
│   │   ├── __init__.py
│   │   ├── combo_service.py             # Envío de emails
│   │   └── user_service.py              # Lógica de negocio de usuarios
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py                      # Import de todos los modelos
│   │   ├── session.py                   # Configuración de sesión DB
│   │   └── init_db.py                   # Inicialización y seed data
│   │
│   └── utils/
│       ├── __init__.py
│       └── helpers.py                   # Funciones auxiliares
│
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                      # Fixtures de pytest
│   ├── api/
│   │   └── v1/
│   │       ├── test_auth.py
│   │       ├── test_users.py
│   │       └── test_items.py
│   └── crud/
│       ├── test_user.py
│       └── test_item.py
│
├── scripts/                             # Scripts de utilidad
│   ├── init_db.py                       # Inicializar base de datos
│   └── create_superuser.py              # Crear usuario admin
│
├── .env                                 # Variables de entorno (NO commitear)
├── .env.example                         # Ejemplo de variables de entorno
├── .gitignore                       # Configuración de Alembic
├── pyproject.toml                       # Poetry (recomendado)
├── requirements.txt                     # Dependencias pip
├── Dockerfile
└── README.md
```

## Descripción de Componentes

### `app/main.py`
Punto de entrada de la aplicación. Configura FastAPI, CORS, middleware y monta los routers.

### `app/api/deps.py`
Dependencias reutilizables como:
- `get_db()`: Obtiene sesión de base de datos
- `get_current_user()`: Obtiene usuario autenticado
- `get_current_active_superuser()`: Verifica permisos de admin

### `app/api/v1/api.py`
Agrupa todos los routers de la versión 1 de la API.

### `app/core/`
Configuración global del proyecto:
- **config.py**: Variables de entorno usando Pydantic Settings
- **security.py**: Funciones de seguridad (JWT, hashing)
- **logging.py**: Configuración de logs

### `app/models/`
Modelos de SQLAlchemy que representan las tablas de la base de datos.

### `app/schemas/`
Schemas de Pydantic para validación de datos de entrada/salida de la API.

### `app/crud/`
Operaciones básicas de base de datos (Create, Read, Update, Delete). Separa la lógica de DB de los endpoints.

### `app/services/`
Lógica de negocio compleja que va más allá del CRUD simple.

### `alembic/`
Sistema de migraciones para gestionar cambios en el esquema de la base de datos.

### `tests/`
Tests unitarios e integración usando pytest.


## Comandos Útiles

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor de desarrollo
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Crear migración
# alembic revision --autogenerate -m "descripción"

# Aplicar migraciones
# alembic upgrade head

# Ejecutar tests
pytest

# Ejecutar con coverage
pytest --cov=app tests/
```