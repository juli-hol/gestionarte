# 🎨 gestionARTE

> Plataforma de gestión integral para artistas y freelancers creativos.

## Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| Frontend | React 18 + Vite + TypeScript |
| Backend | Python 3.12 + FastAPI |
| Base de datos | PostgreSQL 16 |
| ORM | SQLAlchemy 2.0 + Alembic |
| Autenticación | JWT (python-jose) |
| Contenedores | Docker + Docker Compose |
| CI/CD | GitHub Actions |

## Estructura del Proyecto

```
gestionarte/
├── frontend/          # SPA React + Vite
├── backend/           # API REST FastAPI
├── docker/            # Dockerfiles de cada servicio
├── docs/              # Documentación técnica
└── .github/           # CI/CD y plantillas
```

## Inicio Rápido

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/gestionarte.git
cd gestionarte

# 2. Copiar variables de entorno
cp .env.example .env

# 3. Levantar todos los servicios
docker compose up -d

# 4. Aplicar migraciones
docker compose exec backend alembic upgrade head

# 5. Poblar datos de prueba (opcional)
docker compose exec backend python scripts/seed_db.py
```

Frontend disponible en: http://localhost:5173  
API disponible en: http://localhost:8000  
Docs de la API: http://localhost:8000/docs

## Comandos de Desarrollo

```bash
# Frontend
cd frontend && npm install && npm run dev

# Backend
cd backend && pip install -r requirements.txt
uvicorn app.main:app --reload

# Tests Frontend
cd frontend && npm run test

# Tests Backend
cd backend && pytest
```

## Contribución

Ver [docs/guides/contributing.md](docs/guides/contributing.md)
