from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.settings import settings

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:c0mb0_App@db.mkvcewwbvgqykjqsawkz.supabase.co:5432/postgres"

# Motor de la base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    #settings.DATABASE_URL,
    
    # Para PostgreSQL:
    pool_pre_ping=True,  # Verifica conexiones antes de usarlas
)

# SessionLocal: cada instancia es una sesión de BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos ORM
Base = declarative_base()


# Dependencia para obtener una sesión de BD
def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()