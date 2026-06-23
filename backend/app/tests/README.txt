Tests del Backend
==================
Suite completa de pruebas automatizadas del backend:
- unit/        → tests de Services y utilidades con mocks de Repositories
- integration/ → tests de endpoints HTTP con base de datos de test real
- conftest.py  → fixtures compartidos (cliente de test, BD en memoria, usuario mock)
Herramientas: pytest, pytest-asyncio, httpx (cliente async), factory_boy.
