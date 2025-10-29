import React, { useState, useEffect } from 'react'
import api from '../api/client'

export default function MainScreen({ onLogout }){
  const [view, setView] = useState('home') // home, add-food, add-drink, add-dessert, user
  const [suggestions, setSuggestions] = useState([])
  const [combos, setCombos] = useState([])
  const [currentCombo, setCurrentCombo] = useState({ base: null, ingredients: [], bebida: null, acompanamiento: null })

  useEffect(()=> {
    api.get('/combos').then(r=>setCombos(r.data)).catch(()=>setCombos([]))
  }, [])

  const guardarCombo = async () => {
    try {
      const payload = {
        nombre: 'Combo desde frontend',
        base_id: currentCombo.base?.id || 1,
        ingredient_ids: currentCombo.ingredients.map(i=>i.id),
        bebida_id: currentCombo.bebida?.id || null,
        acompanamiento_id: currentCombo.acompanamiento?.id || null
      }
      const res = await api.post('/combos', payload)
      alert('Combo guardado (id: ' + res.data.id + ')')
    } catch (e) {
      alert('Combo guardado (simulado).')
    }
  }

  const verSugerencias = async () => {
    try {
      const product_ids = [ currentCombo.base?.id || 1, ...(currentCombo.ingredients.map(i=>i.id)||[]) ]
      const params = new URLSearchParams()
      product_ids.forEach(id => params.append('product_ids', id))
      const res = await api.get('/locals/search?' + params.toString())
      setSuggestions(res.data)
      setView('user')
    } catch (e) {
      setSuggestions([{ id: 1, nombre: 'BurgerMix', direccion: 'Calle Falsa 123', latitud: null, longitud: null }])
      setView('user')
    }
  }

  return (
    <div className="min-h-screen p-6 bg-gray-50">
      <header className="flex justify-between items-center mb-6">
        <div className="text-2xl font-bold text-orange-500">🍔 ComboApp</div>
        <div className="flex gap-2">
          <button className="px-3 py-1 text-sm" onClick={()=>setView('home')}>Inicio</button>
          <button className="px-3 py-1 text-sm" onClick={()=>setView('user')}>Mi usuario</button>
          <button className="px-3 py-1 text-sm" onClick={onLogout}>Cerrar sesión</button>
        </div>
      </header>

      {view==='home' && (
        <main className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white p-6 rounded shadow">
            <h3 className="text-lg font-semibold mb-4">Crear tu combo</h3>
            <div className="flex flex-col gap-2">
              <button className="px-4 py-2 bg-blue-500 text-white rounded" onClick={()=>setView('add-food')}>Agregar Comida +</button>
              <button className="px-4 py-2 bg-blue-500 text-white rounded" onClick={()=>setView('add-drink')}>Agregar Bebida +</button>
              <button className="px-4 py-2 bg-blue-500 text-white rounded" onClick={()=>setView('add-dessert')}>Agregar Postre +</button>
            </div>

            <div className="mt-4 flex gap-2">
              <button className="px-4 py-2 bg-green-600 text-white rounded" onClick={verSugerencias}>Ver sugerencias de locales Cercanos</button>
              <button className="px-4 py-2 bg-green-600 text-white rounded" onClick={guardarCombo}>Guardar Combo Favorito</button>
            </div>
          </div>

          <aside className="bg-white p-6 rounded shadow">
            <h4 className="text-lg font-semibold mb-2">Tu combo elegido:</h4>
            <div className="text-sm">
              <p>Base: {currentCombo.base?.nombre || '---'}</p>
              <p>Ingredientes: {currentCombo.ingredients.map(i=>i.nombre).join(', ') || '---'}</p>
              <p>Bebida: {currentCombo.bebida?.nombre || '---'}</p>
              <p>Acompañamiento: {currentCombo.acompanamiento?.nombre || '---'}</p>
            </div>

            <div className="mt-4">
              <h5 className="font-semibold mb-2">Sugerencias:</h5>
              <ul>
                {suggestions.map(s=>(
                  <li key={s.id} className="mb-2 border-b pb-2">
                    <div className="flex justify-between">
                      <div>
                        <div className="font-semibold">{s.nombre}</div>
                        <div className="text-sm text-gray-600">{s.direccion}</div>
                      </div>
                      <div>
                        <button className="px-3 py-1 bg-blue-500 text-white rounded">Ver Detalles</button>
                      </div>
                    </div>
                  </li>
                ))}
                {suggestions.length===0 && <li className="text-sm text-gray-500">No hay sugerencias aún.</li>}
              </ul>
            </div>
          </aside>
        </main>
      )}

      {view==='user' && (
        <div className="bg-white p-6 rounded shadow max-w-2xl">
          <h3 className="text-lg font-semibold mb-4">Bienvenido!</h3>
          <h4 className="mb-2">Tus combos:</h4>
          <ul>
            {combos.map(c=>(
              <li key={c.id} className="mb-2 border-b pb-2">{c.nombre || ('Combo ' + c.id)}</li>
            ))}
            {combos.length===0 && <li className="text-sm text-gray-500">No tenés combos guardados.</li>}
          </ul>

          <h4 className="mt-4 mb-2">Sugerencias de locales:</h4>
          <ul>
            {suggestions.map(l=>(
              <li key={l.id} className="mb-3">
                <div className="flex justify-between items-center">
                  <div>
                    <div className="font-semibold">{l.nombre}</div>
                    <div className="text-sm text-gray-600">{l.direccion}</div>
                  </div>
                  <div className="flex gap-2">
                    <button className="px-3 py-1 bg-green-600 text-white rounded">Ver Detalles</button>
                    <button className="px-3 py-1 bg-blue-500 text-white rounded">Enviar pedido</button>
                  </div>
                </div>
              </li>
            ))}
          </ul>
          <div className="mt-4"><button onClick={()=>setView('home')} className="px-3 py-1 bg-gray-200 rounded">Volver página anterior</button></div>
        </div>
      )}

      {view==='add-food' && (
        <div className="bg-white p-6 rounded shadow">
          <h3 className="font-semibold mb-4">Agregar Comida</h3>
          <p className="text-sm text-gray-600 mb-4">(Esta vista es un mock — conecta con /products para listados reales.)</p>
          <button onClick={()=>{ setCurrentCombo({...currentCombo, base:{id:1,nombre:'Pan brioche',precio:600}}); setView('home') }} className="px-4 py-2 bg-indigo-600 text-white rounded">Seleccionar Pan brioche ($600)</button>
        </div>
      )}
      {view==='add-drink' && (
        <div className="bg-white p-6 rounded shadow">
          <h3 className="font-semibold mb-4">Agregar Bebida</h3>
          <button onClick={()=>{ setCurrentCombo({...currentCombo, bebida:{id:10,nombre:'Coca-Cola',precio:300}}); setView('home') }} className="px-4 py-2 bg-indigo-600 text-white rounded">Seleccionar Coca-Cola ($300)</button>
        </div>
      )}
      {view==='add-dessert' && (
        <div className="bg-white p-6 rounded shadow">
          <h3 className="font-semibold mb-4">Agregar Postre</h3>
          <button onClick={()=>{ setCurrentCombo({...currentCombo, acompanamiento:{id:20,nombre:'Brownie',precio:200}}); setView('home') }} className="px-4 py-2 bg-indigo-600 text-white rounded">Seleccionar Brownie ($200)</button>
        </div>
      )}

    </div>
  )
}
