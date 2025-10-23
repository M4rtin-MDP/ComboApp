# Frontend Structure (React.js)

## Estructura de Carpetas

```
frontend/
├── public/
│   ├── index.html
│   ├── favicon.ico
│   └── assets/                          # Imágenes estáticas, iconos
│
├── src/
│   ├── api/
│   │   ├── axios.js                     # Configuración de Axios (interceptors, base URL)
│   │   ├── authApi.js                   # Endpoints de autenticación
│   │   ├── userApi.js                   # Endpoints de usuarios
│   │   └── itemApi.js                   # Endpoints de items
│   │
│   ├── assets/
│   │   ├── images/                      # Imágenes del proyecto
│   │   ├── icons/                       # Iconos SVG
│   │   └── styles/                      # Estilos globales
│   │       ├── globals.css
│   │       └── variables.css
│   │
│   ├── components/
│   │   ├── common/                      # Componentes reutilizables
│   │   │   ├── Button/
│   │   │   │   ├── Button.jsx
│   │   │   │   ├── Button.module.css    # CSS Modules (opcional)
│   │   │   │   └── index.js             # Re-export
│   │   │   ├── Input/
│   │   │   │   ├── Input.jsx
│   │   │   │   └── index.js
│   │   │   ├── Modal/
│   │   │   │   ├── Modal.jsx
│   │   │   │   └── index.js
│   │   │   ├── Loader/
│   │   │   │   ├── Loader.jsx
│   │   │   │   └── index.js
│   │   │   └── Card/
│   │   │       ├── Card.jsx
│   │   │       └── index.js
│   │   │
│   │   └── layout/                      # Componentes de layout
│   │       ├── Navbar/
│   │       │   ├── Navbar.jsx
│   │       │   └── index.js
│   │       ├── Sidebar/
│   │       │   ├── Sidebar.jsx
│   │       │   └── index.js
│   │       ├── Footer/
│   │       │   ├── Footer.jsx
│   │       │   └── index.js
│   │       └── Layout/
│   │           ├── Layout.jsx           # Wrapper principal
│   │           └── index.js
│   │
│   ├── pages/                           # Páginas/Vistas principales
│   │   ├── Home/
│   │   │   ├── Home.jsx
│   │   │   └── index.js
│   │   ├── Login/
│   │   │   ├── Login.jsx
│   │   │   └── index.js
│   │   ├── Register/
│   │   │   ├── Register.jsx
│   │   │   └── index.js
│   │   ├── Dashboard/
│   │   │   ├── Dashboard.jsx
│   │   │   └── index.js
│   │   ├── Profile/
│   │   │   ├── Profile.jsx
│   │   │   └── index.js
│   │   └── NotFound/
│   │       ├── NotFound.jsx
│   │       └── index.js
│   │
│   ├── features/                        # Lógica por módulo (Redux Toolkit)
│   │   ├── auth/
│   │   │   ├── authSlice.js             # Redux slice
│   │   │   └── authThunks.js            # Acciones asíncronas
│   │   ├── users/
│   │   │   ├── userSlice.js
│   │   │   └── userThunks.js
│   │   └── items/
│   │       ├── itemSlice.js
│   │       └── itemThunks.js
│   │
│   ├── hooks/                           # Custom hooks
│   │   ├── useAuth.js                   # Hook de autenticación
│   │   ├── useDebounce.js               # Debounce personalizado
│   │   ├── useLocalStorage.js           # Manejo de localStorage
│   │   └── useFetch.js                  # Hook genérico para fetch
│   │
│   ├── context/                         # Context API (alternativa a Redux)
│   │   ├── AuthContext.jsx
│   │   └── ThemeContext.jsx
│   │
│   ├── routes/
│   │   ├── AppRoutes.jsx                # Configuración de todas las rutas
│   │   ├── PrivateRoute.jsx             # Rutas protegidas
│   │   └── PublicRoute.jsx              # Rutas públicas
│   │
│   ├── store/                           # Redux store
│   │   └── store.js                     # Configuración del store
│   │
│   ├── utils/
│   │   ├── constants.js                 # Constantes globales
│   │   ├── helpers.js                   # Funciones auxiliares
│   │   ├── validators.js                # Validaciones
│   │   └── formatters.js                # Formateo de datos
│   │
│   ├── App.jsx                          # Componente principal
│   ├── App.css
│   ├── index.jsx                        # Entry point
│   └── index.css                        # Estilos globales
│
├── .env                                 # Variables de entorno (NO commitear)
├── .env.example                         # Ejemplo de variables
├── .gitignore
├── package.json
├── package-lock.json
├── vite.config.js                       # Configuración de Vite
├── eslint.config.js                     # Configuración de ESLint
├── prettier.config.js                   # Configuración de Prettier
├── Dockerfile
└── README.md
```

## Descripción de Componentes

### `src/api/`
Capa de comunicación con el backend. Centraliza todas las llamadas HTTP.

### `src/components/`
- **common/**: Componentes reutilizables en toda la app
- **layout/**: Componentes estructurales (Navbar, Footer, etc.)

### `src/pages/`
Componentes de nivel superior que representan páginas completas.

### `src/features/`
Arquitectura por features usando Redux Toolkit. Cada feature tiene su slice y lógica.

### `src/hooks/`
Custom hooks para reutilizar lógica entre componentes.

### `src/routes/`
Configuración de React Router con rutas protegidas y públicas.

### `src/store/`
Configuración del store de Redux con todos los reducers.

### `src/utils/`
Funciones de utilidad, constantes y helpers.

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