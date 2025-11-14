# Cambios Implementados en Objetivos

## Resumen
Se han implementado los cambios solicitados para que cualquier rol pueda crear objetivos y cada objetivo tenga el nombre del usuario que lo creó. Solo el admin y el creador del objetivo pueden eliminarlo.

## Cambios Realizados

### 1. Modelo Objetivo (models.py)
- ✅ Agregado campo `creador` que referencia al usuario que creó el objetivo
- ✅ Campo obligatorio con relación ForeignKey a User

### 2. Migraciones de Base de Datos
- ✅ `0003_objetivo_creador.py`: Agrega el campo creador (inicialmente opcional)
- ✅ `0004_populate_objetivo_creador.py`: Asigna el creador del plan como creador de objetivos existentes
- ✅ `0005_alter_objetivo_creador.py`: Hace el campo creador obligatorio

### 3. Vistas (views.py)
- ✅ `objetivos()`: Removida restricción de admin para ver formulario, agregado select_related('creador')
- ✅ `agregar_objetivo()`: Removida restricción de admin, ahora cualquier miembro puede crear objetivos
- ✅ `eliminar_objetivo()`: Agregada verificación de permisos (solo admin o creador pueden eliminar)

### 4. Template (objetivos.html)
- ✅ Removida condición `es_admin` para mostrar formulario de creación
- ✅ Agregado nombre del creador en la información del objetivo
- ✅ Botón eliminar solo visible para admin o creador del objetivo
- ✅ Ajustado layout para que todos vean el formulario

## Funcionalidades Implementadas

### ✅ Cualquier rol puede crear objetivos
- Todos los miembros del plan pueden acceder al formulario de creación
- Al crear un objetivo, se asigna automáticamente el usuario actual como creador

### ✅ Cada objetivo muestra el nombre del creador
- En la lista de objetivos se muestra "Creado por: [username]"
- La información del creador es visible para todos los miembros

### ✅ Permisos de eliminación
- **Admin del plan**: Puede eliminar cualquier objetivo
- **Creador del objetivo**: Solo puede eliminar sus propios objetivos
- **Otros miembros**: No pueden eliminar objetivos que no crearon

## Instrucciones para Aplicar los Cambios

1. **Ejecutar migraciones**:
   ```bash
   ejecutar_migraciones.bat
   ```

2. **Aplicar cambios finales**:
   ```bash
   aplicar_cambios_objetivos.bat
   ```

3. **Verificar funcionamiento**:
   - Acceder a la sección de objetivos de cualquier plan
   - Crear un objetivo con cualquier rol (no solo admin)
   - Verificar que aparece el nombre del creador
   - Verificar que solo el admin y el creador pueden eliminar objetivos

## Notas Técnicas

- Los objetivos existentes tendrán como creador al creador del plan
- El campo creador es obligatorio para nuevos objetivos
- Se mantiene la funcionalidad existente de aportar dinero a objetivos
- No se afectan otras funcionalidades del sistema

## Archivos Modificados

1. `Planes_app/models.py` - Agregado campo creador
2. `Planes_app/views.py` - Actualizadas vistas de objetivos
3. `Planes_app/templates/objetivos.html` - Actualizado template
4. `Planes_app/migrations/` - Nuevas migraciones (0003, 0004, 0005)