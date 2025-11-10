import React from "react";
import { comidas } from "../helpers/mockData";

export default function AddFoodView({ setView, setCurrentCombo, currentCombo }) {
  return (
    <div className="bg-white p-6 rounded shadow">
      <h3 className="font-semibold mb-4">Selecciona una comida base</h3>
      {comidas.map((food) => (
        <button
          key={food.id}
          onClick={() => {
            setCurrentCombo({ ...currentCombo, base: food });
            setView("home");
          }}
          className="block w-full mb-2 px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700"
        >
          {food.nombre}
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
