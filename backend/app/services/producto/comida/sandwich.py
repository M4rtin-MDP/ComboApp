from app.services.producto.producto_service import Producto, CategoriaProducto
from typing import Type
from abc import ABC
from app.core.registry import Registry

# categoria.COMIDA
@Registry.register('sandwich')
class Sandwich(Producto):
    def __init__(self) -> None:
        super().__init__(CategoriaProducto.COMIDA)
        
    def get_categoria(self):
        return self._categoria
    
    def get_ingredientes(self):
        # return 
        pass
        
    
    
