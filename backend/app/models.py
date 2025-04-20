from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from .database import Base

class Composant(Base):
    __tablename__ = "composant"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    couleur = Column(String)
    cout = Column(Float)
    quantité_en_stock = Column(Integer)

class CommandeComposant(Base):
    __tablename__ = "commande_composant"
    id = Column(Integer, primary_key=True, index=True)
    id_composant = Column(Integer, ForeignKey("composant.id"))
    quantité_commandée = Column(Integer)
    cout_commande = Column(Float)
    date_commande = Column(DateTime)
    statut = Column(String)

class Produit(Base):
    __tablename__ = "produit"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    couleur = Column(String)
    prix = Column(Float)
    quantité_en_stock = Column(Integer)

class CompositionProduit(Base):
    __tablename__ = "composition_produit"
    id = Column(Integer, primary_key=True, index=True)
    id_produit = Column(Integer, ForeignKey("produit.id"))
    id_composant = Column(Integer, ForeignKey("composant.id"))
    quantité_utilisee = Column(Integer)

class CommandeClient(Base):
    __tablename__ = "commande_client"
    id = Column(Integer, primary_key=True, index=True)
    nom_client = Column(String)
    statut = Column(String)
    date_commande = Column(DateTime)

class CommandeClientProduit(Base):
    __tablename__ = "commande_client_produit"
    id = Column(Integer, primary_key=True, index=True)
    id_commande = Column(Integer, ForeignKey("commande_client.id"))
    id_produit = Column(Integer, ForeignKey("produit.id"))
    quantite = Column(Integer)
