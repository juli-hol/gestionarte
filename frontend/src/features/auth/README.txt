Feature: Autenticación
=======================
Todo lo relacionado con el ciclo de autenticación del usuario:
- components/  → LoginForm, RegisterForm, ForgotPassword
- hooks/       → useAuth, useLogin, useLogout
- services/    → authService.ts (llamadas a /api/auth/*)
- types/       → User, AuthState, LoginCredentials
- store/       → authSlice.ts (estado global de sesión)
