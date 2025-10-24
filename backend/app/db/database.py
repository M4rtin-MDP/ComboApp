# ============================================================================
# Configuración de SQLAlchemy para conexión a PostgreSQL
# ============================================================================

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import get_settings


# Obtener configuración
settings = get_settings()

# --------------------------------------------------------------
# ENGINE: Conexion a la base de datos
# --------------------------------------------------------------
engine = create_engine(
    settings.DB_URL,
    pool_pre_ping=True,         # Verifica si la conexión está viva antes de usarla
    pool_size=5,                # Número de conexiones permanentes en el pool
    
    # max_overflow: Conexiones adicionales permitidas bajo demanda
    # Total máximo = pool_size + max_overflow = 5 + 10 = 15
    max_overflow=10,
    
    # pool_recycle: Recicla conexiones cada X segundos
    # Evita problemas con conexiones que expiran en el servidor
    pool_recycle=3600,  # 1 hora
)


# --------------------------------------------------------------
# SESSION: Cada instancia es una sesión de BD
# --------------------------------------------------------------
SessionLocal = sessionmaker(
    # autocommit=False: Requiere commit() explícito para guardar cambios
    autocommit=False, 
    
    # No hace flush automático antes de queries
    autoflush=False, 
    
    # bind: Vincula las sesiones al engine creado arriba
    bind=engine)


# BASE para los modelos ORM
Base = declarative_base()



def get_db():
    """
    - Crea una sesión nueva para cada request
    - Garantiza que se cierre después de usarla
    
    Uso en FastAPI:
        @app.get("/items/")
        def read_items(db: Session = Depends(get_db)):
            items = db.query(Item).all()
            return items
    """
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()