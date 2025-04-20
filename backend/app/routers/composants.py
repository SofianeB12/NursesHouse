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

@router.get("/", response_model=list[schemas.Composant])
def read_items(db: Session = Depends(get_db)):
    return crud.get_composants(db)

@router.post("/", response_model=schemas.Composant)
def create_item(item: schemas.ComposantCreate, db: Session = Depends(get_db)):
    return crud.create_composant(db, item)
