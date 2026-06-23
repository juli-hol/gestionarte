Configuración del Router
==========================
Define la estructura de navegación de la SPA usando React Router v6:
- index.tsx         → árbol de rutas completo
- PrivateRoute.tsx  → guard para rutas autenticadas
- PublicRoute.tsx   → redirige a home si ya está logueado
- routes.ts         → constantes de paths ('/projects', '/tasks/:id', etc.)
