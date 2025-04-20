import { useEffect, useState } from 'react'
import { getProduits } from '../services/api'
import { Produit } from '../types'
import ProductCard from '../components/ProductCard'

export default function ProductList() {
  const [produits, setProduits] = useState<Produit[]>([])

  useEffect(() => {
    getProduits().then(setProduits)
  }, [])

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 px-4">
      {produits.map((p) => (
        <ProductCard key={p.id} produit={p} />
      ))}
    </div>
  )
}
