/*
import { useState } from 'react'
import LoginForm from './components/LoginForm.jsx'
import RegisterForm from './components/RegisterForm.jsx'
import IngredientList from './components/IngredientList.jsx'
import ComboList from './components/ComboList.jsx'
*/
import IngredientList from './components/IngredientList.jsx'
import ComboList from './components/ComboList.jsx'
import ComboBuilder from './components/ComboBuilder.jsx'

// tratar de hacer un from components/* import Comb, ing

function App() {
  // Entramos directamente sin login
  return (
    <div>
      <h1>ComboApp</h1>
      <IngredientList />
      <ComboBuilder />
      <ComboList />
    </div>
  )
}

/*
function App() {
  const [token, setToken] = useState(localStorage.getItem('token'))

  if (!token) {
    return (
      <>
        <RegisterForm />
        <LoginForm onLogin={setToken} />
      </>
    )
  }

  return (
    <div>
      <h1>ComboApp</h1>
      <IngredientList token={token} />
      <ComboBuilder token={token} />
      <ComboList token={token} />
      <button onClick={() => { localStorage.removeItem('token'); setToken(null) }}>
        Cerrar sesión
      </button>
    </div>
  )
}
*/
export default App