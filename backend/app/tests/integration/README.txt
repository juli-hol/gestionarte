Tests de Integración del Backend
===================================
Prueban los endpoints HTTP de extremo a extremo con una BD de test.
Usan el cliente de test de FastAPI (TestClient o AsyncClient de httpx).
Verifican: códigos de estado HTTP, estructura del JSON, efectos en la BD.
Se ejecutan contra SQLite en memoria o PostgreSQL en Docker para CI.
