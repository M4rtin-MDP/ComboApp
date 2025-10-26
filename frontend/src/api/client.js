import axios from 'axios'
import.meta.url

const API_URL = import.meta.env.VITE_API_URL;


// Crear instancia de axios
const api = axios.create({ 
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});


// Interceptor para agregar el token automáticamente
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token'); 
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);


// Interceptor para manejar errores globalmente (opcional)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expirado o inválido
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);


// Auth
export const register = (data) => api.post('/auth/register', data);
export const login = (data) => api.post('/auth/login', data);

// Ingredientes
export const getIngredients = () => api.get('/ingredientes');

// Combos
export const getCombos = () => api.get('/combos');
export const createCombo = (data) => api.post('/combos', data);

export default api