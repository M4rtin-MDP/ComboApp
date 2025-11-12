// src/components/pedido/CategorySelector/CategorySelector.jsx
import PropTypes from 'prop-types';
import styles from './CategorySelector.module.css';

const CategorySelector = ({ categorias, onSelectCategoria }) => {
  const getCategoryIcon = (nombre) => {
    const lowerName = nombre?.toLowerCase() || '';
    if (lowerName.includes('comida')) return '🍔';
    if (lowerName.includes('bebida')) return '🥤';
    if (lowerName.includes('postre')) return '🍰';
    return '🍽️';
  };

  return (
    <div className={styles.section}>
      <h2>Selecciona una categoría</h2>
      <div className={styles.grid}>
        {categorias.map(categoria => (
          <div
            key={categoria.id_categoria}
            className={styles.card}
            onClick={() => onSelectCategoria(categoria)}
          >
            <div className={styles.cardIcon}>
              {getCategoryIcon(categoria.nombre)}
            </div>
            <h3>{categoria.nombre}</h3>
          </div>
        ))}
      </div>
    </div>
  );
};

CategorySelector.propTypes = {
  categorias: PropTypes.array.isRequired,
  onSelectCategoria: PropTypes.func.isRequired
};

export default CategorySelector;