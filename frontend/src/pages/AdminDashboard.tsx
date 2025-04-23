import { useEffect, useState } from 'react'
import { getProduits, getComposants } from '../services/api'
import { Produit, Composant } from '../types'

export default function AdminDashboard() {
  const [produits, setProduits] = useState<Produit[]>([])
  const [composants, setComposants] = useState<Composant[]>([])

  useEffect(() => {
    getProduits().then(setProduits)
    getComposants().then(setComposants)
  }, [])

  return (
    <div className="text-left max-w-6xl mx-auto">
      <h2 className="text-2xl font-serif mb-4">Produits</h2>
      <table className="w-full text-left bg-white shadow-md rounded-lg overflow-hidden mb-8">
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
              <td className="p-2">{p.quantite_en_stock}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2 className="text-2xl font-serif mb-4">Composants</h2>
      <table className="w-full text-left bg-white shadow-md rounded-lg overflow-hidden">
        <thead className="bg-pinkaccent text-white">
          <tr>
            <th className="p-2">Nom</th>
            <th className="p-2">Couleur</th>
            <th className="p-2">Coût (€)</th>
            <th className="p-2">Stock</th>
          </tr>
        </thead>
        <tbody>
          {composants.map((c) => (
            <tr key={c.id} className="border-t hover:bg-pink-50">
              <td className="p-2">{c.nom}</td>
              <td className="p-2">{c.couleur}</td>
              <td className="p-2">{c.cout}</td>
              <td className="p-2">{c.quantite_en_stock}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
