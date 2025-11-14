// src/pages/Register/Register.jsx
import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuthContext } from '@/store/contexts/AuthContext';
import { authService } from '@/services/api/authService';
import styles from './Register.module.css';

const Register = () => {
  const navigate = useNavigate();
  const { login } = useAuthContext();

  const [formData, setFormData] = useState({
    nombre: '',
    direccion: '',
    email: '',
    contrasena: '',
    confirmarContrasena: ''
  });

  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  const [serverError, setServerError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    
    // Limpiar error del campo al escribir
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  const validateForm = () => {
    const newErrors = {};

    // Validar nombre
    if (!formData.nombre.trim()) {
      newErrors.nombre = 'El nombre es requerido';
    } else if (formData.nombre.trim().length < 2) {
      newErrors.nombre = 'El nombre debe tener al menos 2 caracteres';
    }

    // Validar dirección
    if (!formData.direccion.trim()) {
      newErrors.direccion = 'La dirección es requerida';
    } else if (formData.direccion.trim().length < 5) {
      newErrors.direccion = 'La dirección debe tener al menos 5 caracteres';
    }

    // Validar email
    if (!formData.email.trim()) {
      newErrors.email = 'El email es requerido';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Email inválido';
    }

    // Validar contraseña
    if (!formData.contrasena) {
      newErrors.contrasena = 'La contraseña es requerida';
    } else if (formData.contrasena.length < 6) {
      newErrors.contrasena = 'La contraseña debe tener al menos 6 caracteres';
    }

    // Validar confirmación de contraseña
    if (!formData.confirmarContrasena) {
      newErrors.confirmarContrasena = 'Debes confirmar la contraseña';
    } else if (formData.contrasena !== formData.confirmarContrasena) {
      newErrors.confirmarContrasena = 'Las contraseñas no coinciden';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setServerError('');

    if (!validateForm()) {
      return;
    }

    setLoading(true);

    // Preparar datos para el backend (sin confirmarContrasena)
    const userData = {
      nombre: formData.nombre.trim(),
      direccion: formData.direccion.trim(),
      email: formData.email.trim(),
      contrasena: formData.contrasena
    };

    const result = await authService.register(userData);

    if (result.success) {
      // Mostrar mensaje de éxito
      alert('¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.');
      
      // Redirigir al login
      navigate('/login');
    } else {
      setServerError(result.message);
    }

    setLoading(false);
  };

  return (
    <div className={styles.container}>
      <div className={styles.formCard}>
        <div className={styles.header}>
          <h1>Crear Cuenta</h1>
          <p>Únete y comienza a pedir</p>
        </div>

        <form onSubmit={handleSubmit} className={styles.form}>
          {/* Nombre */}
          <div className={styles.formGroup}>
            <label htmlFor="nombre">Nombre</label>
            <input
              type="text"
              id="nombre"
              name="nombre"
              value={formData.nombre}
              onChange={handleChange}
              className={errors.nombre ? styles.inputError : ''}
              placeholder="Ej: Juan Pérez"
            />
            {errors.nombre && (
              <span className={styles.error}>{errors.nombre}</span>
            )}
          </div>

          {/* Email */}
          <div className={styles.formGroup}>
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className={errors.email ? styles.inputError : ''}
              placeholder="tu@email.com"
            />
            {errors.email && (
              <span className={styles.error}>{errors.email}</span>
            )}
          </div>

          {/* Dirección */}
          <div className={styles.formGroup}>
            <label htmlFor="direccion">Dirección</label>
            <input
              type="text"
              id="direccion"
              name="direccion"
              value={formData.direccion}
              onChange={handleChange}
              className={errors.direccion ? styles.inputError : ''}
              placeholder="Ej: Av. Corrientes 1234"
            />
            {errors.direccion && (
              <span className={styles.error}>{errors.direccion}</span>
            )}
          </div>

          {/* Contraseña */}
          <div className={styles.formGroup}>
            <label htmlFor="contrasena">Contraseña</label>
            <input
              type="password"
              id="contrasena"
              name="contrasena"
              value={formData.contrasena}
              onChange={handleChange}
              className={errors.contrasena ? styles.inputError : ''}
              placeholder="Mínimo 6 caracteres"
            />
            {errors.contrasena && (
              <span className={styles.error}>{errors.contrasena}</span>
            )}
          </div>

          {/* Confirmar Contraseña */}
          <div className={styles.formGroup}>
            <label htmlFor="confirmarContrasena">Confirmar contraseña</label>
            <input
              type="password"
              id="confirmarContrasena"
              name="confirmarContrasena"
              value={formData.confirmarContrasena}
              onChange={handleChange}
              className={errors.confirmarContrasena ? styles.inputError : ''}
              placeholder="Repite tu contraseña"
            />
            {errors.confirmarContrasena && (
              <span className={styles.error}>{errors.confirmarContrasena}</span>
            )}
          </div>

          {/* Error del servidor */}
          {serverError && (
            <div className={styles.serverError}>
              <span>❌ {serverError}</span>
            </div>
          )}

          {/* Botón Submit */}
          <button
            type="submit"
            className={styles.submitBtn}
            disabled={loading}
          >
            {loading ? (
              <>
                <span className={styles.spinner}></span>
                Registrando...
              </>
            ) : (
              'Crear Cuenta'
            )}
          </button>
        </form>

        {/* Link a Login */}
        <div className={styles.footer}>
          <p>
            ¿Ya tienes cuenta? <Link to="/login">Inicia sesión</Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Register;