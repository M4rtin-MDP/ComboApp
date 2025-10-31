import React, { useState, useEffect } from 'react'
import api from '../api/client'

export default function MainScreen({ onLogout }) {
  const [view, setView] = useState('home')
  const [suggestions, setSuggestions] = useState([])
  const [combos, setCombos] = useState([])
  const [currentCombo, setCurrentCombo] = useState({
    base: null,
    ingredients: [],
    bebida: null,
    acompanamiento: null
  })

  useEffect(() => {
    api.get('/combos').then(r => setCombos(r.data)).catch(() => setCombos([]))
  }, [])

  const guardarCombo = async () => {
    try {
      const payload = {
        nombre: 'Combo desde frontend',
        base_id: currentCombo.base?.id || 1,
        ingredient_ids: currentCombo.ingredients.map(i => i.id),
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
    const res = await api.get("/locales"); // o /locals/search si existe en tu backend
    setSuggestions(res.data);
  } catch {
    // Mock temporal si el backend no responde
    setSuggestions([
      { id: 1, nombre: "BurgerMix", direccion: "Av. Siempre Viva 742" },
      { id: 2, nombre: "Papas & Burgers", direccion: "Calle Falsa 123" },
    ]);
  }
  setView("user");
};

  const toggleIngredient = (ingredient) => {
    const exists = currentCombo.ingredients.find(i => i.id === ingredient.id)
    if (exists) {
      setCurrentCombo({
        ...currentCombo,
        ingredients: currentCombo.ingredients.filter(i => i.id !== ingredient.id)
      })
    } else {
      setCurrentCombo({
        ...currentCombo,
        ingredients: [...currentCombo.ingredients, ingredient]
      })
    }
  }

  return (
    <div className="min-h-screen p-6 bg-gray-50">
      <header className="flex justify-between items-center mb-6">
        <div className="text-2xl font-bold text-orange-500">🍔 ComboApp</div>
        <div className="flex gap-2">
          <button className="px-3 py-1 text-sm" onClick={() => setView('home')}>Inicio</button>
          <button className="px-3 py-1 text-sm" onClick={() => setView('user')}>Mi usuario</button>
          <button className="px-3 py-1 text-sm" onClick={onLogout}>Cerrar sesión</button>
        </div>
      </header>

      {view === 'home' && (
        <main className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white p-6 rounded shadow">
            <h3 className="text-lg font-semibold mb-4">Crea tu combo preferido!</h3>
            <div className="flex flex-col gap-2">
              <button className="px-4 py-2 bg-blue-500 text-white rounded" onClick={() => setView('add-food')}>Agregar Comida +</button>
              <button className="px-4 py-2 bg-blue-500 text-white rounded" onClick={() => setView('add-ingredients')}>Agregar Ingredientes +</button>
              <button className="px-4 py-2 bg-blue-500 text-white rounded" onClick={() => setView('add-drink')}>Agregar Bebida +</button>
              <button className="px-4 py-2 bg-blue-500 text-white rounded" onClick={() => setView('add-dessert')}>Agregar Postre +</button>
            </div>

            <div className="mt-4 flex gap-2 flex-wrap">
              <button className="px-4 py-2 bg-green-600 text-white rounded" onClick={verSugerencias}>Ver locales Sugeridos</button>
              <button className="px-4 py-2 bg-green-600 text-white rounded" onClick={guardarCombo}>Guardar Combo Favorito</button>
            </div>
          </div>

          <aside className="bg-white p-6 rounded shadow">
            <h4 className="text-lg font-semibold mb-2">Tu combo elegido:</h4>
            <div className="text-sm">
              <p>Base: {currentCombo.base?.nombre || '---'}</p>
              <p>Ingredientes: {currentCombo.ingredients.map(i => i.nombre).join(', ') || '---'}</p>
              <p>Bebida: {currentCombo.bebida?.nombre || '---'}</p>
              <p>Acompañamiento: {currentCombo.acompanamiento?.nombre || '---'}</p>
            </div>

            <div className="mt-4">
              <h5 className="font-semibold mb-2">Sugerencias:</h5>
              <ul>
                {suggestions.map(s => (
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
                {suggestions.length === 0 && <li className="text-sm text-gray-500">No hay sugerencias aún.</li>}
              </ul>
            </div>
          </aside>
        </main>
      )}

{view === "user" && (
  <div className="bg-white p-6 rounded shadow">
    <h3 className="font-semibold mb-4 text-lg">Locales cercanos</h3>

    {suggestions.length === 0 ? (
      <p className="text-gray-500">No se encontraron locales.</p>
    ) : (
      <ul>
        {suggestions.map((s) => (
          <li key={s.id} className="mb-3 border-b pb-3">
            <div className="flex justify-between items-center">
              <div>
                <p className="font-semibold text-gray-800">{s.nombre}</p>
                <p className="text-sm text-gray-600">{s.direccion}</p>
              </div>
              <button
                onClick={() => alert(`Seleccionaste ${s.nombre}`)}
                className="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
              >
                Ver Detalles
              </button>
            </div>
          </li>
        ))}
      </ul>
    )}

    <div className="mt-4 flex justify-between">
      <button
        className="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400"
        onClick={() => setView("home")}
      >
        Volver
      </button>
    </div>
  </div>
)}

      {/* VISTAS EXISTENTES */}

      {view === 'add-ingredients' && (
  <div className="bg-white p-6 rounded shadow">
    <h3 className="font-semibold mb-4">Selecciona tus Ingredientes</h3>
    <p className="text-sm text-gray-600 mb-4">(Vista mock — luego se conecta al backend /ingredientes)</p>

    {[
      { id: 1, nombre: 'Queso Cheddar' },
      { id: 2, nombre: 'Lechuga' },
      { id: 3, nombre: 'Tomate' },
      { id: 4, nombre: 'Cebolla Caramelizada' },
    ].map(ing => (
      <button
        key={ing.id}
        onClick={() => toggleIngredient(ing)}
        className={`block w-full mb-2 px-4 py-2 rounded ${
          currentCombo.ingredients.find(i => i.id === ing.id)
            ? 'bg-green-600 text-white'
            : 'bg-gray-200 text-gray-800'
        }`}
      >
        {ing.nombre}
      </button>
    ))}

    <div className="mt-4 flex justify-between">
      <button
        className="px-4 py-2 bg-gray-300 rounded"
        onClick={() => setView('home')}
      >
        Volver
      </button>
      <button
        className="px-4 py-2 bg-blue-500 text-white rounded"
        onClick={() => setView('home')}
      >
        Confirmar Ingredientes
      </button>
    </div>
  </div>
)}

      {view === 'add-food' && (
  <div className="bg-white p-6 rounded shadow">
    <h3 className="font-semibold mb-4">Selecciona una comida base</h3>

    {[
      { id: 1, nombre: 'Hamburguesa Simple', precio: 600 },
      { id: 2, nombre: 'Hamburguesa Doble', precio: 850 },
      { id: 3, nombre: 'Hamburguesa Veggie', precio: 700 },
      { id: 4, nombre: 'Pollo Crispy', precio: 780 },
      { id: 5, nombre: 'Lomito Simple', precio: 950 },
    ].map(food => (
      <button
        key={food.id}
        onClick={() => {
          setCurrentCombo({ ...currentCombo, base: food });
          setView('home');
        }}
        className="block w-full mb-2 px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700"
      >
        {food.nombre} (${food.precio})
      </button>
    ))}

    <button
      className="mt-4 px-4 py-2 bg-gray-300 rounded"
      onClick={() => setView('home')}
    >
      Volver
    </button>
  </div>
)}

      {view === 'add-drink' && (
  <div className="bg-white p-6 rounded shadow">
    <h3 className="font-semibold mb-4">Selecciona una bebida</h3>

    {[
      { id: 10, nombre: 'Coca-Cola', precio: 300 },
      { id: 11, nombre: 'Sprite', precio: 280 },
      { id: 12, nombre: 'Agua Mineral', precio: 200 },
      { id: 13, nombre: 'Cerveza', precio: 500 },
      { id: 14, nombre: 'Jugo de Naranja', precio: 320 },
    ].map(drink => (
      <button
        key={drink.id}
        onClick={() => {
          setCurrentCombo({ ...currentCombo, bebida: drink });
          setView('home');
        }}
        className="block w-full mb-2 px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700"
      >
        {drink.nombre} (${drink.precio})
      </button>
    ))}

    <button
      className="mt-4 px-4 py-2 bg-gray-300 rounded"
      onClick={() => setView('home')}
    >
      Volver
    </button>
  </div>
)}

{view === 'add-dessert' && (
  <div className="bg-white p-6 rounded shadow">
    <h3 className="font-semibold mb-4">Selecciona un postre o acompañamiento</h3>

    {[
      { id: 20, nombre: 'Brownie', precio: 200 },
      { id: 21, nombre: 'Helado', precio: 250 },
      { id: 22, nombre: 'Tiramisu', precio: 300 },
      { id: 23, nombre: 'Ensalada de frutas', precio: 280 },
      { id: 24, nombre: 'Tarta de Manzana', precio: 320 },
    ].map(dessert => (
      <button
        key={dessert.id}
        onClick={() => {
          setCurrentCombo({ ...currentCombo, acompanamiento: dessert });
          setView('home');
        }}
        className="block w-full mb-2 px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700"
      >
        {dessert.nombre} (${dessert.precio})
      </button>
    ))}

    <button
      className="mt-4 px-4 py-2 bg-gray-300 rounded"
      onClick={() => setView('home')}
    >
      Volver
    </button>
  </div>
)}
    </div>
  )
}


