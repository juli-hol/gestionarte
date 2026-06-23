Servicios de API (Capa HTTP)
==============================
Módulos que encapsulan todas las llamadas HTTP al backend usando Axios.
Cada archivo corresponde a un recurso de la API:
- apiClient.ts       → instancia Axios con interceptores (token, errores)
- authService.ts     → /api/auth/*
- projectService.ts  → /api/projects/*
- taskService.ts     → /api/tasks/*
- clientService.ts   → /api/clients/*
Nunca se hace fetch directamente desde componentes o features.
