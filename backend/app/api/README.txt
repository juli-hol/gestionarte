Capa de API - Routers HTTP
===========================
Define y organiza todos los endpoints HTTP de la aplicación.
Usa versionado de API (v1, v2...) para compatibilidad hacia atrás.
Los routers solo reciben requests, validan con Pydantic y delegan
la lógica al layer de Services.
