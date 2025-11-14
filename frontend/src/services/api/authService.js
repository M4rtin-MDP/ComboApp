// src/services/api/authService.js
import apiClient from '../api.js';

export const authService = {
  // Login
  login: async (credentials) => {
    try {
      // Ajusta la ruta según tu backend
      const response = await apiClient.post('/auth/login', credentials);
      
      // Guarda el token
      if (response.data.token) {
        localStorage.setItem('token', response.data.token);
      }
      
      return {
        success: true,
        user: response.data.user,
        token: response.data.token
      };
    } catch (error) {
      return {
        success: false,
        message: error.response?.data?.message || 'Error al iniciar sesión'
      };
    }
  },

  /**
   * Registra un nuevo usuario
   * @param {Object} userData - { nombre, direccion, email, contrasena }
   * @returns {Promise<Object>} - { success, data, message }
   */
  register: async (userData) => {
    try {
      const response = await apiClient.post('/auth/register', userData);

      return {
        success: true,
        data: response.data, // { access_token, token_type, user }
        message: 'Usuario registrado exitosamente'
      };
    } catch (error) {
      console.error('Error en registro:', error);
      return {
        success: false,
        data: null,
        message: error.response?.data?.detail || 'Error al registrar usuario'
      };
    }
  },

  // Obtener usuario actual (para verificar si el token es válido)
  getCurrentUser: async () => {
    try {
      const response = await apiClient.get('/auth/me');
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Logout
  logout: async () => {
    try {
      await apiClient.post('/auth/logout');
    } catch (error) {
      console.error('Error en logout:', error);
    } finally {
      localStorage.removeItem('token');
    }
  }
};