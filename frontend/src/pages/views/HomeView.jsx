import React from "react";

export default function HomeView({
  setView,
  verSugerencias,
  currentCombo,
  suggestions,
}) {
  return (
    <main className="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div className="bg-white p-6 rounded shadow">
        <h3 className="text-lg font-semibold mb-4">¡Crea tu combo preferido!</h3>
        <div className="flex flex-col gap-2">
          <button
            className="bg-blue-500 text-white rounded px-4 py-2"
            onClick={() => setView("add-food")}
          >
            Agregar Comida
          </button>
          <button
            className="bg-blue-500 text-white rounded px-4 py-2"
            onClick={() => setView("add-ingredients")}
          >
            Agregar Ingredientes
          </button>
          <button
            className="bg-blue-500 text-white rounded px-4 py-2"
            onClick={() => setView("add-drink")}
          >
            Agregar Bebida
          </button>
          <button
            className="bg-blue-500 text-white rounded px-4 py-2"
            onClick={() => setView("add-dessert")}
          >
            Agregar Postre
          </button>
        </div>

        <div className="mt-4 flex gap-2 flex-wrap">
          <button
            className="bg-green-600 text-white rounded px-4 py-2"
            onClick={verSugerencias}
          >
            Ver locales sugeridos
          </button>
        </div>
      </div>

      <aside className="bg-white p-6 rounded shadow">
        <h4 className="text-lg font-semibold mb-2">Tu combo elegido:</h4>
        <div className="text-sm">
          <p>Base: {currentCombo.base?.nombre || "---"}</p>
          <p>
            Ingredientes:{" "}
            {currentCombo.ingredientes.map((i) => i.nombre).join(", ") || "---"}
          </p>
          <p>Bebida: {currentCombo.bebida?.nombre || "---"}</p>
          <p>Postre: {currentCombo.postre?.nombre || "---"}</p>
        </div>

        <div className="mt-4">
          <h5 className="font-semibold mb-2">Sugerencias:</h5>
          <ul>
            {suggestions.map((s) => (
              <li key={s.id} className="mb-2 border-b pb-2">
                <div className="flex justify-between">
                  <div>
                    <div className="font-semibold">{s.nombre}</div>
                    <div className="text-sm text-gray-600">{s.direccion}</div>
                  </div>
                  <button className="px-3 py-1 bg-blue-500 text-white rounded">
                    Ver Detalles
                  </button>
                </div>
              </li>
            ))}
            {suggestions.length === 0 && (
              <li className="text-sm text-gray-500">No hay sugerencias aún.</li>
            )}
          </ul>
        </div>
      </aside>
    </main>
  );
}
