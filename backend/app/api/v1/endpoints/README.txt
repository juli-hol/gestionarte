Endpoints por Recurso
=======================
Un archivo por recurso REST de la API:
- auth.py       → POST /login, POST /register, POST /refresh-token
- users.py      → GET/PUT /users/me, GET /users/{id}
- projects.py   → CRUD /projects
- tasks.py      → CRUD /tasks
- clients.py    → CRUD /clients
Cada archivo usa APIRouter de FastAPI y llama a su Service correspondiente.
