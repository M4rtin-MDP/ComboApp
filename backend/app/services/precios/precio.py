from abc import ABC, abstractmethod
from typing import List, Dict
from app.schemas.restaurante_schema import ComboRequest


class CalculadorPrecio(ABC):
    """Interface para calcular precios"""
    
    @abstractmethod
    def calcular_precio(self, restaurante: dict) -> float:
        """Calcula el precio del combo en un restaurante"""
        pass
    
    @abstractmethod
    def obtener_aplicaciones(self) -> List[str]:
        """Retorna lista de modificadores aplicados"""
        pass


class PrecioBase(CalculadorPrecio):
    """Implementación base: calcula precio desde datos del restaurante"""
    
    def calcular_precio(self, restaurante: Dict) -> float:
        total: float = 0.0
        
        for id_comida, comida in restaurante["comidas_combo"].items():
            total += comida['precio_comida']
            total += sum(comida['precio_ingredientes'])
            
        '''for id_ingrediente, ingrediente in restaurante["ingredientes"]:
            total += ingrediente['precio']
        '''
        return total
    
    def obtener_aplicaciones(self) -> List[str]:
        return ["precio_base"]


class ModificadorPrecio(CalculadorPrecio):
    """Decorator base para modificar precios"""
    
    def __init__(self, calculador: CalculadorPrecio):
        self._calculador = calculador
    
    def calcular_precio(self, restaurante: dict) -> float:
        return self._calculador.calcular_precio(restaurante)
    
    def obtener_aplicaciones(self) -> List[str]:
        return self._calculador.obtener_aplicaciones()