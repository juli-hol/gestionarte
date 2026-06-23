from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, projects, tasks, clients

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
api_router.include_router(users.router, prefix="/users", tags=["Usuarios"])
api_router.include_router(projects.router, prefix="/projects", tags=["Proyectos"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["Tareas"])
api_router.include_router(clients.router, prefix="/clients", tags=["Clientes"])
