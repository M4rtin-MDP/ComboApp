from fastapi import APIRouter
from app.api.v1.endpoints import auth_routes, combo_routes, ingrediente_routes, usuario_routes, comida_routes
from app.api.v1.endpoints import restaurante_routes, pedido_routes, estado_routes, categoria_routes 
from app.api.v1.endpoints import item_comida_routes, item_ingrediente_routes, ingr_comida_routes

api_router = APIRouter()

# Authentication endpoints
api_router.include_router(
    auth_routes.router,
    prefix="/auth",
    tags=["Authentication"]
)

# Combo endpoints
api_router.include_router(
    combo_routes.router,
    prefix="/combos",
    tags=["Combos"]
)

# Ingredientes
api_router.include_router(
    ingrediente_routes.router,
    prefix="/ingredientes",
    tags=["Ingredientes"]
)
# Usuarios
api_router.include_router(
    usuario_routes.router, 
    prefix="/usuarios", 
    tags=["Usuarios"]
)
# Comidas
api_router.include_router(
    comida_routes.router, 
    prefix="/comidas", 
    tags=["comidas"]
)

# Restaurantes
api_router.include_router(
    restaurante_routes.router, 
    prefix="/restautantes", 
    tags=["Restaurantes"]
)

# Pedidos
api_router.include_router(
    pedido_routes.router, 
    prefix="/pedidos", 
    tags=["Pedidos"]
)

# Categoria
api_router.include_router(
    categoria_routes.router, 
    prefix="/categoriass", 
    tags=["Categorias"]
)

# Estado
api_router.include_router(
    estado_routes.router, 
    prefix="/estados", 
    tags=["Estados"]
)

# Item_Ingrediente
api_router.include_router(
    item_ingrediente_routes.router, 
    prefix="/item_ingredientes", 
    tags=["Item_ingredientes"]
)

# Item_comida
api_router.include_router(
    item_comida_routes.router, 
    prefix="/item_comidas", 
    tags=["Item_comidas"]
)

# Ingr_comida
api_router.include_router(
    ingr_comida_routes.router, 
    prefix="/ingr_comidas", 
    tags=["Ingr_comidas"]
)