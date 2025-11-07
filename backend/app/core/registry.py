"""
Registro global de clases para instanciación dinámica.
"""
from typing import Any, Dict, Type, Optional


class Registry:
    """Registro singleton para clases dinámicas"""
    _classes: Dict[str, Type] = {}
    
    @classmethod
    def register(cls, name: Optional[str] = None):
        """
        Decorador para registrar clases automáticamente.
        
        Args:
            name: Nombre personalizado. Si es None, usa el nombre de la clase.
        
        Example:
            @Registry.register()
            class MiClase:
                pass
            
            @Registry.register("nombre_custom")
            class OtraClase:
                pass
        """
        def decorator(klass: Type) -> Type:
            key = name or klass.__name__
            cls._classes[key] = klass
            return klass
        return decorator
    
    @classmethod
    def get(cls, name: str) -> Optional[Type]:
        """
        Obtiene una clase por su nombre.
        
        Args:
            name: Nombre de la clase registrada.
            
        Returns:
            La clase o None si no existe.
        """
        return cls._classes.get(name)
    
    @classmethod
    def create(cls, name: str, *args, **kwargs) -> Any:
        """
        Crea una instancia de una clase registrada.
        
        Ejemplo de uso: comida = get('hamburguesa')
        
        Args:
            name: Nombre de la clase.
            *args, **kwargs: Argumentos para el constructor.
            
        Returns:
            Instancia de la clase.
            
        Raises:
            ValueError: Si la clase no está registrada.
        """
        klass = cls.get(name)
        if klass is None:
            raise ValueError(
                f"Clase '{name}' no encontrada. "
                f"Disponibles: {cls.list_all()}"
            )
        return klass(*args, **kwargs)
    
    @classmethod
    def list_all(cls) -> list[str]:
        """Lista todas las clases registradas."""
        return list(cls._classes.keys())
    
    @classmethod
    def clear(cls):
        """Limpia el registro (útil para tests)."""
        cls._classes.clear()