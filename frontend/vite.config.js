import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  /*
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'), // Permite importar con '@'
    },
  },*/
  server: {
    port: 5173,          // Puerto del servidor local
    open: true,          // Abre el navegador automáticamente
    /*
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // Tu backend (por ejemplo, FastAPI)
        changeOrigin: true,
        secure: false,
      },
    },*/
  },
  /*
  build: {
    outDir: 'dist',      // Carpeta de salida al hacer `npm run build`
    sourcemap: true,     // Genera mapas de origen (útil para depuración)
  },
  css: {
    modules: {
      localsConvention: 'camelCase', // Nombres de clases CSS Modules
    },
  },*/
})
