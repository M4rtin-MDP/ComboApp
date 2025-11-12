import React, { useState, useEffect } from "react";
import api from "../services/api";
import Home from "../pages/Home/Home";
import UserView from "../pages/views/UserView";
import AddFoodView from "../pages/views/AddFoodView";
import AddIngredientsView from "../pages/views/AddIngredientsView";
import AddDrinkView from "../pages/views/AddDrinkView";
import AddDessertView from "../pages/views/AddDessertView";

/**
 * El componente MainScreen (o MainLayout, o AppLayout) no es una página, sino una plantilla o contenedor principal que envuelve las páginas que comparten la misma estructura general.
 * Por ejemplo, si todas tus pantallas de usuario autenticado tienen:
 * Una barra lateral (Sidebar)
 * Un Navbar
 * Un footer
 * Y un área de contenido central. 
 * MainScreen define esa estructura.
 */

export default function MainScreen({ onLogout }) {
  const [view, setView] = useState("home");
  const [suggestions, setSuggestions] = useState([]);
  const [combos, setCombos] = useState([]);
  const [currentCombo, setCurrentCombo] = useState({
    base: null,
    ingredientes: [],
    bebida: null,
    postre: null,
  });

  useEffect(() => {
    api
      .get("/combos")
      .then((r) => setCombos(r.data))
      .catch(() => setCombos([]));
  }, []);

  const verSugerencias = async () => {
    try {
      const res = await api.get("/locales");
      setSuggestions(res.data);
    } catch {
      setSuggestions([
        { id: 1, nombre: "BurgerMix", direccion: "Av. Siempre Viva 742" },
        { id: 2, nombre: "Papas & Burgers", direccion: "Calle Falsa 123" },
      ]);
    }
    setView("user");
  };

  const toggleIngredient = (ingredient) => {
    const exists = currentCombo.ingredientes.find((i) => i.id === ingredient.id);
    setCurrentCombo({
      ...currentCombo,
      ingredientes: exists
        ? currentCombo.ingredientes.filter((i) => i.id !== ingredient.id)
        : [...currentCombo.ingredientes, ingredient],
    });
  };

  const renderView = () => {
    switch (view) {
      case "home":
        return (
          <Home
            setView={setView}
            verSugerencias={verSugerencias}
            onLogout={onLogout}
            currentCombo={currentCombo}
            suggestions={suggestions}
          />
        );
      case "user":
        return <UserView suggestions={suggestions} setView={setView} />;
      case "add-food":
        return (
          <AddFoodView
            setView={setView}
            setCurrentCombo={setCurrentCombo}
            currentCombo={currentCombo}
          />
        );
      case "add-ingredients":
        return (
          <AddIngredientsView
            setView={setView}
            toggleIngredient={toggleIngredient}
            currentCombo={currentCombo}
          />
        );
      case "add-drink":
        return (
          <AddDrinkView
            setView={setView}
            setCurrentCombo={setCurrentCombo}
            currentCombo={currentCombo}
          />
        );
      case "add-dessert":
        return (
          <AddDessertView
            setView={setView}
            setCurrentCombo={setCurrentCombo}
            currentCombo={currentCombo}
          />
        );
      default:
        return null;
    }
  };

  return (
    <div className="min-h-screen p-6 bg-gray-50">
      <header className="flex justify-between items-center mb-6">
        <div className="text-2xl font-bold text-orange-500">🍔 ComboApp</div>
        <div className="flex gap-2">
          <button onClick={() => setView("home")}>Inicio</button>
          <button onClick={() => setView("user")}>Mi usuario</button>
          <button onClick={onLogout}>Cerrar sesión</button>
        </div>
      </header>

      {renderView()}
    </div>
  );
}
