from app.services.producto.producto_service import Producto, CategoriaProducto
from app.core.registry import Registry

# categoria.COMIDA
@Registry.register('sopa')
class Sopa(Producto):
    def __init__(self) -> None:
        super().__init__(CategoriaProducto.COMIDA)
        
    def get_categoria(self):
        return self._categoria
    
    def get_ingredientes(self):
        # return 
        pass
        
    
    
