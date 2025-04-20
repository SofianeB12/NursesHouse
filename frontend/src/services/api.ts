import axios from 'axios'
import { Produit } from '../types'

export const api = axios.create({
  baseURL: 'http://localhost:8000'
})

export const getProduits = async (): Promise<Produit[]> => {
  const res = await api.get('/produits')
  return res.data
}
