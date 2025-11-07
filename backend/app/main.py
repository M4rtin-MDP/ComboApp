from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.api.v1.endpoints import v1_router  # Importa el router maestro del __init__.py

<<<<<<< HEAD
import app.services.producto.comida.hamburguesa
import app.services.producto.comida.pizza
import app.services.producto.comida.milanesa
import app.services.producto.comida.sandwich
import app.services.producto.comida.empanada
import app.services.producto.comida.ensalada
import app.services.producto.comida.sopa
import app.services.producto.postre.flan
import app.services.producto.postre.budin

# Obtener configuración
settings = get_settings()

Base.metadata.create_all(bind=engine)
=======
#Base.metadata.create_all(bind=engine)
>>>>>>> jomiguel

# ----------------------------------------------------------------------------
# APLICACIÓN FASTAPI
# ----------------------------------------------------------------------------
app = FastAPI(
    title="ComboApp",
    version="1.0",
    description="API para gestión de combos y productos",)

# ----------------------------------------------------------------------------
# MIDDLEWARE: CORS (Cross-Origin Resource Sharing)
# ----------------------------------------------------------------------------
#origins = settings.CORS_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],                        # Lista de dominios permitidos para hacer requests
    allow_credentials=True,                     # Permite enviar cookies y headers de autenticación
    allow_methods=["*"],                        # Métodos HTTP permitidos (* = todos) - GET, POST, DELETE, OPTIONS
    allow_headers=["*"],                        # Headers permitidos (* = todos) - Authorization, Content-Type, etc.
)


# ----------------------------------------------------------------------------
# ROUTERS: Incluir rutas de la API

# Incluimos el router maestro de la versión (v1). 
# y les aplica el prefijo "/v1" a todos.
app.include_router(
    v1_router, 
    prefix="/v1"
)


@app.on_event("startup")
async def startup_event():
    from app.core.registry import Registry
    print(f"Aplicación iniciada")
    print(f"Clases registradas: {Registry.list_all()}") 


# Endpoint RAIZ
@app.get('/')
def root():
    '''
    Verifica que la API está activa
    '''
    return {
        'status': 'ok',
        'message': 'ComboApp API funciona!'
    }

