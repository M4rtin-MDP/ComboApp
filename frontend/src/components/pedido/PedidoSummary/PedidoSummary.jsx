// src/components/pedido/PedidoSummary/PedidoSummary.jsx
import PropTypes from 'prop-types';
import styles from './PedidoSummary.module.css';

const PedidoSummary = ({ 
  categoriaActual,
  comidaActual,
  ingredientesActuales = [], // Default value
  onRemoveIngredienteActual,
  carrito = [], // Default value
  onRemoveItem,
  onAgregarItem,
  onFinalizarPedido,
  showActionButtons
}) => {
  
  const tieneItemActual = categoriaActual && comidaActual;
  const tieneCarrito = carrito.length > 0;
  
  if (!tieneItemActual && !tieneCarrito) {
    return null;
  }

  return (
    <aside className={styles.sidebar}>
      <div className={styles.sidebarContent}>
        <h3>🛒 Tu Pedido</h3>
        
        {/* Items ya agregados al carrito */}
        {tieneCarrito && (
          <div className={styles.carritoSection}>
            <h4 className={styles.sectionTitle}>Items agregados ({carrito.length})</h4>
            {carrito.map((item, index) => (
              <div key={item.id} className={styles.carritoItem}>
                <div className={styles.itemHeader}>
                  <span className={styles.itemNumber}>Item {index + 1}</span>
                  <button
                    className={styles.removeItemBtn}
                    onClick={() => onRemoveItem(item.id)}
                    title="Eliminar item completo"
                  >
                    🗑️
                  </button>
                </div>
                
                <div className={styles.itemDetails}>
                  <p><strong>{item.categoria.nombre}</strong></p>
                  <p className={styles.itemComida}>{item.comida.nombre}</p>
                  {item.ingredientes.length > 0 ? (
                    <ul className={styles.itemIngredientes}>
                      {item.ingredientes.map(ing => (
                        <li key={ing.id_ingrediente}>• {ing.nombre}</li>
                      ))}
                    </ul>
                  ) : (
                    <p className={styles.sinIngredientes}>Sin personalización</p>
                  )}
                </div>
              </div>
            ))}
            <div className={styles.divider}></div>
          </div>
        )}

        {/* Item actual siendo armado */}
        {tieneItemActual && (
          <div className={styles.itemActualSection}>
            <h4 className={styles.sectionTitle}>Item actual</h4>
            
            <div className={styles.summarySection}>
              <p className={styles.label}>Categoría</p>
              <p className={styles.value}>{categoriaActual.nombre}</p>
            </div>

            <div className={styles.summarySection}>
              <p className={styles.label}>Comida Base</p>
              <p className={styles.value}>{comidaActual.nombre}</p>
            </div>

            {ingredientesActuales.length > 0 && (
              <div className={styles.summarySection}>
                <p className={styles.label}>Ingredientes ({ingredientesActuales.length})</p>
                <ul className={styles.ingredientList}>
                  {ingredientesActuales.map(ing => (
                    <li key={ing.id_ingrediente}>
                      <span>• {ing.nombre}</span>
                      <button
                        className={styles.removeBtn}
                        onClick={() => onRemoveIngredienteActual(ing)}
                      >
                        ✕
                      </button>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}

        {/* Botones de acción */}
        {showActionButtons && (
          <div className={styles.actionsContainer}>
            <button 
              className={styles.addMoreBtn}
              onClick={onAgregarItem}
              disabled={!categoriaActual || !comidaActual}
            >
              ➕ Agregar otro item
            </button>
            
            <button 
              className={styles.finishBtn}
              onClick={onFinalizarPedido}
              disabled={!tieneItemActual && !tieneCarrito}
            >
              {(!tieneItemActual && !tieneCarrito)
                ? 'Agrega items al pedido' 
                : 'Finalizar Pedido'}
            </button>
          </div>
        )}
      </div>
    </aside>
  );
};

PedidoSummary.propTypes = {
  categoriaActual: PropTypes.object,
  comidaActual: PropTypes.object,
  ingredientesActuales: PropTypes.array,
  onRemoveIngredienteActual: PropTypes.func.isRequired,
  carrito: PropTypes.array,
  onRemoveItem: PropTypes.func.isRequired,
  onAgregarItem: PropTypes.func.isRequired,
  onFinalizarPedido: PropTypes.func.isRequired,
  showActionButtons: PropTypes.bool
};

export default PedidoSummary;