import { useEffect, useState } from 'react'
import { getProduits } from '../services/api'
import { Produit } from '../types'

export default function AdminDashboard() {
  const [produits, setProduits] = useState<Produit[]>([])

  useEffect(() => {
    getProduits().then(setProduits)
  }, [])

  return (
    <div className="text-left max-w-4xl mx-auto">
      <h2 className="text-2xl font-serif mb-4">Liste des produits</h2>
      <table className="w-full text-left bg-white shadow-md rounded-lg overflow-hidden">
        <thead className="bg-pinkaccent text-white">
          <tr>
            <th className="p-2">Nom</th>
            <th className="p-2">Couleur</th>
            <th className="p-2">Prix (€)</th>
            <th className="p-2">Stock</th>
          </tr>
        </thead>
        <tbody>
          {produits.map((p) => (
            <tr key={p.id} className="border-t hover:bg-pink-50">
              <td className="p-2">{p.nom}</td>
              <td className="p-2">{p.couleur}</td>
              <td className="p-2">{p.prix}</td>
              <td className="p-2">{p.quantité_en_stock}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
