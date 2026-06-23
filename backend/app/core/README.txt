Configuración Central del Backend
===================================
Módulos transversales que configuran el comportamiento de toda la aplicación:
- config.py      → Settings con Pydantic BaseSettings (lee .env)
- security.py    → JWT: creación/verificación de tokens, hash de contraseñas
- dependencies.py → dependencias FastAPI (get_db, get_current_user)
- middleware.py  → logging de requests, manejo global de errores
- exceptions.py  → excepciones de dominio personalizadas
