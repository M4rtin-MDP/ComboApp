import pytest
import sys
import os
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

class TestDataValidation:
    """Tests para validar los datos base de la aplicación usando sus endpoints"""
    
    def test_categorias(self):
        """Verificar que las categorías 1, 2, 3 son Bebida, Comida, Postre"""
        response = client.get("/api/v1/categorias/")
        assert response.status_code == 200
        
        categorias = response.json()
        
        # Buscar las categorías por ID
        cat_1 = next((cat for cat in categorias if cat["id_categoria"] == 1), None)
        cat_2 = next((cat for cat in categorias if cat["id_categoria"] == 2), None)
        cat_3 = next((cat for cat in categorias if cat["id_categoria"] == 3), None)
        
        # Verificar que existen
        assert cat_1 is not None, "Categoría 1 (Bebida) no encontrada"
        assert cat_2 is not None, "Categoría 2 (Comida) no encontrada"
        assert cat_3 is not None, "Categoría 3 (Postre) no encontrada"
        
        # Verificar nombres
        assert cat_1["nombre"].lower() == "bebida", f"Esperado 'bebida', obtenido '{cat_1['nombre']}'"
        assert cat_2["nombre"].lower() == "comida", f"Esperado 'comida', obtenido '{cat_2['nombre']}'"
        assert cat_3["nombre"].lower() == "postre", f"Esperado 'postre', obtenido '{cat_3['nombre']}'"
        
        print(f"Categorías verificadas: {cat_1['nombre']}, {cat_2['nombre']}, {cat_3['nombre']}")
    
    def test_comida_base(self):
        """Verificar que comida_base con id 1 es hamburguesa y categoría 2"""
        response = client.get("/api/v1/comidas/1")
        assert response.status_code == 200
        
        comida_1 = response.json()
        
        assert comida_1 is not None, "Comida con ID 1 no encontrada"
        
        # Verificar que es hamburguesa y categoría 2
        assert comida_1["nombre"].lower() == "hamburguesa", f"Esperado 'hamburguesa', obtenido '{comida_1['nombre']}'"
        categoria_field = None
        for field in ['id_categoria']:
            if field in comida_1:
                categoria_field = field
                break
        
        if categoria_field:
            assert comida_1[categoria_field] == 2, f"Esperado categoría 2 (Comida), obtenida {comida_1[categoria_field]}'"
        
        print(f"Comida 1 verificada: {comida_1['nombre']}")
    
    def test_estado(self):
        """Verificar que estado con id 1 es 'pendiente'"""
        response = client.get("/api/v1/estados/1")
        assert response.status_code == 200
        
        estado_1 = response.json()
        
        assert estado_1 is not None, "Estado 1 (pendiente) no encontrado"
        
        # Verificar nombre
        assert estado_1["nombre"].lower() == "pendiente", f"Esperado 'pendiente', obtenido '{estado_1['nombre']}'"
        
        print(f"Estado 1 verificado: {estado_1['nombre']}")
    
    def test_ingrediente(self):
        """Verificar que ingrediente con id 1 es 'tomate'"""
        response = client.get("/api/v1/ingredientes/1")
        assert response.status_code == 200
        
        ingr_1 = response.json()
        assert ingr_1 is not None, "Ingrediente 1 (tomate) no encontrado"
        
        # Verificar nombre
        assert ingr_1["nombre"].lower() == "tomate", f"Esperado 'tomate', obtenido '{ingr_1['nombre']}'"
        
        print(f"Ingrediente 1 verificado: {ingr_1['nombre']}")
    
    def test_ingrediente_comida(self):
        """Verificar que existe una relación entre hamburguesa (comida 1) y tomate (ingrediente 1)"""
        response = client.get("/api/v1/ingredientes_comida/1")
        assert response.status_code == 200
        
        ingredientes_comida_1 = response.json()
        
        # Verificar que es una lista
        assert isinstance(ingredientes_comida_1, list), f"Se esperaba una lista, se obtuvo: {type(ingredientes_comida_1)}"
        
        # Buscar el ingrediente con id_ingrediente = 1 (tomate)
        tomate_en_hamburguesa = next(
            (ing for ing in ingredientes_comida_1 if ing["id_ingrediente"] == 1), 
            None
        )
        
        assert tomate_en_hamburguesa is not None, "Tomate (ingrediente 1) no encontrado en hamburguesa (comida 1)"
        
        # Verificar que el nombre es tomate
        assert tomate_en_hamburguesa["nombre"].lower() == "tomate", \
            f"Esperado 'tomate', obtenido '{tomate_en_hamburguesa['nombre']}'"
        
        print(f"Relación directa verificada: Hamburguesa (comida 1) ↔ {tomate_en_hamburguesa['nombre']} (ingrediente 1)")

class TestDataConsistency:
    """Tests adicionales para consistencia de datos"""
    
    def test_categorias_orden_correcto(self):
        """Verificar que las categorías están en el orden correcto"""
        response = client.get("/api/v1/categorias/")
        categorias = response.json()
        
        # Ordenar por ID para asegurar orden
        categorias_ordenadas = sorted(categorias, key=lambda x: x["id_categoria"])
        
        expected_names = ["bebida", "comida", "postre"]
        for i, expected_name in enumerate(expected_names, 1):
            assert categorias_ordenadas[i-1]["id_categoria"] == i
            assert categorias_ordenadas[i-1]["nombre"].lower() == expected_name
        
        print("Orden de categorías verificado correctamente")
    
    def test_comida_pertenece_a_categoria_existente(self):
        """Verificar que todas las comidas pertenecen a categorías existentes"""
        response_comidas = client.get("/api/v1/comidas/")
        response_categorias = client.get("/api/v1/categorias/")
        
        assert response_comidas.status_code == 200
        assert response_categorias.status_code == 200
        
        comidas = response_comidas.json()
        categorias = response_categorias.json()
        
        # Extraer IDs de categorías existentes
        categorias_ids = {cat["id_categoria"] for cat in categorias}
        
        # Primero inspeccionar la estructura de una comida
        if comidas:
            sample_comida = comidas[0]
            print(f"🔍 Campos de una comida: {list(sample_comida.keys())}")
        
        # Buscar el campo de categoría en las comidas
        categoria_field = None
        for field in ['id_categoria']:
            if comidas and field in comidas[0]:
                categoria_field = field
                break
        
        if categoria_field:
            for comida in comidas:
                assert comida[categoria_field] in categorias_ids, \
                    f"Comida {comida['id_comida']} ({comida['nombre']}) tiene categoría inválida: {comida[categoria_field]}"
            print(f"Consistencia de categorías verificada para {len(comidas)} comidas (campo: {categoria_field})")
        else:
            print("No se pudo verificar consistencia de categorías - campo no encontrado")
            # Mostrar los campos disponibles para debugging
            if comidas:
                print(f"   Campos disponibles: {list(comidas[0].keys())}")

