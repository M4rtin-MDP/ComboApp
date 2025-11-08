from typing import List
from sqlalchemy.orm import Session
from app.models import Ingrediente, IngrComida
from app.schemas import IngrComidaCreate

# Esta funcion retorna los ingredientes asociados a una comida base 
def get_ingredientes_comida(db: Session, comida: int):
    return db.query(IngrComida).filter(IngrComida.id_comida == comida).all()
#------------------------------------------------------------  
'''
def get_ingredientes_comida(db: Session, id_comida: int):
    """
    Devuelve los ingredientes disponibles (disponible=True)
    de una comida específica, incluyendo el nombre del ingrediente.
    """
    resultados = (
        db.query(
            Ingrediente.id_ingrediente.label("id_ingrediente"),
            Ingrediente.nombre.label("nombre")
        )
        .innerjoin(Ingrediente, Ingrediente.id_ingrediente == IngrComida.id_ingrediente)
        .filter(IngrComida.id_comida == id_comida)
        .filter(IngrComida.disponible.is_(True))
        .all()
    )

    return [
        {
            "id_ingrediente": r.id_ingrediente,
            "nombre": r.nombre
        }
        for r in resultados
    ]
'''
def create_ingr_comida(db: Session, ingr: IngrComidaCreate):
    db_ingr = IngrComida(**ingr.dict())
    db.add(db_ingr)
    db.commit()
    db.refresh(db_ingr)
    return db_ingr

def delete_ingr_comida(db: Session, id_ingr: int):
    db_ingr = get_ingredientes_comida(db, id_ingr)
    if not db_ingr:
        return None
    db.delete(db_ingr)
    db.commit()
    return db_ingr