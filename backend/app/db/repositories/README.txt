Patrón Repository - Acceso a Datos
====================================
Encapsulan todas las operaciones de base de datos para cada entidad.
Traducen operaciones de dominio a queries SQL/ORM:
- base_repository.py   → CRUD genérico reutilizable (get, get_all, create, update, delete)
- user_repository.py   → queries específicas de usuarios (find_by_email, etc.)
- project_repository.py
- task_repository.py
Los Services solo llaman Repositories, nunca SQL directo.
