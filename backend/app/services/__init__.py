# app/services/__init__.py
"""
Auto-discovery: Importa automáticamente todos los módulos de services
"""
'''import importlib
import pkgutil
from pathlib import Path


def auto_register_services():
    """Importa todos los módulos en services/ para registrar clases"""
    services_path = Path(__file__).parent
    
    for _, module_name, _ in pkgutil.iter_modules([str(services_path)]):
        # Importa cada módulo encontrado
        try:
            importlib.import_module(f"app.services.{module_name}")
            print(f"✓ Registrado módulo: {module_name}")
        except Exception as e:
            print(f"✗ Error al importar {module_name}: {e}")


# Ejecutar auto-discovery al importar este módulo
auto_register_services()'''