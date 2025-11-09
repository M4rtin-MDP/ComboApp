from .precio import ModificadorPrecio
from typing import List

class DescuentoCombo(ModificadorPrecio):
    """Aplica 10% descuento si hay 2 o más comidas"""
    
    def __init__(self, calculador, porcentaje: float = 0.10):
        super().__init__(calculador)
        self.porcentaje = porcentaje
    
    def calcular_precio(self, restaurante: dict, combo: dict) -> float:
        precio = self._calculador.calcular_precio(restaurante, combo)
        
        if len(combo["comidas"]) >= 2:
            return precio * (1 - self.porcentaje)
        
        return precio
    
    def obtener_aplicaciones(self) -> List[str]:
        apps = self._calculador.obtener_aplicaciones()
        # Solo agregar si realmente se aplicó
        # (se podría mejorar pasando el combo como contexto)
        apps.append(f"Descuento combo -{int(self.porcentaje * 100)}%")
        return apps


class AplicarIVA(ModificadorPrecio):
    """Aplica IVA al precio"""
    
    def __init__(self, calculador, porcentaje: float = 0.21):
        super().__init__(calculador)
        self.porcentaje = porcentaje
    
    def calcular_precio(self, restaurante: dict, combo: dict) -> float:
        precio = self._calculador.calcular_precio(restaurante, combo)
        return precio * (1 + self.porcentaje)
    
    def obtener_aplicaciones(self) -> List[str]:
        apps = self._calculador.obtener_aplicaciones()
        apps.append(f"IVA +{int(self.porcentaje * 100)}%")
        return apps


class CargoEnvio(ModificadorPrecio):
    """Agrega cargo fijo por envío"""
    
    def __init__(self, calculador, cargo: float = 500.0):
        super().__init__(calculador)
        self.cargo = cargo
    
    def calcular_precio(self, restaurante: dict, combo: dict) -> float:
        precio = self._calculador.calcular_precio(restaurante, combo)
        return precio + self.cargo
    
    def obtener_aplicaciones(self) -> List[str]:
        apps = self._calculador.obtener_aplicaciones()
        apps.append(f"Cargo envío +${self.cargo:.0f}")
        return apps


class DescuentoPrimeraCompra(ModificadorPrecio):
    """Descuento para nuevos clientes"""
    
    def __init__(self, calculador, porcentaje: float = 0.15):
        super().__init__(calculador)
        self.porcentaje = porcentaje
    
    def calcular_precio(self, restaurante: dict, combo: dict) -> float:
        precio = self._calculador.calcular_precio(restaurante, combo)
        return precio * (1 - self.porcentaje)
    
    def obtener_aplicaciones(self) -> List[str]:
        apps = self._calculador.obtener_aplicaciones()
        apps.append(f"Primera compra -{int(self.porcentaje * 100)}%")
        return apps


class DescuentoPorcentual(ModificadorPrecio):
    """Descuento genérico por porcentaje"""
    
    def __init__(self, calculador, porcentaje: float, nombre: str):
        super().__init__(calculador)
        self.porcentaje = porcentaje
        self.nombre = nombre
    
    def calcular_precio(self, restaurante: dict, combo: dict) -> float:
        precio = self._calculador.calcular_precio(restaurante, combo)
        return precio * (1 - self.porcentaje)
    
    def obtener_aplicaciones(self) -> List[str]:
        apps = self._calculador.obtener_aplicaciones()
        apps.append(f"{self.nombre} -{int(self.porcentaje * 100)}%")
        return apps