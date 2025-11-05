
from abc import ABC
from producto.comida.hamburguesa import Hamburguesa

class DecoradorHamburguesa(Hamburguesa, ABC):
    def __init__(self) -> None:
        super().__init__()
        
'''
    Tiene que devolver el precio de cada ingrediente sacado del JSON
'''

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
