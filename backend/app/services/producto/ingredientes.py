from app.services.producto.producto_service import Producto, CategoriaProducto
from abc import ABC, abstractmethod
from app.core.registry import Registry

# Decorador de ingredientes
class Ingrediente(Producto, ABC):
    def __init__(self) -> None:
        super().__init__(CategoriaProducto.INGREDIENTE)
    
    
# Implementacion de ingredientes--------------------------------------------
'''
class Ingrediente(Producto, ABC):
    def __init__(self, nombre: str, precio: float) -> None:
        super().__init__(CategoriaProducto.INGREDIENTE, nombre=nombre, precio=precio)
        Registry.register(self)  # lo registra en el sistema global (si usás Registry)

class Tomate(Ingrediente):
    def __init__(self):
        super().__init__("Tomate", 50.0) # deberia traer valores del JSON de los restaurantes sugeridos

class Lechuga(Ingrediente):
    def __init__(self):
        super().__init__("Lechuga", 40.0) 
'''        
# --------------------------------------------

class Tomate(Ingrediente):
    pass

class Lechuga(Ingrediente):
    pass

class QuesoCheddar(Ingrediente):
    pass

class Cebolla(Ingrediente):
    pass

class CebollaCaramelizada(Ingrediente):
    pass

class Panceta(Ingrediente):
    pass

class HuevoFrito(Ingrediente):
    pass

class Palta(Ingrediente):
    pass

class Champiniones(Ingrediente):
    pass

class Morrones(Ingrediente):
    pass

class Jamon(Ingrediente):
    pass

class QuesoMozzarella(Ingrediente):
    pass

class Pepperoni(Ingrediente):
    pass

class Pollo(Ingrediente):
    pass

class QuesoProvolone(Ingrediente):
    pass

class SalchichaItaliana(Ingrediente):
    pass

class AceitunasVerdes(Ingrediente):
    pass

class AceitunasNegras(Ingrediente):
    pass

class MaizDulce(Ingrediente):
    pass

class Esparragos(Ingrediente):
    pass

class Oregano(Ingrediente):
    pass

class AlbahacaFresca(Ingrediente):
    pass

class Tomillo(Ingrediente):
    pass

class Romero(Ingrediente):
    pass

class Anchoas(Ingrediente):
    pass

class Ajo(Ingrediente):
    pass

class HuevoDuro(Ingrediente):
    pass

class Anana(Ingrediente):
    pass

class Mostaza(Ingrediente):
    pass

class Mayonesa(Ingrediente):
    pass

class Barbacoa(Ingrediente):
    pass

class Ketchup(Ingrediente):
    pass

class SalsaGolf(Ingrediente):
    pass

class SalsaCaesar(Ingrediente):
    pass

class Chimichurri(Ingrediente):
    pass

class SalsaCriolla(Ingrediente):
    pass

class PasasDeUva(Ingrediente):
    pass

class CrutonesDePan(Ingrediente):
    pass

class QuesoAzul(Ingrediente):
    pass

class SalsaDeTomate(Ingrediente):
    pass

class SalsaPortuguesa(Ingrediente):
    pass

class SalsaNapolitana(Ingrediente):
    pass

class SalsaPicante(Ingrediente):
    pass

class SalsaRosa(Ingrediente):
    pass

class DulceDeLeche(Ingrediente):
    pass

class CremaDeLeche(Ingrediente):
    pass