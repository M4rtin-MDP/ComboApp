import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login/Login";
import MainScreen from "./pages/MainScreen";

//-------------------------------------------------------
// Simula token válido (modo desarrollo)
localStorage.setItem("token", "fake-dev-token");
//------------------------------------------------------

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
        <Route
          path="/home"
          element={
            token ? (
              <MainScreen onLogout={() => setToken(null)} />
            ) : (
              <Navigate to="/login" replace />
            )
          }
        />
        <Route path="*" element={<Navigate to={token ? "/home" : "/login"} replace />} />
      </Routes>
    </Router>
  );
}
