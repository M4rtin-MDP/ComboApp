import { Navigate, Outlet } from 'react-router-dom';
import { useAuthContext } from '@/store/contexts/AuthContext';

const PrivateRoute = () => {
  const { isAuthenticated, loading } = useAuthContext();

  // Mientras verifica el token
  if (loading) {
    return (
      <div style={{ 
        display: 'flex', 
        justifyContent: 'center', 
        alignItems: 'center', 
        height: '100vh' 
      }}>
        <p>Cargando...</p>
      </div>
    );
  }

  // Si no está autenticado, redirige al login
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  // Si está autenticado, renderiza la ruta
  return <Outlet />;
};

export default PrivateRoute;