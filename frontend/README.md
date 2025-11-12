# Frontend Structure (React.js)

## Estructura de Carpetas

```
📦 my-app/
│
├── 📁 src/
│   ├── 📁 assets/             # Imágenes, íconos, fuentes, etc.
│   ├── 📁 components/         # Componentes reutilizables (botones, cards, modales...)
│   ├── 📁 features/           # Módulos o dominios del negocio (auth, users, products, etc.)
│   ├── 📁 hooks/              # Custom hooks (useFetch, useAuth, etc.)
│   ├── 📁 layouts/            # Layouts globales (Navbar, Sidebar, DashboardLayout, etc.)
│   ├── 📁 pages/              # Páginas principales (Home, Login, Dashboard, etc.)
│   ├── 📁 routes/             # Configuración del router (React Router)
│   ├── 📁 services/           # Lógica de conexión a APIs o servicios externos
│   ├── 📁 store/              # Gestión de estado global (Zustand, Redux, Context API)
│   ├── 📁 utils/              # Funciones auxiliares, constantes, formateadores
│   ├── 📁 styles/             # Archivos de estilo global (CSS, SCSS, Tailwind config, etc.)
│   ├── main.jsx               # Punto de entrada de React (renderiza <App />)
│   ├── App.jsx                # Raíz del componente principal
│   └── index.css              # Estilos globales o importación base de Tailwind
│
├── 📁 public/                 # Archivos estáticos públicos
│   └── favicon.ico
│
├── .env                       # Variables de entorno
├── .eslintrc.cjs              # Configuración de linting
├── .prettierrc                # Configuración de formato
├── vite.config.js             # Configuración de Vite
├── package.json
└── README.md

```

## Descripción de Componentes

## public/
Contenido: Archivos estáticos que no cambian (favicon, robots.txt, imágenes públicas, etc.).

## Stack Tecnológico Recomendado

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "@reduxjs/toolkit": "^2.0.1",
    "react-redux": "^9.0.4",
    "axios": "^1.6.2",
    "react-hook-form": "^7.49.2",
    "zod": "^3.22.4",
    "@hookform/resolvers": "^3.3.2"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.1",
    "vite": "^5.0.8",
    "eslint": "^8.55.0",
    "prettier": "^3.1.1",
    "tailwindcss": "^3.3.6",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32"
  }
}
```

## Alternativas de Estado Global

### Opción 1: Redux Toolkit (Recomendado para apps grandes)
```javascript
// store/store.js
import { configureStore } from '@reduxjs/toolkit';
import authReducer from '../features/auth/authSlice';
import userReducer from '../features/users/userSlice';

export const store = configureStore({
  reducer: {
    auth: authReducer,
    users: userReducer,
  },
});
```

### Opción 2: Context API (Para apps pequeñas/medianas)
```javascript
// context/AuthContext.jsx
import { createContext, useState, useContext } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  // ... lógica
  return (
    <AuthContext.Provider value={{ user, setUser }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
```

## Comandos Útiles

```bash
# Instalar dependencias
npm install

# Ejecutar en desarrollo
npm run dev

# Build para producción
npm run build

# Preview del build
npm run preview

# Linting
npm run lint

# Formatear código
npm run format

# Ejecutar tests
npm test
```

## Variables de Entorno (.env.example)

```bash
VITE_API_URL=http://localhost:8000/api/v1
VITE_APP_NAME=My App
VITE_ENV=development
```

## Configuración de Axios

```javascript
// src/api/axios.js
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para agregar token
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

// Interceptor para manejar errores
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Redirect to login
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
```

