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

@router.get("/", response_model=list[schemas.Produit])
def read_items(db: Session = Depends(get_db)):
    return crud.get_produits(db)

@router.post("/", response_model=schemas.Produit)
def create_item(item: schemas.ProduitCreate, db: Session = Depends(get_db)):
    return crud.create_produit(db, item)
