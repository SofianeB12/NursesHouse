
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

@router.get("/", response_model=list[schemas.CompositionProduit])
def read_items(db: Session = Depends(get_db)):
    return crud.get_compositions_produits(db)

@router.post("/", response_model=schemas.CompositionProduit)
def add_item(item: schemas.CompositionProduitCreate, db: Session = Depends(get_db)):
    return crud.create_composition_produit(db, item)
