import { Produit } from '../types'

export default function ProductCard({ produit }: { produit: Produit }) {
  return (
    <div className="bg-white p-4 rounded-2xl shadow-md border border-pinkaccent text-left">
      <h2 className="text-xl font-serif mb-2">{produit.nom}</h2>
      <p className="text-sm text-gray-600 mb-1">Couleur : {produit.couleur}</p>
      <p className="text-pinkaccent font-bold text-lg">{produit.prix} €</p>
      <button className="mt-4 w-full bg-pinkaccent text-white py-2 rounded-xl hover:bg-pink-500 transition">
        Commander
      </button>
    </div>
  )
}
