from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Composant(Base):
    __tablename__ = "composant"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    couleur = Column(String)
    unité = Column(String)
    quantité_en_stock = Column(Integer)
    dernière_mise_à_jour = Column(DateTime)

class CommandeComposant(Base):
    __tablename__ = "commande_composant"
    id = Column(Integer, primary_key=True, index=True)
    id_composant = Column(Integer, ForeignKey("composant.id"))
    quantité_commandée = Column(Integer)
    date_commande = Column(DateTime)
    date_livraison_attendue = Column(DateTime)
    statut = Column(String)

class Produit(Base):
    __tablename__ = "produit"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    couleur = Column(String)
    prix = Column(Float)
    quantité_en_stock = Column(Integer)
    description = Column(String)

class CompositionProduit(Base):
    __tablename__ = "composition_produit"
    id = Column(Integer, primary_key=True, index=True)
    id_produit = Column(Integer, ForeignKey("produit.id"))
    id_composant = Column(Integer, ForeignKey("composant.id"))
    quantité_utilisée = Column(Integer)

class CommandeClient(Base):
    __tablename__ = "commande_client"
    id = Column(Integer, primary_key=True, index=True)
    id_produit = Column(Integer, ForeignKey("produit.id"))
    nom_client = Column(String)
    nom_personnalisé = Column(String)
    statut = Column(String)
    date_commande = Column(DateTime)
