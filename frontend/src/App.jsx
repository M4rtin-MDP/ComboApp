import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login/Login";
import AppLayout from "./layouts/AppLayouts";
import HomeView from "./pages/views/HomeView";
import AddFoodView from "./pages/views/AddFoodView";
import AddIngredientsView from "./pages/views/AddIngredientsView";
import AddDrinkView from "./pages/views/AddDrinkView";
import AddDessertView from "./pages/views/AddDessertView";

//localStorage.setItem("token", "fake-dev-token");

export default function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || null);

  useEffect(() => {
    if (token) localStorage.setItem("token", token);
    else localStorage.removeItem("token");
  }, [token]);

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login onLogin={setToken} />} />
        {/* Rutas protegidas - Solo si hay token */}
        {token ? (
          <Route element={<AppLayout onLogout={() => setToken(null)} />}>
            <Route path="/home" element={<HomeView />} />
            <Route path="/add-food" element={<AddFoodView />} />
            <Route path="/add-ingredients" element={<AddIngredientsView />} />
            <Route path="/add-drink" element={<AddDrinkView />} />
            <Route path="/add-dessert" element={<AddDessertView />} />
            <Route path="*" element={<Navigate to="/home" replace />} />
          </Route>
        ) : (
          <Route path="*" element={<Navigate to="/login" replace />} />
        )}
      </Routes>
    </Router>
  );
}


