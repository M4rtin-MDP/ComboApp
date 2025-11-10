import React from "react";

export default function UserView({ suggestions, setView }) {
  return (
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
  );
}
