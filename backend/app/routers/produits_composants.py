from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{produit_id}/composants", response_model=list[schemas.Composant])
def get_composants_by_produit(produit_id: int, db: Session = Depends(get_db)):
    return crud.get_composants_by_produit(db, produit_id)
