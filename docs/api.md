## Git

1. Crear rama feature: `git checkout -b feature`
2. Commit: `git commit -m '<tipo>:<breve descripcion>'`

    | Tipo       | Uso                                                   |
    | ---------- | ----------------------------------------------------- |
    | `feat`     | Nueva funcionalidad                                   |
    | `fix`      | Corrección de errores                                 |
    | `docs`     | Cambios en documentación                              |
    | `style`    | Cambios de formato o estilo (sin afectar la lógica)   |
    | `refactor` | Mejora del código sin cambiar funcionalidad           |
    | `test`     | Añadir o modificar tests                              |
    | `chore`    | Tareas de mantenimiento (dependencias, scripts, etc.) |

3. Push a la rama:  `git push origin feature`
4. Abrir Pull Request