// src/pages/Home/Home.jsx
import { useAuthContext } from '@/store/contexts/AuthContext';
import { useNavigate } from 'react-router-dom';
import styles from './Home.module.css';

const Home = () => {
  const { user, logout } = useAuthContext();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate('/login', { replace: true });
  };

  const handleNuevoPedido = () => {
    navigate('/pedido');
  };

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <div className={styles.logo}>
          <h1>🍔 ComboApp</h1>
        </div>
        <div className={styles.userMenu}>
          <span>Hola, {user?.nombre || user?.email}!</span>
          <button onClick={handleLogout} className={styles.logoutBtn}>
            Cerrar Sesión
          </button>
        </div>
      </header>

      <main className={styles.main}>
        <div className={styles.welcome}>
          <h2>¡Bienvenido a ComboApp!</h2>
          <p>Arma tu combo perfecto y descubre los mejores restaurantes</p>
        </div>

        <div className={styles.actionCards}>
          <div className={styles.card}>
            <div className={styles.cardIcon}>🍔</div>
            <h3>Nuevo Pedido</h3>
            <p>Arma tu combo personalizado</p>
            <button className={styles.cardBtn} onClick={handleNuevoPedido}>
              Comenzar
            </button>
          </div>

          <div className={styles.card}>
            <div className={styles.cardIcon}>📋</div>
            <h3>Ver mis pedidos</h3>
            <p>Historial de tus pedidos</p>
            <button className={styles.cardBtn}>Ver</button>
          </div>

          <div className={styles.card}>
            <div className={styles.cardIcon}>⚙️</div>
            <h3>Opciones de Usuario</h3>
            <p>Configura tu perfil y preferencias</p>
            <button className={styles.cardBtn}>Configurar</button>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Home;