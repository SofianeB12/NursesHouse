import { useEffect, useState } from 'react'
import { Produit, Composant } from '../types'
import { getComposantsByProduit } from '../services/api'

export default function ProductCard({ produit }: { produit: Produit }) {
  const [composants, setComposants] = useState<Composant[]>([])

  useEffect(() => {
    getComposantsByProduit(produit.id).then(setComposants)
  }, [produit.id])

  return (
    <div className="bg-white p-4 rounded-2xl shadow-md border border-pinkaccent text-left">
      <h2 className="text-xl font-serif mb-2">{produit.nom}</h2>
      <p className="text-sm text-gray-600 mb-1">Couleur : {produit.couleur}</p>
      <p className="text-pinkaccent font-bold text-lg mb-2">{produit.prix} €</p>
      <p className="text-sm text-gray-700 mb-2">Composé de : {composants.map(c => c.nom).join(', ')}</p>
      <button className="mt-2 w-full bg-pinkaccent text-white py-2 rounded-xl hover:bg-pink-500 transition">
        Commander
      </button>
    </div>
  )
}
