import apiClient from '../api.js';

export const ingredientesService = {
  // Obtener ingredientes por ID de comida
  getIngredientesByComida: async (comidaId) => {
    try {
      const response = await apiClient.get(`/ingredientes_comida/${comidaId}`);
      return {
        success: true,
        data: response.data
      };
    } catch (error) {
      return {
        success: false,
        data: []
      };
    }
  }



};


