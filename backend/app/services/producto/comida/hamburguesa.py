from producto_service import Producto, CategoriaProducto
from abc import ABC

# categoria.COMIDA
class Hambuerguesa(Producto):
    def __init__(self) -> None:
        super().__init__(CategoriaProducto.COMIDA)
        
    def get_categoria(self):
        return self._categoria
    
    def get_ingredientes(self):
        # return 
        pass
        
        


class DecoradorHamburguesa(Hambuerguesa, ABC):
    def __init__(self) -> None:
        super().__init__()
        

class (DecoradorHamburguesa):
    pass

    