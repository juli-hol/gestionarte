GitHub Actions Workflows
=========================
Archivos YAML que definen los pipelines de CI/CD:
- ci.yml       → lint + tests en cada PR
- deploy.yml   → build y deploy a producción al mergear a main
- release.yml  → generación automática de changelog y tags de versión
