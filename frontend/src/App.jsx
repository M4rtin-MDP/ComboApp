import { useState, useEffect } from 'react'
import Header from './components/Header.jsx'
import HomeScreen from './components/HomeScreen.jsx'
import UserScreen from './components/UserScreen.jsx'
import DetailsScreen from './components/DetailsScreen.jsx'
import api from './api/client.js'

export default function App(){
  const [screen, setScreen] = useState('home')
  const [currentCombo, setCurrentCombo] = useState({ base:null, ingredients:[], bebida:null, acompanamiento:null })
  const [locals, setLocals] = useState([])
  const [selectedLocal, setSelectedLocal] = useState(null)

  useEffect(()=>{
    async function load(){
      try{
        await api.get('/products')
      }catch(e){}
    }
    load()
  },[])

  const go = (s)=> setScreen(s)

  return (
    <div className="container">
      <Header onLogin={()=>{}} onRegister={()=>{}} />
      {screen === 'home' && <HomeScreen onAdd={()=>go('user')} onSuggest={async ()=>{
        try{
          const res = await api.get('/locals')
          setLocals(res.data || [])
        }catch(e){ setLocals([]) }
        go('user')
      }} />}
      {screen === 'user' && <UserScreen combo={currentCombo} locals={locals} onChooseLocal={(l)=>{ setSelectedLocal(l); go('details') }} onBack={()=>go('home')} onAddIngredient={(type, item)=>{
        setCurrentCombo(prev=>{
          const next = {...prev}
          if(type === 'base') next.base = item
          if(type === 'ingredient') next.ingredients = [...prev.ingredients, item]
          if(type === 'bebida') next.bebida = item
          if(type === 'postre') next.acompanamiento = item
          return next
        })
      }} />}
      {screen === 'details' && <DetailsScreen local={selectedLocal} combo={currentCombo} onBack={()=>go('user')} onAddToCombo={()=>{ }} onOrder={async ()=>{
        try{
          const payload = { combo_id: 1, user_id: 1, local_id: selectedLocal?.id }
          await api.post('/orders', payload)
          alert('Pedido enviado')
        }catch(e){ alert('No se pudo enviar pedido') }
      }} />}
    </div>
  )
}
