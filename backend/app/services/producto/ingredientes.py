from app.services.producto.producto_service import Producto, CategoriaProducto
from abc import ABC, abstractmethod
from app.core.registry import Registry

# Decorador de ingredientes
class Ingrediente(Producto, ABC):
    def __init__(self, producto: Producto) -> None:
        super().__init__(CategoriaProducto.INGREDIENTE)
        self.producto = producto
    
    
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
@Registry.register('tomate')
class Tomate(Ingrediente):
    pass
@Registry.register('lechuga')
class Lechuga(Ingrediente):
    pass

@Registry.register('queso_cheddar')
class QuesoCheddar(Ingrediente):
    pass

@Registry.register('cebolla')
class Cebolla(Ingrediente):
    pass

@Registry.register('panceta')
class Panceta(Ingrediente):
    pass

@Registry.register('huevo_frito')
class HuevoFrito(Ingrediente):
    pass

@Registry.register('palta')
class Palta(Ingrediente):
    pass

@Registry.register('champiniones')
class Champiniones(Ingrediente):
    pass

@Registry.register('morrones')
class Morrones(Ingrediente):
    pass

@Registry.register('jamon')
class Jamon(Ingrediente):
    pass

@Registry.register('queso_mozzarella')
class QuesoMozzarella(Ingrediente):
    pass

@Registry.register('pepperoni')
class Pepperoni(Ingrediente):
    pass

@Registry.register('pollo')
class Pollo(Ingrediente):
    pass

@Registry.register('queso_provolone')
class QuesoProvolone(Ingrediente):
    pass

@Registry.register('salchicha_italiana')
class SalchichaItaliana(Ingrediente):
    pass

@Registry.register('aceitunas_verdes')
class AceitunasVerdes(Ingrediente):
    pass

@Registry.register('aceitunas_negrasr')
class AceitunasNegras(Ingrediente):
    pass

@Registry.register('maiz_dulce')
class MaizDulce(Ingrediente):
    pass

@Registry.register('esparragos')
class Esparragos(Ingrediente):
    pass

@Registry.register('oregano')
class Oregano(Ingrediente):
    pass

@Registry.register('albahaca_fresca')
class AlbahacaFresca(Ingrediente):
    pass

@Registry.register('tomillo')
class Tomillo(Ingrediente):
    pass

@Registry.register('romero')
class Romero(Ingrediente):
    pass

@Registry.register('anchoas')
class Anchoas(Ingrediente):
    pass

@Registry.register('ajo')
class Ajo(Ingrediente):
    pass

@Registry.register('huevo_duro')
class HuevoDuro(Ingrediente):
    pass

@Registry.register('anana')
class Anana(Ingrediente):
    pass

@Registry.register('mostaza')
class Mostaza(Ingrediente):
    pass

@Registry.register('mayonesa')
class Mayonesa(Ingrediente):
    pass

@Registry.register('barbacoa')
class Barbacoa(Ingrediente):
    pass

@Registry.register('ketchup')
class Ketchup(Ingrediente):
    pass

@Registry.register('salsa_golf')
class SalsaGolf(Ingrediente):
    pass

@Registry.register('salsa_caesar')
class SalsaCaesar(Ingrediente):
    pass

@Registry.register('chimichurri')
class Chimichurri(Ingrediente):
    pass

@Registry.register('salsa_criolla')
class SalsaCriolla(Ingrediente):
    pass

@Registry.register('pasas_uva')
class PasasDeUva(Ingrediente):
    pass

@Registry.register('crutones_pan')
class CrutonesDePan(Ingrediente):
    pass

@Registry.register('queso_azul')
class QuesoAzul(Ingrediente):
    pass

@Registry.register('salsa_tomate')
class SalsaDeTomate(Ingrediente):
    pass

@Registry.register('salsa_portuguesa')
class SalsaPortuguesa(Ingrediente):
    pass

@Registry.register('salsa_napolitana')
class SalsaNapolitana(Ingrediente):
    pass

@Registry.register('salsa_picante')
class SalsaPicante(Ingrediente):
    pass

@Registry.register('salsa_rosa')
class SalsaRosa(Ingrediente):
    pass

@Registry.register('dulce_leche')
class DulceDeLeche(Ingrediente):
    pass

@Registry.register('crema_leche')
class CremaDeLeche(Ingrediente):
    pass