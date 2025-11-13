from sqlalchemy.orm import Session
import app.repositories.comida_repository as repo
from app.schemas.comida_base_schema import ComidaBaseCreate



class Producto():
    
    def listar_comidas(self, db: Session):
        return repo.get_comidas(db)

    def obtener_comida(self, db: Session, id_comida: int):
        return repo.get_comida(db, id_comida)


    def actualizar_comida(self, db: Session, id_comida: int, comida: ComidaBaseCreate):
        return repo.update_comida(db, id_comida, comida)

    def eliminar_comida(self, db: Session, id_comida: int):
        return repo.delete_comida(db, id_comida)
    
    


