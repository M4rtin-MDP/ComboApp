import { useEffect, useState } from "react";
import { getIngredients, createCombo } from "../api/client.js";

export default function ComboBuilder({ token }) {
  const [ingredients, setIngredients] = useState([]);
  const [selectedIngredients, setSelectedIngredients] = useState([]);
  const [comboName, setComboName] = useState("");

  useEffect(() => {
    getIngredients(token)
      .then(res => setIngredients(res.data))
      .catch(() => alert("Error al obtener ingredientes"));
  }, [token]);

  const toggleIngredient = (id) => {
    setSelectedIngredients(prev =>
      prev.includes(id) ? prev.filter(i => i !== id) : [...prev, id]
    );
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!comboName || selectedIngredients.length === 0) {
      alert("Debes poner nombre y seleccionar al menos un ingrediente");
      return;
    }
    try {
      const res = await createCombo({ name: comboName, ingredient_ids: selectedIngredients }, token);
      alert(`Combo creado: ${res.data.name} - Total: $${res.data.total_price}`);
      setComboName("");
      setSelectedIngredients([]);
    } catch {
      alert("Error al crear combo");
    }
  };

  return (
    <div>
      <h3>Crear Combo</h3>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Nombre del combo"
          value={comboName}
          onChange={(e) => setComboName(e.target.value)}
        />
        <h4>Seleccioná ingredientes:</h4>
        {ingredients.map((ing) => (
          <label key={ing.id} style={{ display: "block" }}>
            <input
              type="checkbox"
              checked={selectedIngredients.includes(ing.id)}
              onChange={() => toggleIngredient(ing.id)}
            />
            {ing.name} (${ing.price})
          </label>
        ))}
        <button type="submit">Crear Combo</button>
      </form>
    </div>
  );
}