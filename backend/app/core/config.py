from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from pydantic import Field, computed_field
from functools import lru_cache


# Obtiene la ruta absoluta del directorio raíz del proyecto
# Ruta Raiz -> app/
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    """
    Maneja todas las configuraciones de la aplicación. 
    Lee las variables de entorno desde el archivo .env
    """
    
    # ------------------------------------------------------------------------
    # CONFIGURACIÓN GENERAL
    # ------------------------------------------------------------------------
    # Field(...) indica que el campo es OBLIGATORIO
    # Si no existe en el .env, lanzará un error de validación
    
    # ------ INFO -------
    AMBIENTE: str = Field(...)
    CORS_ORIGINS: list[str] = Field(...)
    API_ALIAS_V1: str
    
    # --- BASE DE DATOS ---
    DB_NAME: str = Field(...)
    DB_HOST: str = Field(...)
    DB_PORT: int = Field(...) 
    DB_USER: str = Field(...)
    DB_PASSWORD: str = Field(...)
    
    
    # @computed_field: Pydantic calcula este campo automáticamente
    # @property: Se accede como un atributo (settings.DB_URL) no como método
    # No se lee del .env, se construye dinámicamente con los otros campos
    @computed_field
    @property
    def DB_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    
    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding='utf-8',
        case_sensitive=True                     # Los nombres de variables deben coincidir exactamente
    )
    

# @lru_cache(): Cachea el resultado, ejecuta Settings() solo UNA vez
# - Patrón Singleton: una sola instancia en toda la aplicación
@lru_cache()
def get_settings() -> Settings:
    """
    Retorna la instancia única de configuración.
    Primera llamada: lee el .env y crea Settings
    Siguientes llamadas: devuelve la instancia cacheada
    """
    return Settings()
