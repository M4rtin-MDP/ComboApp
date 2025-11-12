import PropTypes from 'prop-types';
import styles from './Button.module.css';

/**
 * Componente Button reutilizable
 * @param {Object} props - Props del componente
 * @param {string} props.variant - Variante del botón (primary, secondary, danger)
 * @param {ReactNode} props.children - Contenido del botón
 * @param {Function} props.onClick - Función al hacer click
 */
const Button = ({ 
  children, 
  variant = 'primary', 
  onClick, 
  disabled = false,
  type = 'button',
  ...rest 
}) => {
  return (
    <button
      type={type}
      className={`${styles.button} ${styles[variant]}`}
      onClick={onClick}
      disabled={disabled}
      {...rest}
    >
      {children}
    </button>
  );
};

Button.propTypes = {
  children: PropTypes.node.isRequired,
  variant: PropTypes.oneOf(['primary', 'secondary', 'danger']),
  onClick: PropTypes.func,
  disabled: PropTypes.bool,
  type: PropTypes.oneOf(['button', 'submit', 'reset'])
};

export default Button;