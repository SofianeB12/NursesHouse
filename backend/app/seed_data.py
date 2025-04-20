from datetime import datetime
from sqlalchemy.orm import Session
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

def seed_data():
    db: Session = database.SessionLocal()

    comp1 = models.Composant(nom="Lanière", couleur="Rose", cout=1.5, quantité_en_stock=100)
    comp2 = models.Composant(nom="Stylo", couleur="Bleu", cout=0.8, quantité_en_stock=200)
    db.add_all([comp1, comp2])
    db.commit()

    prod = models.Produit(nom="Pack infirmière", couleur="Rose", prix=9.99, quantité_en_stock=50)
    db.add(prod)
    db.commit()

    cp1 = models.CompositionProduit(id_produit=prod.id, id_composant=comp1.id, quantité_utilisee=1)
    cp2 = models.CompositionProduit(id_produit=prod.id, id_composant=comp2.id, quantité_utilisee=1)
    db.add_all([cp1, cp2])
    db.commit()

    cmd_client = models.CommandeClient(nom_client="Julie Martin", statut="préparation", date_commande=datetime.now())
    db.add(cmd_client)
    db.commit()

    cmd_prod = models.CommandeClientProduit(id_commande=cmd_client.id, id_produit=prod.id, quantite=2)
    db.add(cmd_prod)
    db.commit()

    db.close()
    print("✅ Données de test insérées avec succès.")

if __name__ == "__main__":
    seed_data()
