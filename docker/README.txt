Configuración de Contenedores Docker
======================================
Dockerfiles y configuraciones para containerizar cada servicio:
- Dockerfile.frontend   → imagen de producción del frontend (nginx)
- Dockerfile.backend    → imagen de producción del backend (uvicorn)
- nginx.conf            → configuración del servidor web para el frontend
El docker-compose.yml raíz orquesta todos estos servicios juntos.
