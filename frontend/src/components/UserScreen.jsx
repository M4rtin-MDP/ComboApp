export default function UserScreen({combo, locals, onChooseLocal, onBack, onAddIngredient}){
  return (
    <div>
      <h2>Bienvenido!</h2>
      <div className="card" style={{marginBottom:12}}>
        <h3>Tus combo elegido:</h3>
        <p className="small">{combo.base ? combo.base.nombre : '(sin base)'} {combo.ingredients.length>0?'+ ' + combo.ingredients.map(i=>i.nombre).join(' + '):''} {combo.bebida?'+ '+combo.bebida.nombre:''}</p>
      </div>

      <div className="card" style={{marginBottom:12}}>
        <h3>Sugerencias de locales:</h3>
        <ul className="list">
          {locals && locals.length>0 ? locals.map(l => (
            <li key={l.id}>
              <div>
                <strong>{l.nombre}</strong> <div className="small">{l.direccion || ''}</div>
              </div>
              <div>
                <div style={{fontSize:14}}>${l.id ? 1500 + (l.id%5)*50 : 1500}</div>
                <button className="btn-ghost" onClick={()=>onChooseLocal(l)}>Ver Detalles</button>
              </div>
            </li>
          )) : <li className="small">No hay locales cargados.</li>}
        </ul>
      </div>

      <div className="center">
        <button className="btn-ghost" onClick={onBack}>Volver página anterior</button>
      </div>
    </div>
  )
}
