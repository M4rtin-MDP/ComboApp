from sqlalchemy.orm import Session
import app.repositories.comida_repository as repo
from app.schemas.comida_base_schema import ComidaBaseCreate
from abc import ABC, abstractmethod
from enum import Enum


class CategoriaProducto(Enum):
    BEBIDA = 1
    COMIDA = 2
    POSTRE = 3
    INGREDIENTE = 4

'''
Agrergarle el atributo precio (opcionalmente). La idea es setearlo cuando se selecciona le restauranmte (a traves de un get) y que devuevla el total del combo.
Una vez que tenga el total y se confirma, se guarda en la tabla pedidos
'''
class Producto(ABC):
    
    def __init__(self, categoria: CategoriaProducto) -> None:
        self._categoria = categoria
    
    '''
        listar_comidas  -> repo.get_producto_comida()
        listar_bebidas
        listar_postresr
    '''
    def listar_comidas(self, db: Session):
        return repo.get_comidas(db)

    def obtener_comida(self, db: Session, id_comida: int):
        return repo.get_comida(db, id_comida)


    def actualizar_comida(self, db: Session, id_comida: int, comida: ComidaBaseCreate):
        return repo.update_comida(db, id_comida, comida)

    def eliminar_comida(self, db: Session, id_comida: int):
        return repo.delete_comida(db, id_comida)
    
    
'''    @abstractmethod
    def get_precio():
        
        pass
    '''






