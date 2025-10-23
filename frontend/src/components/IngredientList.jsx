import { useEffect, useState } from 'react'
import { getIngredients } from '../api/client.js'

export default function IngredientList({ token }) {
  const [ingredients, setIngredients] = useState([])

  useEffect(() => {
    getIngredients(token).then(res => setIngredients(res.data))
  }, [token])

  return (
    <div>
      <h3>Ingredientes disponibles</h3>
      <ul>
        {ingredients.map(i => <li key={i.id}>{i.name} - ${i.price}</li>)}
      </ul>
    </div>
  )
}