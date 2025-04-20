from sqlalchemy.orm import Session
from . import models, schemas

def get_composants(db: Session):
    return db.query(models.Composant).all()

def create_composant(db: Session, composant: schemas.ComposantCreate):
    db_obj = models.Composant(**composant.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
