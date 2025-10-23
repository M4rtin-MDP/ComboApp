## Documentacion:
- supabase: https://supabase.com/docs/reference/python/select
- fastAPI:  https://fastapi.tiangolo.com/tutorial/

#### cositas para ver
- workflows/branch-protection.yml       ??
- Docker

### Requisitos previos:
    sudo apt install python3.12-venv
    sudo apt install -y libpq-dev python3-dev

    sudo sysctl -w net.ipv6.conf.all.disable_ipv6=0
    sudo sysctl -w net.ipv6.conf.default.disable_ipv6=0

--------------------------------------------------------------
### Ejecutar ambiente virtual 
Si no funciona, probar con *python3*

    python -m venv .venv

Activar el entorno

    PowerShell:    .\.venv\Scripts\activate
    Linux:      source .venv/bin/activate

Instalar Dependencias

    pip install -r requirements.txt


### Ejecutar la API

    uvicorn app.main:app --reload


### Ejecutar Frontend



## Estructura del Proyecto
```
combo_app/
├── app/
│   ├── __init__.py
│   ├── main.py                     # Instancia todos los routers
│   │
│   ├── core/                       # Contiene configuración global y componentes básicos del proyecto
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── api/
│   │   └── v1/                     # Creación de endpoints (routers)
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── items.py
│   │       └── auth.py
│   │
│   ├── models/                     # Representa la estructura real de la base de datos
│   │   ├── __init__.py             # Se usa para consultas, inserciones, actualizaciones mediante ORM
│   │   ├── user.py
│   │   └── item.py
│   │
│   ├── schemas/                    # Define las clases Pydantic
│   │   ├── __init__.py             # Se usa para validar y serializar datos (requests y responses)
│   │   ├── user.py
│   │   └── item.py
│   │
│   ├── utils/                      # Funciones auxiliares para el proyecto
│   │   ├── __init__.py
│   │   └── item_service.py
│   │
│   ├── services/                   # Lógica de negocio e interacción con la Base de Datos
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── item_service.py
│   │
│   └── db/
│       ├── __init__.py
│       ├── database.py
│       └── migrations/
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_users.py
│   └── test_items.py
│
├── Dockerfile                      # Cómo se construye el contenedor
├── docker-compose.yml              # Levanta todo el entorno (API + base de datos)
├── .env                            # Variables sensibles (DB, claves JWT)
├── .gitignore
├── requirements.txt                # Dependencias (fastapi, uvicorn, sqlalchemy, etc.)
├── README.md
└── run.sh
```
