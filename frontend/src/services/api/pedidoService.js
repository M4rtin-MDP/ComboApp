import api from '../api.js';

export const pedidoService = {
  /**
   * Crea un pedido completo con todos sus combos, comidas e ingredientes
   * @param {Object} datos - Datos del pedido
   * @returns {Promise<Object>} - { success, data, message }
   */
  crearPedidoCompleto: async (datos) => {
    const { id_usuario, id_restaurante, total, carrito } = datos;

    try {
      // PASO 1: Crear el pedido principal
      console.log('Paso 1: Creando pedido...');
      const pedidoPayload = {
        id_usuario,
        id_restaurante,
        id_estado: 1, // 1 = Pendiente
        fecha: new Date().toISOString(),
        total
      };

      const pedidoResponse = await api.post('/pedidos', pedidoPayload);
      const id_pedido = pedidoResponse.data.id_pedido || pedidoResponse.data;
      
      console.log('Pedido creado con ID:', id_pedido);

      // PASO 2: Por cada item del carrito, crear combo y sus relaciones
      console.log('Paso 2: Creando combos...');

      // 2.1: Crear combo
      const comboPayload = { id_pedido };
      const comboResponse = await api.post(`/combos/${id_pedido}`, comboPayload);
      
      for (const item of carrito) {
        
        const id_combo = comboResponse.data.id_combo || comboResponse.data;
        console.log(`Combo creado con ID: ${id_combo} para ${item.comida.nombre}`);

        // 2.2: Asociar la comida al combo
        const comidaPayload = {
          id_combo: id_combo,
          id_comida: item.comida.id_comida
        };
        console.log(comidaPayload);
        
        // Guardo el item comida 
        const itemComidaResponse = await api.post('/combos/items_comidas/', comidaPayload);
        console.log(`  Comida ${item.comida.nombre} asociada al combo`);

        // 2.3: Asociar cada ingrediente al combo
        for (const ingrediente of item.ingredientes) {
          const ingredientePayload = {
            item_comida: itemComidaResponse.data.item_comida || itemComidaResponse.data,
            id_ingrediente: ingrediente.id_ingrediente
          };
          await api.post('/combos/items_ingredientes/', ingredientePayload);
          console.log(`  Ingrediente ${ingrediente.nombre} asociado al combo`);
        }
      }

      console.log('Pedido completo creado exitosamente!');

      return {
        success: true,
        data: { id_pedido },
        message: 'Pedido creado exitosamente'
      };

    } catch (error) {
      console.error('Error al crear el pedido:', error);
      return {
        success: false,
        data: null,
        message: error.response?.data?.message || 'Error al crear el pedido'
      };
    }
  },


  /**
   * Obtiene todos los pedidos de un usuario
   * @param {number} id_usuario - ID del usuario
   * @returns {Promise<Object>} - { success, data, message }
   */
  getPedidosUsuario: async (id_usuario) => {
    try {
      const response = await api.get(`/pedidos/usuario/${id_usuario}`);
      return {
        success: true,
        data: response.data,
        message: 'Pedidos obtenidos exitosamente'
      };
    } catch (error) {
      console.error('Error al obtener pedidos del usuario:', error);
      return {
        success: false,
        data: [],
        message: error.response?.data?.message || 'Error al obtener los pedidos'
      };
    }
  },

  /**
   * Obtiene el detalle de combos de un pedido
   * @param {number} id_pedido - ID del pedido
   * @returns {Promise<Object>} - { success, data, message }
   */
  getDetalleCombosPedido: async (id_pedido) => {
    try {
      const response = await api.get(`/combos/pedido/${id_pedido}`);
      return {
        success: true,
        data: response.data,
        message: 'Detalle de combos obtenido exitosamente'
      };
    } catch (error) {
      console.error('Error al obtener detalle de combos:', error);
      return {
        success: false,
        data: [],
        message: error.response?.data?.message || 'Error al obtener el detalle'
      };
    }
  }
};


export default pedidoService;