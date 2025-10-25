from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import user_routes, product_routes, local_routes, combo_routes, order_routes
from fastapi.middleware.cors import CORSMiddleware

# create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ComboApp Full API")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000", 
    "http://127.0.0.1:3000"
]

# allow CORS for local frontend during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.include_router(auth_routes.router)
#app.include_router(ingredient_routes.router)
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(product_routes.router, prefix="/products", tags=["Products"])
app.include_router(local_routes.router, prefix="/locals", tags=["Locals"])
app.include_router(combo_routes.router, prefix="/combos", tags=["Combos"])
app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])

@app.get('/')
def root():
    return {'message': 'ComboApp API running'}
