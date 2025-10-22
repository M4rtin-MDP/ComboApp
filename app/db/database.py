import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

DATABASE_URL = "sqlite:///./combobuilder.db"

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:c0mb0_App@db.mkvcewwbvgqykjqsawkz.supabase.co:5432/postgres"
# https://mkvcewwbvgqykjqsawkz.supabase.co
# sb_secret_OCELAUU3XiBBkkgxDxbB1g_-IqunVXe


def get_config():
    # Cargar variables del archivo .env
    # Subir dos niveles desde database.py hasta la raíz y localizar instalacion.env
    #env_path = Path(__file__).resolve().parent.parent.parent / "instalacion.env"
    #load_dotenv(dotenv_path=env_path)


    # Leer variables
    
    USER = os.getenv("USER")
    PASSWORD = 'c0mb0_App' #os.getenv("PASS")
    HOST = os.getenv("DB_HOST", 'db.mkvcewwbvgqykjqsawkz.supabase.co')
    PORT = os.getenv("PORT", "5432")
    DB_NAME = os.getenv("DB_NAME")

    DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    return DATABASE_URL


URL = get_config()
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()