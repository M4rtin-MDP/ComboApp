from .usuario import Usuario
from .categoria import Categoria
from .combo import Combo
from .comida import ComidaBase
from .estado import Estado
from .ingrediente import Ingrediente
from .item_comida import ItemComida
from .item_ingrediente import ItemIngrediente
from .pedido import Pedido
from .restaurante import Restaurante
from .ingr_comida import IngrComida

# Esto asegura que todos los modelos se registren
__all__ = [
    "Usuario",
    "Categoria", 
    "Combo",
    "ComidaBase",
    "Estado",
    "Ingrediente",
    "ItemComida",
    "ItemIngrediente",
    "Pedido",
    "Restaurante",
    "IngrComida"
]