from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import settings
from app.api.v1.api import api_router


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

# Montar el router de API v1
app.include_router(api_router) #, prefix=settings.API_V1_STR)

@app.get('/')
def root():
    return {'message': 'ComboApp API funciona papa'}
