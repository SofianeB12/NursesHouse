import React from 'react'
import { useEffect, useState } from 'react'
import { Composant } from '../types'
import { getComposants, createComposant } from '../services/api'
import { createCommandeComposant } from '../services/commandesComposants'

export default function AjouterCommandeComposant() {
  const [composants, setComposants] = useState<Composant[]>([])
  const [mode, setMode] = useState<'existant' | 'nouveau'>('existant')

  const [idComposant, setIdComposant] = useState<number | null>(null)
  const [quantite, setQuantite] = useState(1)
  const [coutCommande, setCoutCommande] = useState<number | null>(null)
  const [dateCommande, setDateCommande] = useState<string>("")
  const [statut, setStatut] = useState<string>("en_attente")

  const [nouveauComposant, setNouveauComposant] = useState({
    nom: '',
    couleur: '',
    quantite_en_stock: 0
  })

  const [message, setMessage] = useState("")

  useEffect(() => {
    getComposants().then(setComposants)
  }, [])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!coutCommande || !dateCommande) {
      setMessage("❌ Veuillez remplir tous les champs requis.")
      return
    }

    if (mode === 'existant' && idComposant) {
      await createCommandeComposant({
        id_composant: idComposant,
        quantite_commandee: quantite,
        cout_commande: coutCommande,
        date_commande: dateCommande,
        statut: statut
      })
      setMessage("✅ Commande ajoutée avec un composant existant.")
    }

    if (mode === 'nouveau') {
      const coutUnitaire = coutCommande / quantite
      const composant = await createComposant({
        ...nouveauComposant,
        cout: coutUnitaire
      })
      await createCommandeComposant({
        id_composant: composant.id,
        quantite_commandee: quantite,
        cout_commande: coutCommande,
        date_commande: dateCommande,
        statut: statut
      })
      setMessage("✅ Nouveau composant créé et commande enregistrée.")
    }
  }

  return (
    <div className="max-w-xl mx-auto mt-10 bg-white p-6 rounded-2xl shadow">
      <h2 className="text-2xl font-serif mb-4">Ajouter une commande de composant</h2>

      <div className="flex gap-4 mb-6">
        <label>
          <input type="radio" name="mode" value="existant" checked={mode === 'existant'} onChange={() => setMode('existant')} />
          <span className="ml-2">Composant existant</span>
        </label>
        <label>
          <input type="radio" name="mode" value="nouveau" checked={mode === 'nouveau'} onChange={() => setMode('nouveau')} />
          <span className="ml-2">Nouveau composant</span>
        </label>
      </div>

      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        {mode === 'existant' && (
          <>
            <label>
              Sélectionner un composant :
              <select className="w-full p-2 mt-1 border rounded" value={idComposant ?? ''} onChange={e => setIdComposant(Number(e.target.value))}>
                <option value="">-- Choisir --</option>
                {composants.map(c => (
                  <option key={c.id} value={c.id}>{c.nom} ({c.couleur})</option>
                ))}
              </select>
            </label>
          </>
        )}

        {mode === 'nouveau' && (
          <>
            <label>
              Nom du composant :
              <input type="text" className="w-full p-2 border rounded" value={nouveauComposant.nom} onChange={e => setNouveauComposant({ ...nouveauComposant, nom: e.target.value })} />
            </label>
            <label>
              Couleur :
              <input type="text" className="w-full p-2 border rounded" value={nouveauComposant.couleur} onChange={e => setNouveauComposant({ ...nouveauComposant, couleur: e.target.value })} />
            </label>
            <label>
              Stock :
              <input type="number" className="w-full p-2 border rounded" value={nouveauComposant.stock} onChange={e => setNouveauComposant({ ...nouveauComposant, stock: Number(e.target.value) })} />
            </label>
          </>
        )}

        <label>
          Quantité commandée :
          <input type="number" className="w-full p-2 border rounded" min={1} value={quantite} onChange={e => setQuantite(Number(e.target.value))} />
        </label>

        <label>
          Coût total de la commande (€) :
          <input type="number" className="w-full p-2 border rounded" value={coutCommande ?? ''} onChange={e => setCoutCommande(Number(e.target.value))} />
        </label>

        <label>
          Date de la commande :
          <input type="date" className="w-full p-2 border rounded" value={dateCommande} onChange={e => setDateCommande(e.target.value)} />
        </label>

        <label>
          Statut :
          <select className="w-full p-2 border rounded" value={statut} onChange={e => setStatut(e.target.value)}>
            <option value="en_attente">En attente</option>
            <option value="livré">Livré</option>
            <option value="annulé">Annulé</option>
          </select>
        </label>

        <button type="submit" className="bg-pinkaccent text-white py-2 px-4 rounded hover:bg-pink-500">
          Valider la commande
        </button>

        {message && <p className="text-green-600 mt-2">{message}</p>}
      </form>
    </div>
  )
}
