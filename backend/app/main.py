from fastapi import FastAPI
from .database import Base, engine
from .routers import composants, commandes_composants, produits, compositions_produits, commandes_clients, commandes_clients_produits

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(composants.router, prefix="/composants", tags=["Composants"])
app.include_router(commandes_composants.router, prefix="/commandes-composants", tags=["Commandes Composants"])
app.include_router(produits.router, prefix="/produits", tags=["Produits"])
app.include_router(compositions_produits.router, prefix="/compositions-produits", tags=["Compositions Produits"])
app.include_router(commandes_clients.router, prefix="/commandes-clients", tags=["Commandes Clients"])
app.include_router(commandes_clients_produits.router, prefix="/commandes-clients-produits", tags=["Commandes Clients Produits"])
