from abc import ABC, abstractmethod
from typing import List


class CalculadorPrecio(ABC):
    """Interface para calcular precios"""
    
    @abstractmethod
    def calcular_precio(self, restaurante: dict, combo: dict) -> float:
        """Calcula el precio del combo en un restaurante"""
        pass
    
    @abstractmethod
    def obtener_aplicaciones(self) -> List[str]:
        """Retorna lista de modificadores aplicados"""
        pass


class PrecioBase(CalculadorPrecio):
    """Implementación base: calcula precio desde datos del restaurante"""
    
    def calcular_precio(self, restaurante: dict, combo: dict) -> float:
        total = 0.0
        
        for id_comida, comida_sol in combo["comidas"].items():
            comida_key = str(id_comida)
            
            # Precio de la comida
            if comida_key in restaurante["comidas"]:
                total += restaurante["comidas"][comida_key]["precio"]
            
            # Precio de ingredientes adicionales
            for ingrediente in comida_sol.get("ingredientes", []):
                if ingrediente in restaurante.get("ingredientes", {}):
                    total += restaurante["ingredientes"][ingrediente]["precio"]
        
        return total
    
    def obtener_aplicaciones(self) -> List[str]:
        return ["Precio base"]


class ModificadorPrecio(CalculadorPrecio):
    """Decorator base para modificar precios"""
    
    def __init__(self, calculador: CalculadorPrecio):
        self._calculador = calculador
    
    def calcular_precio(self, restaurante: dict, combo: dict) -> float:
        return self._calculador.calcular_precio(restaurante, combo)
    
    def obtener_aplicaciones(self) -> List[str]:
        return self._calculador.obtener_aplicaciones()