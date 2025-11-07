

class Bebida(Producto):
    # crearle un identificador para luego comparar con los datos de cada restaurante (ver si estan disponibles y recibir el precio)
    def __init__(self) -> None:
        super().__init__(CategoriaProducto.COMIDA)
        
    def get_categoria(self):
        return self._categoria

    def get_id(self):
        # return 
        pass