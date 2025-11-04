from producto_service import Producto, CategoriaProducto
from abc import ABC

# categoria.COMIDA
class Hamburguesa(Producto):
    def __init__(self) -> None:
        super().__init__(CategoriaProducto.COMIDA)
        
    def get_categoria(self):
        return self._categoria
    
    def get_ingredientes(self):
        # return 
        pass
        
        


class DecoradorHamburguesa(Hamburguesa, ABC):
    def __init__(self) -> None:
        super().__init__()
        

class QuesoCheddar(DecoradorHamburguesa):
    pass

class Tomate(DecoradorHamburguesa):
    pass

class Lechuga(DecoradorHamburguesa):
    pass

class Cebolla(DecoradorHamburguesa):
    pass

class CebollaCaramelizada(DecoradorHamburguesa):
    pass

class Bacon(DecoradorHamburguesa):
    pass

class Huevos(DecoradorHamburguesa):
    pass

class Jamon(DecoradorHamburguesa):
    pass

class Mayonesa(DecoradorHamburguesa):
    pass

class Ketchup(DecoradorHamburguesa):
    pass

class Mostaza(DecoradorHamburguesa):
    pass
