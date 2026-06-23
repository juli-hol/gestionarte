Redux Slices / Stores Atómicos
================================
Cada archivo define el estado, reducers y acciones de una entidad:
- authSlice.ts     → usuario autenticado, token, permisos
- uiSlice.ts       → estado de sidebar, modales, loading global
- notifSlice.ts    → cola de notificaciones toast
Siguiendo el patrón de Redux Toolkit (createSlice + createAsyncThunk).
