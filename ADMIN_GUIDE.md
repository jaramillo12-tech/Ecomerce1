# Guía de Administrador - TechStore

## 🔐 Credenciales de Administrador

**Usuario:** `admin`  
**Contraseña:** `adminpass`

## 🚀 Cómo Acceder al Panel de Administrador

1. Ve a la página de inicio de sesión: `http://localhost:3001/sign_in`
2. Ingresa las credenciales de administrador
3. Serás redirigido automáticamente al panel de administrador

## 📋 Funcionalidades Disponibles

### 1. **Gestionar Productos** (`/admin/manage-products`)
- ✅ **Agregar nuevos productos**
- ✅ **Editar productos existentes**
- ✅ **Eliminar productos**
- ✅ **Ver lista completa de productos**

### 2. **Dashboard de Administrador** (`/admin`)
- Vista general del sistema
- Acceso rápido a todas las funciones

### 3. **Estadísticas** (`/admin/statistics`)
- Estadísticas de ventas y productos

## 🛠️ Cómo Usar las Funciones de Administrador

### **Agregar un Nuevo Producto:**
1. Ve a "Gestionar Productos"
2. Haz clic en "Añadir Nuevo Producto"
3. Completa el formulario:
   - **Nombre:** Nombre del producto
   - **Descripción:** Descripción detallada
   - **Precio:** Precio en dólares (ej: 99.99)
   - **URL de Imagen:** Ruta de la imagen (por defecto: `/favicon.ico`)
   - **Categoría:** Categoría del producto
   - **Stock:** Cantidad disponible
4. Haz clic en "Añadir Producto"

### **Editar un Producto Existente:**
1. En la tabla de productos, haz clic en "Editar"
2. Modifica los campos necesarios
3. Haz clic en "Guardar Cambios"

### **Eliminar un Producto:**
1. En la tabla de productos, haz clic en "Eliminar"
2. El producto se eliminará inmediatamente

## 🎨 Modo Oscuro

El sistema de administrador también soporta modo oscuro:
- Usa el toggle en la navbar para cambiar entre tema claro y oscuro
- Todas las páginas de administrador se adaptan automáticamente

## 🔒 Seguridad

- Solo los usuarios con credenciales de administrador pueden acceder
- Las páginas de administrador verifican automáticamente los permisos
- Si no eres administrador, serás redirigido a la página de inicio de sesión

## 📱 Responsive Design

- El panel de administrador es completamente responsive
- Funciona en desktop, tablet y móvil
- Las tablas se adaptan automáticamente a diferentes tamaños de pantalla

## 🚨 Notas Importantes

1. **Cambios en Tiempo Real:** Los cambios se reflejan inmediatamente en la tienda
2. **Validación:** El sistema valida que los campos requeridos estén completos
3. **IDs Automáticos:** Los nuevos productos reciben IDs automáticamente
4. **Imágenes:** Por defecto usa `/favicon.ico`, pero puedes cambiar la URL

## 🆘 Usuarios de Prueba

**Administrador:**
- Usuario: `admin`
- Contraseña: `adminpass`

**Usuario Regular:**
- Usuario: `user`
- Contraseña: `pass`

---

¡Disfruta gestionando tu tienda TechStore! 🛍️
