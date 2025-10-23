import axios from 'axios'

const API_URL = "http://127.0.0.1:8000"

const api = axios.create({ baseURL: API_URL })

export const register = data => api.post("/auth/register", data)
export const login = data => api.post("/auth/login", data)
export const getIngredients = token => api.get("/ingredients", { headers: { Authorization: `Bearer ${token}` } })
export const getCombos = token => api.get("/combos", { headers: { Authorization: `Bearer ${token}` } })
export const createCombo = (data, token) =>
  api.post("/combos", data, { headers: { Authorization: `Bearer ${token}` } })

export default api