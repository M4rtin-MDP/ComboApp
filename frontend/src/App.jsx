import React, { useState } from 'react'
import Auth from './pages/Login/Auth.jsx'
import MainScreen from './components/MainScreen.jsx'

export default function App(){
  const [token, setToken] = useState(localStorage.getItem('token'))
  const handleLogin = (t) => { localStorage.setItem('token', t); setToken(t) }
  const handleLogout = () => { localStorage.removeItem('token'); setToken(null) }

  if(!token) return <Auth onLogin={handleLogin} />

  return <MainScreen onLogout={handleLogout} />
}