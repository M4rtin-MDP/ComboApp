
from fastapi import APIRouter

# Importar los routers de este subdirectorio
from . import combo_routes, item_comida_routes, item_ingrediente_routes

# Crear un router para todos los endpoints de combos
combo_router = APIRouter(
    prefix="/combos",  
    tags=["Combos"]
)

combo_router.include_router(combo_routes.router)
combo_router.include_router(item_comida_routes.router, prefix= '/items_comidas')
combo_router.include_router(item_ingrediente_routes.router, prefix= '/ites_ingredientes')

# Exponer el router
__all__ = ["combo_router"]