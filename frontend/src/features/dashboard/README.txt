Feature: Dashboard Principal
=============================
Panel de control con métricas y resumen del estado del negocio:
- components/  → KPICard, RevenueChart, RecentActivity, TaskSummary
- hooks/       → useDashboardStats
- services/    → dashboardService.ts
Consume datos agregados del backend para mostrar indicadores clave.
