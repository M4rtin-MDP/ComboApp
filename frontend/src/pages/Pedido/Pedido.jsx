// src/pages/Pedido/Pedido.jsx
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { categoriaService } from '@/services/api/categoriaService';
import { ingredientesService } from '@/services/api/ingredientesService';
import CategorySelector from '@/components/pedido/CategorySelector/CategorySelector';
import ComidaSelector from '@/components/pedido/ComidaSelector/ComidaSelector';
import IngredientSelector from '@/components/pedido/IngredientSelector/IngredientSelector';
import PedidoSummary from '@/components/pedido/PedidoSummary/PedidoSummary';
import styles from './Pedido.module.css';

const Pedido = () => {
  const navigate = useNavigate();
  
  const [step, setStep] = useState(1);
  const [categorias, setCategorias] = useState([]);
  const [comidas, setComidas] = useState([]);
  const [ingredientes, setIngredientes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Estado para el item actual que se está armando
  const [selectedCategoria, setSelectedCategoria] = useState(null);
  const [selectedComida, setSelectedComida] = useState(null);
  const [selectedIngredientes, setSelectedIngredientes] = useState([]);
  
  // Carrito con todos los items agregados - INICIALIZADO
  const [carrito, setCarrito] = useState([]);
  
  useEffect(() => {
    loadCategorias();
  }, []);

  const loadCategorias = async () => {
    setLoading(true);
    const result = await categoriaService.getCategorias();
    
    if (result.success) {
      setCategorias(result.data);
    } else {
      setError(result.message);
    }
    
    setLoading(false);
  };

  const handleSelectCategoria = async (categoria) => {
    setSelectedCategoria(categoria);
    setLoading(true);
    setComidas([]);

    const result = await categoriaService.getComidasByCategoria(categoria.id_categoria);
    
    if (result.success) {
      const comidasArray = Array.isArray(result.data) ? result.data : [result.data];
      setComidas(comidasArray);
      setStep(2);
    } else {
      setError(result.message);
    }
    
    setLoading(false);
  };

  const handleSelectComida = async (comida) => {
    setSelectedComida(comida);
    setLoading(true);
    setIngredientes([]);

    const result = await ingredientesService.getIngredientesByComida(comida.id_comida);
    
    if (result.success) {
      const ingredientesData = result.data || [];
      setIngredientes(ingredientesData);
      
      // Si no hay ingredientes, ir directo a paso 3 pero permitir agregar sin ingredientes
      setStep(3);
    } else {
      setError(result.message);
    }
    
    setLoading(false);
  };

  const handleToggleIngrediente = (ingrediente) => {
    setSelectedIngredientes(prev => {
      const exists = prev.find(i => i.id_ingrediente === ingrediente.id_ingrediente);
      if (exists) {
        return prev.filter(i => i.id_ingrediente !== ingrediente.id_ingrediente);
      }
      return [...prev, ingrediente];
    });
  };

  const handleBack = () => {
    if (step === 3) {
      setStep(2);
      setSelectedComida(null);
      setSelectedIngredientes([]);
    } else if (step === 2) {
      setStep(1);
      setSelectedCategoria(null);
      setComidas([]);
    } else {
      navigate('/home');
    }
  };

  // Nueva función: Agregar item actual al carrito
  const handleAgregarItem = () => {
    if (!selectedCategoria || !selectedComida) {
      alert('Debes seleccionar al menos una categoría y comida');
      return;
    }

    const nuevoItem = {
      id: Date.now(), // ID único para cada item
      categoria: selectedCategoria,
      comida: selectedComida,
      ingredientes: [...selectedIngredientes] // Puede ser array vacío
    };
    
    setCarrito(prev => [...prev, nuevoItem]);
    
    // Resetear selección actual para agregar otro item
    setStep(1);
    setSelectedCategoria(null);
    setSelectedComida(null);
    setSelectedIngredientes([]);
    setComidas([]);
    setIngredientes([]);
  };

  // Función para remover un item completo del carrito
  const handleRemoveItem = (itemId) => {
    setCarrito(prev => prev.filter(item => item.id !== itemId));
  };

  // Función para remover un ingrediente del item actual (antes de agregarlo al carrito)
  const handleRemoveIngredienteActual = (ingrediente) => {
    handleToggleIngrediente(ingrediente);
  };

  const handleFinalizarPedido = () => {
    // Si hay algo seleccionado actualmente, agregarlo primero
    let pedidoFinal = [...carrito];
    
    if (selectedCategoria && selectedComida) {
      const itemActual = {
        id: Date.now(),
        categoria: selectedCategoria,
        comida: selectedComida,
        ingredientes: [...selectedIngredientes]
      };
      pedidoFinal = [...carrito, itemActual];
    }

    if (pedidoFinal.length === 0) {
      alert('Debes agregar al menos un item al pedido');
      return;
    }
    
    console.log('Pedido final:', pedidoFinal);
    
    // Navegar a la página de restaurantes disponibles con el pedido
    navigate('/pedido/restaurantes-disponibles', { 
      state: { pedido: pedidoFinal }
    });
  };

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <button onClick={handleBack} className={styles.backBtn}>
          ← Volver
        </button>
        <h1>Armar Pedido</h1>
        <div className={styles.steps}>
          <span className={step >= 1 ? styles.stepActive : ''}>1</span>
          <span className={step >= 2 ? styles.stepActive : ''}>2</span>
          <span className={step >= 3 ? styles.stepActive : ''}>3</span>
        </div>
      </header>

      <div className={styles.contentWrapper}>
        <main className={styles.main}>
          {error && <div className={styles.error}>{error}</div>}
          {loading && <div className={styles.loading}>Cargando...</div>}

          {step === 1 && !loading && (
            <CategorySelector 
              categorias={categorias}
              onSelectCategoria={handleSelectCategoria}
            />
          )}

          {step === 2 && !loading && (
            <ComidaSelector 
              comidas={comidas}
              categoriaName={selectedCategoria?.nombre}
              onSelectComida={handleSelectComida}
            />
          )}

          {step === 3 && !loading && (
            <IngredientSelector 
              ingredientes={ingredientes}
              selectedIngredientes={selectedIngredientes}
              comidaName={selectedComida?.nombre}
              onToggleIngrediente={handleToggleIngrediente}
            />
          )}
        </main>

        <PedidoSummary 
          // Item actual siendo editado
          categoriaActual={selectedCategoria}
          comidaActual={selectedComida}
          ingredientesActuales={selectedIngredientes}
          onRemoveIngredienteActual={handleRemoveIngredienteActual}
          
          // Carrito completo
          carrito={carrito}
          onRemoveItem={handleRemoveItem}
          
          // Acciones
          onAgregarItem={handleAgregarItem}
          onFinalizarPedido={handleFinalizarPedido}
          showActionButtons={step >= 2 && selectedComida !== null}
        />
      </div>
    </div>
  );
};

export default Pedido;