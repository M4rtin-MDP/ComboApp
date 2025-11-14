// src/pages/MisPedidos/MisPedidos.jsx
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthContext } from '@/store/contexts/AuthContext';
import { pedidoService } from '@/services/api/pedidoService';
import { restauranteService } from '@/services/api/restauranteService';
import styles from './MisPedidos.module.css';

// Mapeo de estados
const ESTADOS = {
  1: { label: 'Pendiente', color: '#ffc107', icon: '⏳' },
  2: { label: 'Confirmado', color: '#17a2b8', icon: '✓' },
  3: { label: 'Cancelado', color: '#dc3545', icon: '❌' },
  4: { label: 'En camino', color: '#6f42c1', icon: '🚴' },
  5: { label: 'Entregado', color: '#28a745', icon: '✅' },
  6: { label: 'En preparación', color: '#007bff', icon: '👨‍🍳' }
};

const MisPedidos = () => {
  const navigate = useNavigate();
  const { user } = useAuthContext();
  
  const [pedidos, setPedidos] = useState([]);
  const [pedidosExpandidos, setPedidosExpandidos] = useState({});
  const [detallesPedidos, setDetallesPedidos] = useState({});
  const [restaurantes, setRestaurantes] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!user?.id_usuario) {
      navigate('/login');
      return;
    }
    
    cargarPedidos();
  }, []);

  const cargarPedidos = async () => {
    setLoading(true);
    const result = await pedidoService.getPedidosUsuario(user.id_usuario);
    
    if (result.success) {
      const pedidosOrdenados = result.data.sort((a, b) => 
        new Date(b.fecha) - new Date(a.fecha)
      );
      
      setPedidos(pedidosOrdenados);
      
      // Expandir el primero automáticamente
      if (pedidosOrdenados.length > 0) {
        const primerPedido = pedidosOrdenados[0].id_pedido;
        setPedidosExpandidos({ [primerPedido]: true });
        await cargarDetallePedido(primerPedido);
      }
    } else {
      setError(result.message);
    }
    
    setLoading(false);
  };

  const cargarDetallePedido = async (id_pedido) => {
    const pedido = pedidos.find(p => p.id_pedido === id_pedido);
    
    // Cargar restaurante si no está en cache
    if (pedido && !restaurantes[pedido.id_restaurante]) {
      const resultRestaurante = await restauranteService.getRestauranteById(pedido.id_restaurante);
      
      if (resultRestaurante.success) {
        setRestaurantes(prev => ({
          ...prev,
          [pedido.id_restaurante]: resultRestaurante.data.nombre
        }));
      }
    }

    // Cargar detalle de combos
    const resultDetalle = await pedidoService.getDetalleCombosPedido(id_pedido);
    
    if (resultDetalle.success) {
      setDetallesPedidos(prev => ({
        ...prev,
        [id_pedido]: agruparCombosPorItem(resultDetalle.data)
      }));
    }
  };

  const agruparCombosPorItem = (combos) => {
    const itemsMap = {};
    
    combos.forEach(combo => {
      const itemId = combo.item_comida;
      
      if (!itemsMap[itemId]) {
        itemsMap[itemId] = {
          comida: combo.comida,
          ingredientes: []
        };
      }
      
      if (combo.ingrediente) {
        itemsMap[itemId].ingredientes.push(combo.ingrediente);
      }
    });
    
    return Object.values(itemsMap);
  };

  const togglePedido = async (id_pedido) => {
    const estaExpandido = pedidosExpandidos[id_pedido];
    
    setPedidosExpandidos(prev => ({
      ...prev,
      [id_pedido]: !estaExpandido
    }));

    // Si se está expandiendo y no tiene detalles, cargarlos
    if (estaExpandido && !detallesPedidos[id_pedido]) {
      await cargarDetallePedido(id_pedido);
    }
  };

  const formatearFecha = (fecha) => {
    return new Date(fecha).toLocaleDateString('es-AR', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.loading}>
          <div className={styles.spinner}></div>
          <p>Cargando tus pedidos...</p>
        </div>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <button onClick={() => navigate('/home')} className={styles.backBtn}>
          ← Volver
        </button>
        <h1>Mis Pedidos</h1>
      </header>

      <main className={styles.main}>
        {error && (
          <div className={styles.errorBox}>
            <p>❌ {error}</p>
          </div>
        )}

        {pedidos.length === 0 ? (
          <div className={styles.emptyState}>
            <div className={styles.emptyIcon}>📦</div>
            <h2>No tienes pedidos aún</h2>
            <p>Cuando realices tu primer pedido, aparecerá aquí</p>
            <button onClick={() => navigate('/pedido')} className={styles.ctaBtn}>
              Hacer mi primer pedido
            </button>
          </div>
        ) : (
          <div className={styles.pedidosList}>
            {pedidos.map((pedido, index) => {
              const estaExpandido = pedidosExpandidos[pedido.id_pedido];
              const estado = ESTADOS[pedido.id_estado] || ESTADOS[1];
              const detalle = detallesPedidos[pedido.id_pedido];
              const nombreRestaurante = restaurantes[pedido.id_restaurante];

              return (
                <div
                  key={pedido.id_pedido}
                  className={`${styles.pedidoCard} ${estaExpandido ? styles.expandido : ''}`}
                >
                  {/* Header del pedido (siempre visible) */}
                  <div
                    className={styles.pedidoHeader}
                    onClick={() => togglePedido(pedido.id_pedido)}
                  >
                    <div className={styles.pedidoHeaderLeft}>
                      <h3>Pedido #{pedido.id_pedido}</h3>
                      <p className={styles.fecha}>{formatearFecha(pedido.fecha)}</p>
                    </div>

                    <div className={styles.pedidoHeaderRight}>
                      <span
                        className={styles.estadoBadge}
                        style={{ backgroundColor: estado.color }}
                      >
                        {estado.icon} {estado.label}
                      </span>
                      <span className={styles.total}>${pedido.total.toFixed(2)}</span>
                      <span className={styles.expandIcon}>
                        {estaExpandido ? '▼' : '▶'}
                      </span>
                    </div>
                  </div>

                  {/* Contenido expandido */}
                  {estaExpandido && (
                    <div className={styles.pedidoContent}>
                      {/* Restaurante */}
                      {nombreRestaurante && (
                        <div className={styles.restauranteInfo}>
                          <p className={styles.label}>🏪 Restaurante</p>
                          <p className={styles.value}>{nombreRestaurante}</p>
                        </div>
                      )}

                      {/* Detalle de items */}
                      {detalle ? (
                        <div className={styles.itemsDetalle}>
                          <p className={styles.label}>📦 Detalle del pedido</p>
                          <div className={styles.itemsList}>
                            {detalle.map((item, idx) => (
                              <div key={idx} className={styles.itemCard}>
                                <div className={styles.itemHeader}>
                                  <span className={styles.itemNumber}>{idx + 1}</span>
                                  <h4>{item.comida}</h4>
                                </div>
                                
                                {item.ingredientes.length > 0 && (
                                  <ul className={styles.ingredientesList}>
                                    {item.ingredientes.map((ing, i) => (
                                      <li key={i}>• {ing}</li>
                                    ))}
                                  </ul>
                                )}
                              </div>
                            ))}
                          </div>
                        </div>
                      ) : (
                        <div className={styles.loadingDetalle}>
                          <div className={styles.spinnerSmall}></div>
                          <p>Cargando detalles...</p>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </main>
    </div>
  );
};

export default MisPedidos;