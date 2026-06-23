Modelos ORM (SQLAlchemy)
=========================
Clases Python que representan tablas de la base de datos:
- user.py       → tabla users (id, email, hashed_password, role, created_at)
- project.py    → tabla projects (id, name, status, client_id, deadline)
- task.py       → tabla tasks (id, title, status, priority, project_id)
- client.py     → tabla clients (id, name, email, phone, company)
Heredan de Base (SQLAlchemy declarative_base).
