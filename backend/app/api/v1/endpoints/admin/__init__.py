from fastapi import APIRouter

from .. import ingredientes_comida_routes

# Importar los routers de este subdirectorio
from . import restaurante_routes

# Crear un router para todos los endpoints de admin
admin_router = APIRouter(
    prefix="/admin",  
    tags=["Admin"]
)

admin_router.include_router(restaurante_routes.router, prefix= '/restaurantes')

# Exponer el router
__all__ = ["admin_router"]