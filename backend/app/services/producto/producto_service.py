from sqlalchemy.orm import Session
import app.repositories.comida_repository as repo
from schemas import ComidaBaseCreate
from abc import ABC, abstractmethod
from enum import Enum


class CategoriaProducto(Enum):
    BEBIDA = 1
    COMIDA = 2
    POSTRE = 3

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
    
    @abstractmethod
    def agregar_ingrediente(self, ingrediente):
        pass
    







