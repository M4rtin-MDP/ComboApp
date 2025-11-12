// src/pages/Restaurantes/Restaurantes.jsx
import { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import styles from './Restaurantes.module.css';

const Restaurantes = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const [pedido, setPedido] = useState(null);
  const [restaurantes, setRestaurantes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!location.state?.pedido) {
      navigate('/pedido');
      return;
    }

    setPedido(location.state.pedido);
    buscarRestaurantes(location.state.pedido);
  }, [location, navigate]);

  const buscarRestaurantes = async (pedidoData) => {
    setLoading(true);
    
    try {
      // Aquí harías el fetch a tu API
      // const response = await fetch('/restaurantes/disponibles_total', {
      //   method: 'POST',
      //   body: JSON.stringify(pedidoData)
      // });
      
      // Por ahora simulamos
      console.log('Buscando restaurantes con pedido:', pedidoData);
      
      // Simular delay
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      // Datos de ejemplo
      setRestaurantes([
        { id: 1, nombre: 'Restaurant A', distancia: '2km' },
        { id: 2, nombre: 'Restaurant B', distancia: '3km' }
      ]);
      
    } catch (error) {
      console.error('Error buscando restaurantes:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.loading}>
          <h2>Buscando restaurantes disponibles...</h2>
          <p>Esto puede tomar unos segundos</p>
        </div>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <button onClick={() => navigate('/pedido')} className={styles.backBtn}>
          ← Volver
        </button>
        <h1>Restaurantes Disponibles</h1>
      </header>

      <main className={styles.main}>
        <div className={styles.pedidoResumen}>
          <h3>Tu pedido:</h3>
          <pre>{JSON.stringify(pedido, null, 2)}</pre>
        </div>

        <div className={styles.restaurantesList}>
          <h2>Restaurantes encontrados ({restaurantes.length})</h2>
          {restaurantes.map(rest => (
            <div key={rest.id} className={styles.restauranteCard}>
              <h3>{rest.nombre}</h3>
              <p>Distancia: {rest.distancia}</p>
              <button className={styles.selectBtn}>Seleccionar</button>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
};

export default Restaurantes;