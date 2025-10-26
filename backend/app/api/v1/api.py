from fastapi import APIRouter
from app.api.v1.endpoints import auth_routes, combo_routes, ingredient_routes

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
    prefix="/ingredients",
    tags=["Ingredientes"]
)