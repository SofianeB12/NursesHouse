
from sqlalchemy.orm import Session
from . import models, schemas

# Composant
def get_composants(db: Session):
    return db.query(models.Composant).all()

def create_composant(db: Session, item: schemas.ComposantCreate):
    db_obj = models.Composant(**item.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Commande Composant
def get_commandes_composants(db: Session):
    return db.query(models.CommandeComposant).all()

def create_commande_composant(db: Session, item: schemas.CommandeComposantCreate):
    db_obj = models.CommandeComposant(**item.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Produit
def get_produits(db: Session):
    return db.query(models.Produit).all()

def create_produit(db: Session, item: schemas.ProduitCreate):
    db_obj = models.Produit(**item.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Composition Produit
def get_compositions_produits(db: Session):
    return db.query(models.CompositionProduit).all()

def create_composition_produit(db: Session, item: schemas.CompositionProduitCreate):
    db_obj = models.CompositionProduit(**item.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Commande Client
def get_commandes_clients(db: Session):
    return db.query(models.CommandeClient).all()

def create_commande_client(db: Session, item: schemas.CommandeClientCreate):
    db_obj = models.CommandeClient(**item.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Commande Client Produit
def get_commandes_clients_produits(db: Session):
    return db.query(models.CommandeClientProduit).all()

def create_commande_client_produit(db: Session, item: schemas.CommandeClientProduitCreate):
    db_obj = models.CommandeClientProduit(**item.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_composants_by_produit(db: Session, produit_id: int):
    compositions = db.query(models.CompositionProduit).filter_by(id_produit=produit_id).all()
    composants = []
    for compo in compositions:
        composant = db.query(models.Composant).get(compo.id_composant)
        if composant:
            composants.append(composant)
    return composants
