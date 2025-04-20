from pydantic import BaseModel
from datetime import datetime

class ComposantBase(BaseModel):
    nom: str
    couleur: str
    cout: float
    quantité_en_stock: int

class ComposantCreate(ComposantBase):
    pass

class Composant(ComposantBase):
    id: int
    class Config:
        orm_mode = True

class CommandeComposantBase(BaseModel):
    id_composant: int
    quantité_commandée: int
    cout_commande: float
    date_commande: datetime
    statut: str

class CommandeComposantCreate(CommandeComposantBase):
    pass

class CommandeComposant(CommandeComposantBase):
    id: int
    class Config:
        orm_mode = True

class ProduitBase(BaseModel):
    nom: str
    couleur: str
    prix: float
    quantité_en_stock: int

class ProduitCreate(ProduitBase):
    pass

class Produit(ProduitBase):
    id: int
    class Config:
        orm_mode = True

class CompositionProduitBase(BaseModel):
    id_produit: int
    id_composant: int
    quantité_utilisee: int

class CompositionProduitCreate(CompositionProduitBase):
    pass

class CompositionProduit(CompositionProduitBase):
    id: int
    class Config:
        orm_mode = True

class CommandeClientBase(BaseModel):
    nom_client: str
    statut: str
    date_commande: datetime

class CommandeClientCreate(CommandeClientBase):
    pass

class CommandeClient(CommandeClientBase):
    id: int
    class Config:
        orm_mode = True

class CommandeClientProduitBase(BaseModel):
    id_commande: int
    id_produit: int
    quantite: int

class CommandeClientProduitCreate(CommandeClientProduitBase):
    pass

class CommandeClientProduit(CommandeClientProduitBase):
    id: int
    class Config:
        orm_mode = True
