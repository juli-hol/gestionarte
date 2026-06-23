Capa de Servicios - Lógica de Negocio
=======================================
Orquesta la lógica de negocio de la aplicación.
Los Services son invocados por los Endpoints y a su vez invocan Repositories.
Aquí van las reglas de negocio: validaciones complejas, cálculos, envío
de emails, integración con servicios externos, transacciones multi-tabla.
- auth_service.py
- project_service.py
- task_service.py
- client_service.py
