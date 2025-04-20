
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

@router.get("/", response_model=list[schemas.CommandeClient])
def read_items(db: Session = Depends(get_db)):
    return crud.get_commandes_clients(db)

@router.post("/", response_model=schemas.CommandeClient)
def add_item(item: schemas.CommandeClientCreate, db: Session = Depends(get_db)):
    return crud.create_commande_client(db, item)
