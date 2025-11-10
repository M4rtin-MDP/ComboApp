import React from "react";
import { Outlet, Link } from "react-router-dom";

export default function AppLayout({ onLogout }) {
  return (
    <div className="min-h-screen p-6 bg-gray-50">
      <header className="flex justify-between items-center mb-6">
        <div className="text-2xl font-bold text-orange-500">
          🍔 ComboApp
        </div>

        <nav className="flex gap-4">
          <Link to="/home" className="text-blue-600 hover:underline">Inicio</Link>
          <Link to="/add-food" className="text-blue-600 hover:underline">Comidas</Link>
          <Link to="/add-ingredients" className="text-blue-600 hover:underline">Ingredientes</Link>
          <Link to="/add-drink" className="text-blue-600 hover:underline">Bebidas</Link>
          <Link to="/add-dessert" className="text-blue-600 hover:underline">Postres</Link>
          <button onClick={onLogout} className="text-red-600 hover:underline">
            Cerrar sesión
          </button>
        </nav>
      </header>

      {/* Aquí se renderiza la página actual */}
      <main>
        <Outlet />
      </main>
    </div>
  );
}


