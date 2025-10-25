export default function DetailsScreen({local, combo, onBack, onAddToCombo, onOrder}){
  if(!local) return <div className="card">Local no seleccionado</div>
  return (
    <div>
      <h2>Local: {local.nombre}</h2>
      <div className="card" style={{marginBottom:12}}>
        <p><strong>Productos disponibles:</strong></p>
        <p><strong>Base:</strong> Pan brioche ($600)</p>
        <p><strong>Ingredientes:</strong> Lechuga ($100), Queso ($200), Bacon ($250)</p>
        <p><strong>Bebidas:</strong> Cola ($300), Agua ($200)</p>
      </div>
      <div className="row">
        <button className="btn" onClick={onAddToCombo}>Agregar al combo</button>
        <button className="btn-ghost" onClick={onBack}>Volver página anterior</button>
        <button className="btn" onClick={onOrder}>Enviar pedido</button>
      </div>
    </div>
  )
}
