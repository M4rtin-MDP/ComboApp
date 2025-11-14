import apiClient from '../api.js';

export const categoriaService = {
  // Obtener todas las categorías (comida, bebida, postres)
  getCategorias: async () => {
    try {
      const response = await apiClient.get('/categorias');
      return {
        success: true,
        data: response.data
      };
    } catch (error) {
      return {
        success: false,
        message: error.response?.data?.message || 'Error al obtener categorías'
      };
    }
  },

  // Obtener comidas por categoría
  getComidasByCategoria: async (categoriaId) => {
    try {
      const response = await apiClient.get(`/comidas/categorias/${categoriaId}`);
      return {
        success: true,
        data: response.data
      };
    } catch (error) {
      return {
        success: false,
        message: error.response?.data?.message || 'Error al obtener comidas'
      };
    }
  }



};