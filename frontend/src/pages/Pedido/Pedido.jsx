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

  const [selectedCategoria, setSelectedCategoria] = useState(null);
  const [selectedComida, setSelectedComida] = useState(null);
  const [selectedIngredientes, setSelectedIngredientes] = useState([]);
  
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
      setIngredientes(result.data);
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

  const handleFinalizarPedido = () => {
    const pedido = {
      categoria: selectedCategoria,
      comida: selectedComida,
      ingredientes: selectedIngredientes
    };
    
    console.log('Pedido armado:', pedido);
    alert('¡Pedido creado exitosamente!');
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
          categoria={selectedCategoria}
          comida={selectedComida}
          ingredientes={selectedIngredientes}
          onRemoveIngrediente={handleToggleIngrediente}
          onFinalizarPedido={handleFinalizarPedido}
          showFinishButton={step === 3}
        />
      </div>
    </div>
  );
};

export default Pedido;