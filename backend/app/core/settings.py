from pydantic_settings import BaseSettings
from pathlib import Path
from pydantic import Field

# Ruta Raiz. Apunta app/
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    
    # CONFIGURACION GENERAL
    ENVIRONMENT: str = Field(default="desarrollo", alias="AMBIENTE")
    
    # BASE DE DATOS
    # los ... significa campo OBLIGATORIO
    DB_USER: str = Field(alias="DATABASE_USER")
    DB_PASSWORD: str = Field(alias="DATABASE_PASSWORD")
    DB_HOST: str = Field(default="localhost", alias="DATABASE_HOST")
    DB_PORT: int = Field(default=5432, alias="DATABASE_PORT")
    DB_NAME: str = Field(alias="DATABASE_NAME")
    
    
    @property
    def database_url(self) -> str:
        """Construye la URL de la base de datos si usas componentes"""
        # DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Pydantic lo lee y aplica estas reglas
    class Config:
        env_file = str(BASE_DIR / ".env")
        case_sensitive = True

# Instancia única (Singleton)
settings = Settings()