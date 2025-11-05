from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.comida_base_schema import ComidaBase, ComidaBaseCreate
import app.repositories.comida_repository as repo

router = APIRouter()

@router.get("/", response_model=List[ComidaBase])
def listar_comidas(db: Session = Depends(get_db)):
    return repo.get_comidas(db)

@router.get("/{id_comida}", response_model=ComidaBase)
def obtener_comida(id_comida: int, db: Session = Depends(get_db)):
    comida = repo.get_comida(db, id_comida)
    if not comida:
        raise HTTPException(status_code=404, detail="Comida no encontrada")
    return comida

'''
Le paso el id_comida: si es Hamburguesa, Pizza, ...
'''

'''
@router.post("/{id_comida}")
def crear_comida(comida: Producto):
    
    con el id_comida puedo conseguir que Clase le corresponde (ejh: Hambuergues) y lo devuevle como string
    
    TODO: registro automático con decorador - Buscar
    
    -----------------
    si me devuelve el string -> 'Hamburguesa'
    
    
    pass
'''

'''
def build_comida(comida_base: Type[Producto], ingredients:list[Type[Producto]]) -> Producto:
    comida = comida_base()
    for ingrediente in ingredients:
            comida = ingredient(comida)
    return comida
'''


@router.put("/{id_comida}", response_model=ComidaBase)
def actualizar_comida(id_comida: int, comida: ComidaBaseCreate, db: Session = Depends(get_db)):
    updated = repo.update_comida(db, id_comida, comida)
    if not updated:
        raise HTTPException(status_code=404, detail="Comida no encontrada")
    return updated

@router.delete("/{id_comida}", response_model=ComidaBase)
def eliminar_comida(id_comida: int, db: Session = Depends(get_db)):
    deleted = repo.delete_comida(db, id_comida)
    if not deleted:
        raise HTTPException(status_code=404, detail="Comida no encontrada")
    return deleted



