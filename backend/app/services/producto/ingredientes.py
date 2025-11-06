from app.services.producto.producto_service import Producto, CategoriaProducto
from abc import ABC, abstractmethod
from app.core.registry import Registry

# Decorador de ingredientes
class Ingrediente(Producto, ABC):
    def __init__(self) -> None:
        super().__init__(CategoriaProducto.INGREDIENTE)
    
    
# --------------------------------------------
# 
# --------------------------------------------

class QuesoAzul(Ingrediente):

    pass

class Tomate(Ingrediente):
    pass

class Lechuga(Ingrediente):
    pass

class Cebolla(Ingrediente):
    pass

class CebollaCaramelizada(Ingrediente):
    pass

class Bacon(Ingrediente):
    pass

class Huevos(Ingrediente):
    pass

class Jamon(Ingrediente):
    pass

class Mayonesa(Ingrediente):
    pass

class Ketchup(Ingrediente):
    pass

class Mostaza(Ingrediente):
    pass
