from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ComposantBase(BaseModel):
    nom: str
    couleur: str
    unité: str
    quantité_en_stock: int
    dernière_mise_à_jour: datetime

class ComposantCreate(ComposantBase):
    pass

class Composant(ComposantBase):
    id: int
    class Config:
        orm_mode = True

class ProduitBase(BaseModel):
    nom: str
    couleur: str
    prix: float
    quantité_en_stock: int
    description: str

class ProduitCreate(ProduitBase):
    pass

class Produit(ProduitBase):
    id: int
    class Config:
        orm_mode = True


class CommandeClientBase(BaseModel):
    id_produit: int
    nom_client: str
    nom_personnalisé: str
    statut: str
    date_commande: datetime

class CommandeClientCreate(CommandeClientBase):
    pass

class CommandeClient(CommandeClientBase):
    id: int
    class Config:
        orm_mode = True


class CommandeComposantBase(BaseModel):
    id_composant: int
    quantité_commandée: int
    date_commande: datetime
    date_livraison_attendue: datetime
    statut: str

class CommandeComposantCreate(CommandeComposantBase):
    pass

class CommandeComposant(CommandeComposantBase):
    id: int
    class Config:
        orm_mode = True


class CompositionProduitBase(BaseModel):
    id_produit: int
    id_composant: int
    quantité_utilisée: int

class CompositionProduitCreate(CompositionProduitBase):
    pass

class CompositionProduit(CompositionProduitBase):
    id: int
    class Config:
        orm_mode = True
