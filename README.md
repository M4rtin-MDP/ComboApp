# Proyecto

Aplicación de armado y pedido de combos full-stack con FastAPI y React.js.

## Autores

- Joaquín Miguel - [@joaquin-miguel](https://github.com/joaquin-miguel)
- Hernán Pablo De Lorenzo - [@HernanPabloDL](https://github.com/HernanPabloDL)
- Martín Marques de Paiva - [@M4rtin-MDP](https://github.com/M4rtin-MDP)

## Stack

### Backend
- FastAPI
- Supabase (PostgreSQL)
- SQLAlchemy
- Pydantic

### Frontend
- React 18
- Vite
- Redux Toolkit
- React Router
- Axios

## Requisitos Previos

- Docker & Docker Compose
- Python 3.12+
- Node.js 18+
- Git

## 📚 Documentación

- [Estructura Backend](./backend/README.md)
- [Estructura Frontend](./frontend/README.md)
- [API Documentation](./docs/api.md)
- [Setup Guide](./docs/setup.md)


## Docker
```
# Verificar que Docker responde
docker ps

# Construir tu proyecto
docker compose build

# Levantar todo
docker compose up -d

# Ver logs
docker compose logs -f
```

# Estructura del Proyecto

```
combo_app/
├── backend/                             # Ver: Backend Structure
│   ├── app/
│   ├── tests/
│   ├── .env
│   ├── .env.example
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
│
├── frontend/                            # Ver: Frontend Structure
│   ├── public/
│   ├── src/
│   ├── index.html
│   ├── .env
│   ├── .env.example
│   ├── package.json
│   ├── vite.config.js
│   ├── Dockerfile
│   └── README.md
│
├── .github/
│   └── workflows/
│       ├── backend-ci.yml               # CI/CD para backend
│       ├── frontend-ci.yml              # CI/CD para frontend
│       └── deploy.yml                   # Deploy completo
│
├── docs/                                # Documentación del proyecto
│   ├── api.md                           # Documentación de API
│   └── setup.md                         # Guía de instalación
│
├── .gitignore                           # Gitignore global
├── docker-compose.yml                   # Desarrollo local
├── docker-compose.prod.yml              # Producción
└── README.md                            # Documentación principal
```