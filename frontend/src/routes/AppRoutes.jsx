// src/routes/AppRoutes.jsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Suspense, lazy } from 'react';
import PrivateRoute from './PrivateRoutes';

const Login = lazy(() => import('@/pages/Login/Login'));
const Home = lazy(() => import('@/pages/Home/Home'));
const Pedido = lazy(() => import('@/pages/Pedido/Pedido'));
const RestaurantesDisponibles = lazy(() => import('@/pages/RestaurantesDisponibles/RestaurantesDisponibles'));


const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Suspense fallback={<div>Cargando...</div>}>
        <Routes>
          <Route path="/" element={<Navigate to="/login" replace />} />
          <Route path="/login" element={<Login />} />
          
          <Route element={<PrivateRoute />}>
            <Route path="/home" element={<Home />} />
            <Route path="/pedido" element={<Pedido />} />
            <Route path="/pedido/restaurantes-disponibles" element={<RestaurantesDisponibles />} />
          </Route>

          <Route path="*" element={<Navigate to="/login" replace />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
};

export default AppRoutes;