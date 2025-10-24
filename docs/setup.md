## Documentacion:
- supabase: https://supabase.com/docs/reference/python/select
- fastAPI:  https://fastapi.tiangolo.com/tutorial/

#### cositas para ver
- workflows/branch-protection.yml       ??
- Docker

### Repositorios:
    sudo apt install python3.12-venv
    sudo apt install -y libpq-dev python3-dev

--------------------------------------------------------------
### Ejecutar ambiente virtual 
Si no funciona, probar con *python3*

    python -m venv .venv

Activar el entorno

    PowerShell:    .\.venv\Scripts\activate
    Linux:      source .venv/bin/activate


## 🛠️ Instalación y Configuración
### Local 

1. Backend:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

2. Frontend:
```bash
cd frontend
npm install
npm run dev
```

### Docker

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

## Testing

```bash
# Tests del backend
cd backend && pytest

# Tests del frontend
cd frontend && npm test

```