export default function HomeScreen({onAdd, onSuggest}){
  return (
    <div className="hero card">
      <h2>¡Creá tu combo ideal!</h2>
      <div className="row" style={{marginTop:12}}>
        <button className="btn" onClick={onAdd}>Agregar Comida +</button>
        <button className="btn" onClick={onAdd}>Agregar Bebida +</button>
        <button className="btn" onClick={onAdd}>Agregar Postre +</button>
      </div>
      <div style={{marginTop:14}} className="center">
        <button className="btn-ghost" onClick={onSuggest}>Ver sugerencias de locales Cercanos</button>
        <button className="btn-ghost" style={{marginLeft:8}}>Guardar Combo Favorito</button>
      </div>
    </div>
  )
}
