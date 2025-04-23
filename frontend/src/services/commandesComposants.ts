import { api } from './api'
import { CommandeComposantCreate } from '../types'

export const createCommandeComposant = async (commande: CommandeComposantCreate) => {
  const res = await api.post('/commandes-composants', commande)
  return res.data
}
