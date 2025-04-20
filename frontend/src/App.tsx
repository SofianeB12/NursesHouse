import { useState } from 'react'
import ProductList from './pages/ProductList'
import AdminDashboard from './pages/AdminDashboard'
import logo from '/logo.png'

export default function App() {
  const [view, setView] = useState<'home' | 'admin'>('home')

  return (
    <div className="min-h-screen bg-pinklight text-gray-800 text-center p-6">
      <img src={logo} alt="Logo" className="w-32 mx-auto mb-4" />
      <h1 className="text-3xl font-serif mb-2">Nurse's House</h1>
      <p className="text-pinkaccent mb-6">Accessoires personnalisés pour infirmières</p>
      <div className="flex justify-center gap-4 mb-6">
        <button onClick={() => setView('home')} className="bg-white border border-pinkaccent px-4 py-2 rounded-xl hover:bg-pinkaccent hover:text-white transition">
          Accueil
        </button>
        <button onClick={() => setView('admin')} className="bg-white border border-pinkaccent px-4 py-2 rounded-xl hover:bg-pinkaccent hover:text-white transition">
          Admin
        </button>
      </div>
      {view === 'home' ? <ProductList /> : <AdminDashboard />}
    </div>
  )
}
