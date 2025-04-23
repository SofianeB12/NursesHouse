import React from 'react'
import ProductList from './pages/ProductList'
import AdminDashboard from './pages/AdminDashboard'

import { Routes, Route, Link } from 'react-router-dom'
import AjouterCommandeComposant from './pages/AjouterCommandeComposant'

export default function App() {
  return (
    <div className="min-h-screen bg-pinklight text-gray-800 p-6">
      <img src="/logo.png" alt="Logo" className="w-32 mx-auto mb-4" />
      <nav className="mb-6 flex gap-4 justify-center">
        <Link to="/" className="bg-white border border-pinkaccent px-4 py-2 rounded-xl hover:bg-pinkaccent hover:text-white">
          Accueil
        </Link>
        <Link to="/admin" className="bg-white border border-pinkaccent px-4 py-2 rounded-xl hover:bg-pinkaccent hover:text-white">
          Admin
        </Link>
        <Link to="/ajouter-commande" className="bg-white border border-pinkaccent px-4 py-2 rounded-xl hover:bg-pinkaccent hover:text-white">
          Ajouter commande
        </Link>
      </nav>

      <Routes>
        <Route path="/" element={<ProductList />} />
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/ajouter-commande" element={<AjouterCommandeComposant />} />
      </Routes>
    </div>
  )
}
