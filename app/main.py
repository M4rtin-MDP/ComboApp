from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import auth_routes, ingredient_routes, combo_routes
from fastapi.middleware.cors import CORSMiddleware

# create tables
#Base.metadata.create_all(bind=engine)

app = FastAPI(title="ComboApp", version="1.0")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)
app.include_router(ingredient_routes.router)
app.include_router(combo_routes.router)

@app.get('/')
def root():
    return {'message': 'ComboApp API funciona papa'}
