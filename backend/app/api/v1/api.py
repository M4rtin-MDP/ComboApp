from fastapi import APIRouter
from app.api.v1.endpoints import auth_routes, combo_routes, ingredient_routes, user_routes, product_routes, local_routes, order_routes

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
    ingredient_routes.router,
    prefix="/ingredientes",
    tags=["Ingredientes"]
)

api_router.include_router(
    user_routes.router, 
    prefix="/users", 
    tags=["Users"]
)

api_router.include_router(
    product_routes.router, 
    prefix="/products", 
    tags=["Products"]
)

api_router.include_router(
    local_routes.router, 
    prefix="/locals", 
    tags=["Locals"]
)

api_router.include_router(
    order_routes.router, 
    prefix="/orders", 
    tags=["Orders"]
)