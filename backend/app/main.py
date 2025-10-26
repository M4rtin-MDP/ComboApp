from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.api.v1.api import api_router

# Obtener configuración
settings = get_settings()


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
# ----------------------------------------------------------------------------
# Incluye todas las rutas definidas en api_router
# Ej: prefix="/api/v1" -> http://localhost:8000/api/v1/items
app.include_router(
    api_router
    , prefix=settings.API_ALIAS_V1
) 

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

