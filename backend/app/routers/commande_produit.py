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

@router.get("/", response_model=list[schemas.CommandeClientProduit])
def read_items(db: Session = Depends(get_db)):
    return crud.get_commandes_produits(db)

@router.post("/", response_model=schemas.CommandeClientProduit)
def add_item(item: schemas.CommandeClientProduitCreate, db: Session = Depends(get_db)):
    return crud.create_commande_produit(db, item)
