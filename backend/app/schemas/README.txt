Schemas Pydantic (DTOs)
========================
Data Transfer Objects: validan y serializan datos de entrada/salida de la API.
Por convención, cada entidad tiene tres schemas:
- XxxBase       → campos comunes
- XxxCreate     → para POST (sin id ni timestamps)
- XxxUpdate     → para PUT/PATCH (campos opcionales)
- XxxResponse   → para la respuesta JSON al cliente
Separan la representación de la API del modelo de base de datos.
