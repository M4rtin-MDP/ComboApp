from producto_service import Producto, CategoriaProducto
from ingredientes.hamburguesa_decorador import DecoradorHamburguesa
from typing import Type


# categoria.COMIDA
class Hamburguesa(Producto):
    def __init__(self) -> None:
        super().__init__(CategoriaProducto.COMIDA)
        
    def get_categoria(self):
        return self._categoria
    
    def get_ingredientes(self):
        # return 
        pass
        
        
    def agregar_ingrediente(self , ingrediente: Type[DecoradorHamburguesa]):
        ingrediente(self)
        pass
        
