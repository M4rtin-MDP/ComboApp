import React from "react";
import { bebidas } from "../helpers/mockData";

export default function AddDrinkView({ setView, setCurrentCombo, currentCombo }) {
  return (
    <div className="bg-white p-6 rounded shadow">
      <h3 className="font-semibold mb-4">Selecciona una bebida</h3>
      {bebidas.map((drink) => (
        <button
          key={drink.id}
          onClick={() => {
            setCurrentCombo({ ...currentCombo, bebida: drink });
            setView("home");
          }}
          className="block w-full mb-2 px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700"
        >
          {drink.nombre}
        </button>
      ))}

      <button
        className="mt-4 px-4 py-2 bg-gray-300 rounded"
        onClick={() => setView("home")}
      >
        Volver
      </button>
    </div>
  );
}
