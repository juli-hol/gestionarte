Capa de Base de Datos
======================
Todo lo relacionado con el acceso y gestión de datos persistentes:
- session.py      → engine SQLAlchemy, SessionLocal, Base declarativa
- models/         → clases ORM que mapean tablas de la BD
- repositories/   → patrón Repository: queries SQL encapsuladas
Separa la lógica de acceso a datos de la lógica de negocio (Services).
