from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.comida_base_schema import ComidaBase, ComidaBaseCreate
import app.repositories.comida_repository as repo
from app.core.registry import Registry
from app.services.producto.producto_service import Producto
from app.services.producto.ingredientes import Ingrediente

router = APIRouter(
    prefix="/comidas", 
    tags=["Comidas"]
)

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


@router.post("/{id_comida}")
def crear_comida(id_comida: int, db: Session = Depends(get_db)):
    '''
    Creo una comida desde el ID de la base de datos
    '''
    nombre_producto = repo.get_clase_producto(db, id_comida)    # Me devuelve el string
    print('desde BD:', nombre_producto)
     
    clase_producto:Producto = Registry.create(nombre_producto)
    print(clase_producto)
    
    #return clase_producto

    

'''def build_comida(comida: str, ingredientes:list[str], db:Session = Depends(get_db)) -> Producto:
    
    #Creo una comida desde el string recibido del front
    #Agrega los ingredientes desde una lista de ID_Ingrediente
    
    
    # Instancio la clase Producto (Hamburguesa, Pizza, ...) 
    clase_producto:Producto = Registry.create(comida)
    
    
    for ingrediente in ingredientes:
        
        ingrediente: Ingrediente = Ingrediente()
            clase_producto = ingrediente(comida)
            
    return clase_producto'''



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



# https://.../api/v1/
    # /comida/base/{id_comida}