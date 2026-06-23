#!/bin/bash
# ============================================================
# Script para crear y subir el repo gestionarte a GitHub
# Requisitos: gh CLI instalado y autenticado (gh auth login)
# ============================================================

set -e

REPO_NAME="gestionarte"
DESCRIPTION="Plataforma de gestión integral para artistas y freelancers creativos"

echo "🚀 Creando repositorio en GitHub..."
gh repo create "$REPO_NAME" \
  --public \
  --description "$DESCRIPTION" \
  --clone=false

echo "📁 Inicializando git local..."
git init
git add .
git commit -m "feat: initial project structure

- React 18 + Vite + TypeScript frontend
- FastAPI + SQLAlchemy + PostgreSQL backend
- Docker + Docker Compose setup
- GitHub Actions CI/CD
- Feature-Sliced Design architecture"

echo "🔗 Conectando con GitHub..."
git branch -M main
git remote add origin "https://github.com/$(gh api user --jq .login)/$REPO_NAME.git"

echo "⬆️  Subiendo código..."
git push -u origin main

echo ""
echo "✅ Repositorio creado exitosamente!"
gh repo view --web
