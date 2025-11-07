from fastapi import APIRouter

# Importar los routers de este subdirectorio
from . import ingr_comida_routes, restaurante_routes

# Crear un router para todos los endpoints de admin
admin_router = APIRouter(
    prefix="/admin",  
    tags=["Admin"]
)

admin_router.include_router(ingr_comida_routes.router, prefix= '/ingredientes_x_comida')
admin_router.include_router(restaurante_routes.router, prefix= '/restaurantes')

# Exponer el router
__all__ = ["admin_router"]