export default function Header({onLogin,onRegister}){
  return (
    <header className="header">
      <div className="logo">🍔 ComboApp</div>
      <div className="top-actions">
        <button className="btn-ghost" onClick={onLogin}>Iniciar Sesión</button>
        <button className="btn" onClick={onRegister}>Registro</button>
      </div>
    </header>
  )
}
