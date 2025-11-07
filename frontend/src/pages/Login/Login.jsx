import React, { useState } from "react";
import api from "../../api/client";

export default function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const res = await api.post("/login", { username, password });
      localStorage.setItem("token", res.data.access_token);
      onLogin(res.data.access_token);
    } catch (err) {
      setError("Credenciales incorrectas o servidor no disponible.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <form
        onSubmit={handleLogin}
        className="bg-white p-8 rounded shadow-md w-80 flex flex-col gap-4"
      >
        <h2 className="text-xl font-bold text-center text-orange-600">🍔 ComboApp</h2>
        <input
          type="text"
          placeholder="Usuario"
          className="border p-2 rounded"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Contraseña"
          className="border p-2 rounded"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {error && <p className="text-red-500 text-sm text-center">{error}</p>}
        <button type="submit" className="bg-orange-500 text-white py-2 rounded hover:bg-orange-600">
          Ingresar
        </button>
      </form>
    </div>
  );
}

