import React from "react";
import { ingredientes } from "../helpers/mockData";

export default function AddIngredientsView({
  setView,
  toggleIngredient,
  currentCombo,
}) {
  return (
    <div className="bg-white p-6 rounded shadow">
      <h3 className="font-semibold mb-4">Selecciona tus Ingredientes</h3>
      {ingredientes.map((ing) => (
        <button
          key={ing.id}
          onClick={() => toggleIngredient(ing)}
          className={`block w-full mb-2 px-4 py-2 rounded ${
            currentCombo.ingredientes.find((i) => i.id === ing.id)
              ? "bg-green-600 text-white"
              : "bg-gray-200 text-gray-800"
          }`}
        >
          {ing.nombre}
        </button>
      ))}

      <div className="mt-4 flex justify-between">
        <button
          className="px-4 py-2 bg-gray-300 rounded"
          onClick={() => setView("home")}
        >
          Volver
        </button>
        <button
          className="px-4 py-2 bg-blue-500 text-white rounded"
          onClick={() => setView("home")}
        >
          Confirmar Ingredientes
        </button>
      </div>
    </div>
  );
}
