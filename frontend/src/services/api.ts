import axios from 'axios'
import { Produit, Composant } from '../types'

export const api = axios.create({
  baseURL: 'http://localhost:8000'
})

export const getProduits = async (): Promise<Produit[]> => {
  const res = await api.get('/produits')
  return res.data
}

export const getComposants = async (): Promise<Composant[]> => {
  const res = await api.get('/composants')
  return res.data
}

export const getComposantsByProduit = async (produitId: number): Promise<Composant[]> => {
  const res = await api.get(`/produits/${produitId}/composants`)
  return res.data
}

export const createComposant = async (composant: Omit<Composant, 'id'>): Promise<Composant> => {
  const res = await api.post('/composants', composant)
  return res.data
}