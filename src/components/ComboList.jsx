import { useEffect, useState } from 'react'
import { getCombos } from '../api/client.js'

export default function ComboList({ token }) {
  const [combos, setCombos] = useState([])

  useEffect(() => {
    getCombos(token).then(res => setCombos(res.data))
  }, [token])

  return (
    <div>
      <h3>Combos existentes</h3>
      <ul>
        {combos.map(c => (
          <li key={c.id}>
            {c.name} - Total: ${c.total_price}
          </li>
        ))}
      </ul>
    </div>
  )
}