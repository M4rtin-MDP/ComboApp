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

from app.api.v1.endpoints import (
    usuario_routes as usuario,
    pedido_routes as pedido,
    categoria_routes as categoria,
    restaurante_routes as restaurante,
    ingrediente_routes as ingrediente,
    combo_routes as combo,
    estado_routes as estado,
    item_comida_routes as item_comida,
    ingr_comida_routes as ingr_comida,
    comida_routes as comida,
    item_ingrediente_routes as item_ingrediente,
)

app.include_router(usuario.router)
app.include_router(pedido.router)
app.include_router(categoria.router)
app.include_router(restaurante.router)
app.include_router(ingrediente.router)
app.include_router(combo.router)
app.include_router(estado.router)
app.include_router(item_comida.router)
app.include_router(ingr_comida.router)
app.include_router(comida.router)
app.include_router(item_ingrediente.router)


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

