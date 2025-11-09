import httpx
'''
Ejemplo simbolico del uso de la API con otros restaurantes reales
'''
class RestauranteAPIRepository(RestauranteRepository):
    """Implementación: consulta API externa"""
    
    def __init__(self, api_url: str):
        self.api_url = api_url
    
    async def obtener_catalogo_completo(self) -> List[Dict]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.api_url}/restaurants")
            return response.json()
    
    async def obtener_restaurante_por_id(self, id: int) -> Dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.api_url}/restaurants/{id}")
            return response.json()