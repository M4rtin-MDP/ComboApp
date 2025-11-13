// src/components/pedido/IngredientSelector/IngredientSelector.jsx
import PropTypes from 'prop-types';
import styles from './IngredientSelector.module.css';

const IngredientSelector = ({ 
  ingredientes, 
  selectedIngredientes, 
  comidaName, 
  onToggleIngrediente 
}) => {
  
  // Si no hay ingredientes disponibles
  if (!ingredientes || ingredientes.length === 0) {
    return (
      <div className={styles.container}>
        <h2>Selecciona Ingredientes</h2>
        <p className={styles.subtitle}>para tu <strong>{comidaName}</strong></p>
        
        <div className={styles.noIngredientsMessage}>
          <div className={styles.icon}>✓</div>
          <h3>Este producto no requiere personalización</h3>
          <p>Puedes agregarlo directamente a tu pedido o continuar con otro item.</p>
        </div>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <h2>Selecciona Ingredientes</h2>
      <p className={styles.subtitle}>para tu <strong>{comidaName}</strong></p>
      
      <div className={styles.grid}>
        {ingredientes.map(ingrediente => {
          const isSelected = selectedIngredientes.some(
            i => i.id_ingrediente === ingrediente.id_ingrediente
          );
          
          return (
            <button
              key={ingrediente.id_ingrediente}
              className={`${styles.card} ${isSelected ? styles.selected : ''}`}
              onClick={() => onToggleIngrediente(ingrediente)}
            >
              {isSelected && <span className={styles.checkmark}>✓</span>}
              <h3>{ingrediente.nombre}</h3>
              {ingrediente.descripcion && (
                <p className={styles.description}>{ingrediente.descripcion}</p>
              )}
            </button>
          );
        })}
      </div>
      
      {selectedIngredientes.length > 0 && (
        <div className={styles.selectedCount}>
          {selectedIngredientes.length} ingrediente(s) seleccionado(s)
        </div>
      )}
    </div>
  );
};

IngredientSelector.propTypes = {
  ingredientes: PropTypes.array,
  selectedIngredientes: PropTypes.array.isRequired,
  comidaName: PropTypes.string,
  onToggleIngrediente: PropTypes.func.isRequired
};

export default IngredientSelector;