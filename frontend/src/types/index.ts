export interface Produit {
  id: number
  nom: string
  couleur: string
  cout: number
  prix: number
  quantite_en_stock: number
}

export interface Composant {
  id: number
  nom: string
  couleur: string
  cout: number
  quantite_en_stock: number
}


export interface CommandeComposant {
  id: number
  id_composant: number
  quantite: number
}

export interface CommandeComposantCreate {
  id_composant: number
  quantite_commandee: number
  cout_commande : number
  date_commande : Date
  statut : string
}
