// src/services/api/restauranteService.js
import apiClient from '../api.js';

export const restauranteService = {
  /**
   * Obtiene restaurantes disponibles según el pedido
   * @param {Array} pedido - Array con las comidas e ingredientes seleccionados
   * @returns {Promise<Object>} - { success, data, message }
   */
  getRestaurantesDisponibles: async (pedido) => {
    try {
      // Transformar el carrito al formato que espera el backend
      const payload = pedido.map(item => ({
        id_comida: item.comida.id_comida,
        nombre: item.comida.nombre,
        id_ingrediente: item.ingredientes.map(ing => ing.id_ingrediente),
        ingredientes: item.ingredientes.map(ing => ing.nombre)
      }));

      console.log('Payload enviado:', payload);

      const response = await apiClient.post('/restaurantes/disponibles_total', payload);
      
      return {
        success: true,
        data: response.data,
        message: 'Restaurantes obtenidos exitosamente'
      };
    } catch (error) {
      console.error('Error al obtener restaurantes disponibles:', error);
      return {
        success: false,
        data: [],
        message: error.response?.data?.message || 'Error al buscar restaurantes disponibles'
      };
    }
  },

  /**
   * Obtiene los detalles de un restaurante por su ID
   * @param {number} id_restaurante - ID del restaurante
   * @returns {Promise<Object>} - { success, data, message }
   */
  getRestauranteById: async (id_restaurante) => {
    try {
      const response = await api.get(`/restaurantes/restaurantes_json/${id_restaurante}`);
      return {
        success: true,
        data: response.data,
        message: 'Restaurante obtenido exitosamente'
      };
    } catch (error) {
      console.error('Error al obtener restaurante:', error);
      return {
        success: false,
        data: null,
        message: error.response?.data?.message || 'Error al obtener el restaurante'
      };
    }
  }
};



export default restauranteService;