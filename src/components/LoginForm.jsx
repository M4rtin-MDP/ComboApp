import { useState } from 'react'
import { login } from '../api/client.js'

export default function LoginForm({ onLogin }) {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const res = await login({ username, password })
      const token = res.data.access_token
      localStorage.setItem('token', token)
      onLogin(token)
    } catch {
      alert('Error al iniciar sesión')
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h3>Iniciar Sesión</h3>
      <input placeholder='Usuario' value={username} onChange={(e) => setUsername(e.target.value)} />
      <input placeholder='Contraseña' type='password' value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type='submit'>Entrar</button>
    </form>
  )
}