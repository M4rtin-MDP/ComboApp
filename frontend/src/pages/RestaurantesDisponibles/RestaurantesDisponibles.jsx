// src/pages/RestaurantesDisponibles/RestaurantesDisponibles.jsx
import { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { restauranteService } from '@/services/api/restauranteService';
import styles from './RestaurantesDisponibles.module.css';

const RestaurantesDisponibles = () => {
  const location = useLocation();
  const navigate = useNavigate();
  
  const [restaurantes, setRestaurantes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [selectedRestaurante, setSelectedRestaurante] = useState(null);
  
  const pedido = location.state?.pedido;

  useEffect(() => {
    if (!pedido || pedido.length === 0) {
      navigate('/pedido');
      return;
    }
    
    buscarRestaurantes();
  }, []);

  const buscarRestaurantes = async () => {
    setLoading(true);
    setError('');
    
    const result = await restauranteService.getRestaurantesDisponibles(pedido);
    
    if (result.success) {
      setRestaurantes(result.data);
      
      if (result.data.length === 0) {
        setError('No hay restaurantes disponibles con todos los items de tu pedido');
      }
    } else {
      setError(result.message);
    }
    
    setLoading(false);
  };

  const handleSelectRestaurante = (restaurante) => {
    setSelectedRestaurante(restaurante);
  };

  const handleConfirmarRestaurante = () => {
    if (!selectedRestaurante) {
      alert('Debes seleccionar un restaurante');
      return;
    }

    // Aquí redirigirías al resumen del pedido con el restaurante seleccionado
    console.log('Restaurante seleccionado:', selectedRestaurante);
    console.log('Pedido completo:', pedido);
    
    // navigate('/pedido/resumen', { 
    //   state: { 
    //     pedido, 
    //     restaurante: selectedRestaurante 
    //   }
    // });
    
    alert(`Restaurante "${selectedRestaurante.nombre}" seleccionado. Continuaría al resumen del pedido.`);
  };

  const handleVolver = () => {
    navigate('/pedido');
  };

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.loading}>
          <div className={styles.spinner}></div>
          <p>Buscando restaurantes disponibles...</p>
        </div>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <button onClick={handleVolver} className={styles.backBtn}>
          ← Volver
        </button>
        <div>
          <h1>Restaurantes Disponibles</h1>
          <p className={styles.subtitle}>{pedido.length} item(s) en tu pedido</p>
        </div>
      </header>

      <div className={styles.content}>
        {/* Resumen del pedido */}
        <aside className={styles.pedidoResumen}>
          <h3>📦 Tu Pedido</h3>
          <div className={styles.pedidoItems}>
            {pedido.map((item, index) => (
              <div key={item.id} className={styles.pedidoItem}>
                <span className={styles.itemNumber}>{index + 1}.</span>
                <div className={styles.itemInfo}>
                  <p className={styles.itemNombre}>{item.comida.nombre}</p>
                  <p className={styles.itemCategoria}>{item.categoria.nombre}</p>
                  {item.ingredientes.length > 0 && (
                    <p className={styles.itemIngredientes}>
                      {item.ingredientes.map(ing => ing.nombre).join(', ')}
                    </p>
                  )}
                </div>
              </div>
            ))}
          </div>
        </aside>

        {/* Lista de restaurantes */}
        <main className={styles.main}>
          {error && (
            <div className={styles.errorContainer}>
              <div className={styles.errorIcon}>⚠️</div>
              <h2>No encontramos restaurantes</h2>
              <p>{error}</p>
              <button onClick={handleVolver} className={styles.errorBtn}>
                Modificar Pedido
              </button>
            </div>
          )}

          {!error && restaurantes.length > 0 && (
            <>
              <h2 className={styles.mainTitle}>
                Encontramos {restaurantes.length} restaurante(s)
              </h2>
              
              <div className={styles.restaurantesGrid}>
                {restaurantes.map((restaurante, index) => (
                  <div
                    key={index}
                    className={`${styles.restauranteCard} ${
                      selectedRestaurante?.nombre === restaurante.nombre
                        ? styles.selected
                        : ''
                    }`}
                    onClick={() => handleSelectRestaurante(restaurante)}
                  >
                    {selectedRestaurante?.nombre === restaurante.nombre && (
                      <div className={styles.checkmark}>✓</div>
                    )}
                    
                    <div className={styles.restauranteHeader}>
                      <h3>{restaurante.nombre}</h3>
                      <span className={styles.badge}>Disponible</span>
                    </div>

                    <div className={styles.restauranteInfo}>
                      <div className={styles.infoRow}>
                        <span className={styles.label}>📍 Ubicación:</span>
                        <span className={styles.value}>
                          {restaurante.latitud.toFixed(4)}, {restaurante.longitud.toFixed(4)}
                        </span>
                      </div>

                      <div className={styles.preciosContainer}>
                        <div className={styles.precioItem}>
                          <span className={styles.precioLabel}>Subtotal:</span>
                          <span className={styles.precioValor}>
                            ${restaurante.precio_original.toFixed(2)}
                          </span>
                        </div>
                        
                        <div className={styles.precioItem}>
                          <span className={styles.precioLabel}>Total (con envío):</span>
                          <span className={styles.precioTotal}>
                            ${restaurante.precio_total.toFixed(2)}
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>

              <div className={styles.confirmSection}>
                <button
                  className={styles.confirmBtn}
                  onClick={handleConfirmarRestaurante}
                  disabled={!selectedRestaurante}
                >
                  {selectedRestaurante
                    ? `Continuar con ${selectedRestaurante.nombre}`
                    : 'Selecciona un restaurante'}
                </button>
              </div>
            </>
          )}
        </main>
      </div>
    </div>
  );
};

export default RestaurantesDisponibles;