from app.services.producto.producto_service import Producto, CategoriaProducto
from app.core.registry import Registry

# categoria.POSTRE
@Registry.register('vino_blanco')
class VinoBlanco(Producto):
    def __init__(self) -> None:
        super().__init__(CategoriaProducto.POSTRE)
        
    def get_categoria(self):
        return self._categoria
    
    def get_ingredientes(self):
        # return 
        pass
        
    
    
