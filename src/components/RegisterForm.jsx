import { useState } from 'react'
import { register } from '../api/client.js'

export default function RegisterForm() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      await register({ username, password })
      alert('Usuario registrado correctamente')
    } catch {
      alert('Error al registrar usuario')
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h3>Registrarse</h3>
      <input placeholder='Usuario' value={username} onChange={(e) => setUsername(e.target.value)} />
      <input placeholder='Contraseña' type='password' value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type='submit'>Registrar</button>
    </form>
  )
}