from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()


@router.get("/")
def list_projects(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    # TODO: implementar con ProjectService
    return {"items": [], "total": 0}


@router.get("/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db)):
    # TODO: implementar con ProjectService
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proyecto no encontrado")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_project(db: Session = Depends(get_db)):
    # TODO: implementar con ProjectService
    pass


@router.put("/{project_id}")
def update_project(project_id: int, db: Session = Depends(get_db)):
    pass


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    pass
