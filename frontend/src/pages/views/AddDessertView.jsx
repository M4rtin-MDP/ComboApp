import React from "react";
import { postres } from "../helpers/mockData";

export default function AddDessertView({ setView, setCurrentCombo, currentCombo }) {
  return (
    <div className="bg-white p-6 rounded shadow">
      <h3 className="font-semibold mb-4">Selecciona un postre o acompañamiento</h3>
      {postres.map((dessert) => (
        <button
          key={dessert.id}
          onClick={() => {
            setCurrentCombo({ ...currentCombo, postre: dessert });
            setView("home");
          }}
          className="block w-full mb-2 px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700"
        >
          {dessert.nombre}
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

