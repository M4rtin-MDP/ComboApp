from fastapi import APIRouter

# Importar todos los routers de los archivos .py en este directorio
from . import auth_routes, categoria_routes, comida_routes, estado_routes, ingrediente_routes, pedido_routes, usuario_routes

# Importar routers de subdirectorios
# Nota: La estructura combo y admin ya tienen su propio __init__.py
from . import admin, combo

# Crear un APIRouter maestro para todos los endpoints de v1
v1_router = APIRouter()

# Incluir los routers 
v1_router.include_router(admin.admin_router)

v1_router.include_router(auth_routes.router)
v1_router.include_router(categoria_routes.router)
v1_router.include_router(combo.combo_router)
v1_router.include_router(comida_routes.router)
v1_router.include_router(estado_routes.router)
v1_router.include_router(ingrediente_routes.router)
v1_router.include_router(pedido_routes.router)
v1_router.include_router(usuario_routes.router)




# Exponer el router maestro para que pueda ser importado desde api.py
__all__ = ["v1_router"]