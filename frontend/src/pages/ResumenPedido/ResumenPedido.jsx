// src/pages/ResumenPedido/ResumenPedido.jsx
import { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { useAuthContext } from '@/store/contexts/AuthContext';
import { pedidoService } from '@/services/api/pedidoService';
import styles from './ResumenPedido.module.css';

const ResumenPedido = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { user } = useAuthContext();
  
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  
  const { pedido, restaurante } = location.state || {};

  // Validar que tengamos los datos necesarios
  if (!pedido || !restaurante) {
    navigate('/pedido');
    return null;
  }

  const handleConfirmarPedido = async () => {
    if (!user?.id_usuario) {
      setError('Usuario no autenticado');
      return;
    }

    setLoading(true);
    setError('');

    // Preparar datos para el servicio
    const datos = {
      id_usuario: user.id_usuario,
      id_restaurante: restaurante.id_restaurante || 0, // Ajustar según tu backend
      total: restaurante.precio_total,
      carrito: pedido
    };

    const result = await pedidoService.crearPedidoCompleto(datos);

    if (result.success) {
      // Redirigir a Mis Pedidos
																 
      navigate('/mis-pedidos');
    } else {
							
      setError(result.message);
    }

    setLoading(false);
  };

  const handleVolver = () => {
    navigate('/pedido/restaurantes-disponibles', { 
      state: { pedido } 
    });
  };

  const calcularSubtotal = () => {
    return restaurante.precio_original || 0;
  };

  const calcularEnvio = () => {
    return (restaurante.precio_total || 0) - (restaurante.precio_original || 0);
  };

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <button onClick={handleVolver} className={styles.backBtn}>
          ← Volver
        </button>
        <h1>Resumen del Pedido</h1>
      </header>

      <div className={styles.content}>
        {/* Columna principal */}
        <main className={styles.main}>
          {/* Restaurante seleccionado */}
          <section className={styles.section}>
            <h2>🏪 Restaurante</h2>
            <div className={styles.restauranteCard}>
              <h3>{restaurante.nombre}</h3>
              <p className={styles.ubicacion}>
                📍 {restaurante.latitud.toFixed(4)}, {restaurante.longitud.toFixed(4)}
              </p>
            </div>
          </section>

          {/* Items del pedido */}
          <section className={styles.section}>
            <h2>📦 Tu Pedido ({pedido.length} items)</h2>
            <div className={styles.itemsList}>
              {pedido.map((item, index) => (
                <div key={item.id} className={styles.itemCard}>
                  <div className={styles.itemHeader}>
                    <span className={styles.itemNumber}>{index + 1}</span>
                    <div className={styles.itemInfo}>
                      <h4>{item.comida.nombre}</h4>
                      <p className={styles.categoria}>{item.categoria.nombre}</p>
                    </div>
                  </div>
                  
                  {item.ingredientes.length > 0 && (
                    <div className={styles.ingredientes}>
                      <p className={styles.ingredientesLabel}>Ingredientes:</p>
                      <ul>
                        {item.ingredientes.map(ing => (
                          <li key={ing.id_ingrediente}>• {ing.nombre}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </section>

          {error && (
            <div className={styles.errorBox}>
              <p>❌ {error}</p>
            </div>
          )}
        </main>

        {/* Sidebar con resumen de precios */}
        <aside className={styles.sidebar}>
          <div className={styles.sidebarContent}>
            <h3>💰 Resumen de Pago</h3>
            
            <div className={styles.preciosDetalle}>
              <div className={styles.precioRow}>
                <span>Subtotal:</span>
                <span>${calcularSubtotal().toFixed(2)}</span>
              </div>
              
              <div className={styles.precioRow}>
                <span>Envío:</span>
                <span>${calcularEnvio().toFixed(2)}</span>
              </div>
              
              <div className={styles.divider}></div>
              
              <div className={styles.precioRow + ' ' + styles.total}>
                <span>Total:</span>
                <span className={styles.totalMonto}>
                  ${restaurante.precio_total.toFixed(2)}
                </span>
              </div>
            </div>

            <button
              className={styles.confirmarBtn}
              onClick={handleConfirmarPedido}
              disabled={loading}
            >
              {loading ? (
                <>
                  <span className={styles.spinner}></span>
                  Procesando...
                </>
              ) : (
                'Confirmar Pedido'
              )}
            </button>

            <p className={styles.infoText}>
              Al confirmar, se procesará tu pedido y se enviará al restaurante.
            </p>
          </div>
        </aside>
      </div>
    </div>
  );
};

export default ResumenPedido;