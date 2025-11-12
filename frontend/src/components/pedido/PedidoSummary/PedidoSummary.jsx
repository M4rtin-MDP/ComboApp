// src/components/pedido/PedidoSummary/PedidoSummary.jsx
import PropTypes from 'prop-types';
import styles from './PedidoSummary.module.css';

const PedidoSummary = ({ 
  categoria, 
  comida, 
  ingredientes, 
  onRemoveIngrediente,
  onFinalizarPedido,
  showFinishButton 
}) => {
  
  if (!categoria && !comida && ingredientes.length === 0) {
    return null;
  }

  return (
    <aside className={styles.sidebar}>
      <div className={styles.sidebarContent}>
        <h3>🛒 Tu Pedido</h3>
        
        {categoria && (
          <div className={styles.summarySection}>
            <p className={styles.label}>Categoría</p>
            <p className={styles.value}>{categoria.nombre}</p>
          </div>
        )}

        {comida && (
          <div className={styles.summarySection}>
            <p className={styles.label}>Comida Base</p>
            <p className={styles.value}>{comida.nombre}</p>
          </div>
        )}

        {ingredientes.length > 0 && (
          <div className={styles.summarySection}>
            <p className={styles.label}>Ingredientes ({ingredientes.length})</p>
            <ul className={styles.ingredientList}>
              {ingredientes.map(ing => (
                <li key={ing.id_ingrediente}>
                  <span>• {ing.nombre}</span>
                  <button
                    className={styles.removeBtn}
                    onClick={() => onRemoveIngrediente(ing)}
                  >
                    ✕
                  </button>
                </li>
              ))}
            </ul>
          </div>
        )}

        {showFinishButton && (
          <button 
            className={styles.finishBtn}
            onClick={onFinalizarPedido}
            disabled={ingredientes.length === 0}
          >
            {ingredientes.length === 0 
              ? 'Selecciona ingredientes' 
              : 'Finalizar Pedido'}
          </button>
        )}
      </div>
    </aside>
  );
};

PedidoSummary.propTypes = {
  categoria: PropTypes.object,
  comida: PropTypes.object,
  ingredientes: PropTypes.array.isRequired,
  onRemoveIngrediente: PropTypes.func.isRequired,
  onFinalizarPedido: PropTypes.func.isRequired,
  showFinishButton: PropTypes.bool
};

export default PedidoSummary;