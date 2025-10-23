# Root Project Structure

## Estructura Completa del Proyecto

```
combo_app/
├── backend/                             # Ver: Backend Structure
│   ├── app/
│   ├── alembic/
│   ├── tests/
│   ├── scripts/
│   ├── .env
│   ├── .env.example
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
│
├── frontend/                            # Ver: Frontend Structure
│   ├── public/
│   ├── src/
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
│   ├── setup.md                         # Guía de instalación
│   └── architecture.md                  # Arquitectura del sistema
│
├── scripts/                             # Scripts de utilidad del proyecto
│   ├── setup.sh                         # Setup inicial del proyecto
│   ├── dev.sh                           # Levantar entorno de desarrollo
│   └── deploy.sh                        # Script de deployment
│
├── .gitignore                           # Gitignore global
├── docker-compose.yml                   # Desarrollo local
├── docker-compose.prod.yml              # Producción
├── Makefile                             # Comandos útiles
├── README.md                            # Documentación principal
└── LICENSE
```

## docker-compose.yml (Desarrollo)

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    container_name: backend-dev
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/mydb
      - SECRET_KEY=dev-secret-key-change-in-production
      - ENVIRONMENT=development
    volumes:
      - ./backend:/app
      - /app/venv
    depends_on:
      - db
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

  frontend:
    build: ./frontend
    container_name: frontend-dev
    ports:
      - "3000:3000"
    environment:
      - VITE_API_URL=http://localhost:8000/api/v1
    volumes:
      - ./frontend:/app
      - /app/node_modules
    stdin_open: true
    tty: true
    command: npm run dev -- --host

  db:
    image: postgres:15-alpine
    container_name: postgres-dev
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  pgadmin:
    image: dpage/pgadmin4
    container_name: pgadmin-dev
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=admin
    ports:
      - "5050:80"
    depends_on:
      - db

volumes:
  postgres_data:
```

## Makefile

```makefile
.PHONY: help install dev stop clean test lint format

help:
	@echo "Comandos disponibles:"
	@echo "  make install    - Instalar dependencias"
	@echo "  make dev        - Levantar entorno de desarrollo"
	@echo "  make stop       - Detener contenedores"
	@echo "  make clean      - Limpiar contenedores y volúmenes"
	@echo "  make test       - Ejecutar tests"
	@echo "  make lint       - Ejecutar linters"
	@echo "  make format     - Formatear código"

install:
	@echo "Instalando dependencias del backend..."
	cd backend && python -m venv venv && . venv/bin/activate && pip install -r requirements.txt
	@echo "Instalando dependencias del frontend..."
	cd frontend && npm install

dev:
	@echo "Levantando entorno de desarrollo..."
	docker-compose up -d

stop:
	@echo "Deteniendo contenedores..."
	docker-compose down

clean:
	@echo "Limpiando contenedores, volúmenes e imágenes..."
	docker-compose down -v --rmi local

test:
	@echo "Ejecutando tests del backend..."
	cd backend && pytest
	@echo "Ejecutando tests del frontend..."
	cd frontend && npm test

lint:
	@echo "Ejecutando linter en backend..."
	cd backend && flake8 app
	@echo "Ejecutando linter en frontend..."
	cd frontend && npm run lint

format:
	@echo "Formateando código del backend..."
	cd backend && black app && isort app
	@echo "Formateando código del frontend..."
	cd frontend && npm run format
```

## .gitignore (Root)

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/
env/
.venv

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*
dist/
build/
.next/
out/

# Environment variables
.env
.env.local
.env.*.local

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Testing
.coverage
htmlcov/
.pytest_cache/
coverage/

# Logs
*.log
logs/

# Database
*.db
*.sqlite3

# Docker
docker-compose.override.yml
```

## README.md Principal

```markdown
# My Fullstack Project

Aplicación full-stack con FastAPI (Backend) y React.js (Frontend).

## 🚀 Stack Tecnológico

### Backend
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic

### Frontend
- React 18
- Vite
- Redux Toolkit
- React Router
- Axios

## 📋 Requisitos Previos

- Docker & Docker Compose
- Python 3.11+
- Node.js 18+
- Git

## 🛠️ Instalación y Configuración

### Opción 1: Con Docker (Recomendado)

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/my-fullstack-project.git
cd my-fullstack-project
```

2. Copiar archivos de ejemplo:
```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

3. Levantar servicios:
```bash
docker-compose up -d
```

4. Acceder a:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- PgAdmin: http://localhost:5050

### Opción 2: Local (Sin Docker)

1. Backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
uvicorn app.main:app --reload
```

2. Frontend:
```bash
cd frontend
npm install
npm run dev
```

## 📚 Documentación

- [Backend Structure](./backend/README.md)
- [Frontend Structure](./frontend/README.md)
- [API Documentation](./docs/api.md)
- [Setup Guide](./docs/setup.md)

## 🧪 Testing

```bash
# Tests del backend
cd backend && pytest

# Tests del frontend
cd frontend && npm test

# O usando Makefile
make test
```

## 🔧 Comandos Útiles

```bash
make dev          # Levantar entorno de desarrollo
make stop         # Detener contenedores
make clean        # Limpiar todo
make test         # Ejecutar tests
make lint         # Ejecutar linters
make format       # Formatear código
```

## 📁 Estructura del Proyecto

Ver documentación detallada:
- [Backend Structure](./backend/README.md)
- [Frontend Structure](./frontend/README.md)

## 🤝 Contribuir

1. Fork el proyecto
2. Crear rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📝 License

MIT License - ver [LICENSE](LICENSE) para más detalles.

## 👥 Autores

- Tu Nombre - [@tu-usuario](https://github.com/tu-usuario)
```

## Variables de Entorno

### backend/.env.example
```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/mydb

# Security
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Environment
ENVIRONMENT=development

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:3000"]

# Email (opcional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-password
```

### frontend/.env.example
```bash
VITE_API_URL=http://localhost:8000/api/v1
VITE_APP_NAME=My App
VITE_ENVIRONMENT=development
```

## Comandos Rápidos

```bash
# Setup inicial completo
make install

# Desarrollo
make dev

# Ver logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Entrar a un contenedor
docker-compose exec backend bash
docker-compose exec frontend sh

# Recrear contenedores
docker-compose up -d --build

# Ejecutar migraciones
docker-compose exec backend alembic upgrade head

# Crear superuser
docker-compose exec backend python scripts/create_superuser.py
```