Migraciones de Base de Datos (Alembic)
========================================
Gestiona los cambios de esquema de la base de datos de forma versionada.
- env.py          → configuración de Alembic (connection string, target metadata)
- script.py.mako  → template para nuevas migraciones
- versions/       → archivos de migración ordenados cronológicamente
Comandos: alembic upgrade head | alembic revision --autogenerate -m 'descripcion'
