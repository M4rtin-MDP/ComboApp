// src/components/pedido/IngredientSelector/IngredientSelector.jsx
import PropTypes from 'prop-types';
import styles from './IngredientSelector.module.css';

const IngredientSelector = ({ 
  ingredientes, 
  selectedIngredientes, 
  comidaName,
  onToggleIngrediente 
}) => {
  
  const isSelected = (ingrediente) => {
    return selectedIngredientes.some(
      i => i.id_ingrediente === ingrediente.id_ingrediente
    );
  };

  return (
    <div className={styles.section}>
      <h2>Personaliza tu {comidaName}</h2>
      
      <div className={styles.ingredientsList}>
        {ingredientes.map(ingrediente => {
          const selected = isSelected(ingrediente);
          
          return (
            <div
              key={ingrediente.id_ingrediente}
              className={`${styles.ingredientItem} ${selected ? styles.selected : ''}`}
              onClick={() => onToggleIngrediente(ingrediente)}
            >
              <div className={styles.ingredientInfo}>
                <h4>{ingrediente.nombre}</h4>
              </div>
              <div className={styles.checkbox}>
                {selected && '✓'}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

IngredientSelector.propTypes = {
  ingredientes: PropTypes.array.isRequired,
  selectedIngredientes: PropTypes.array.isRequired,
  comidaName: PropTypes.string,
  onToggleIngrediente: PropTypes.func.isRequired
};

export default IngredientSelector;