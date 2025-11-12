// src/components/pedido/ComidaSelector/ComidaSelector.jsx
import PropTypes from 'prop-types';
import styles from './ComidaSelector.module.css';

const ComidaSelector = ({ comidas, categoriaName, onSelectComida }) => {
  return (
    <div className={styles.section}>
      <h2>Selecciona tu {categoriaName}</h2>
      <div className={styles.grid}>
        {comidas.map(comida => (
          <div
            key={comida.id_comida}
            className={styles.card}
            onClick={() => onSelectComida(comida)}
          >
            <div className={styles.cardIcon}>🍽️</div>
            <h3>{comida.nombre}</h3>
          </div>
        ))}
      </div>
    </div>
  );
};

ComidaSelector.propTypes = {
  comidas: PropTypes.array.isRequired,
  categoriaName: PropTypes.string,
  onSelectComida: PropTypes.func.isRequired
};

export default ComidaSelector;