import sqlite3
import os
from typing import List, Dict, Optional
from datetime import datetime


class Database:
    """Clase para manejar la base de datos SQLite"""
    
    def __init__(self, db_path: str = "techstore.db"):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        """Obtener conexión a la base de datos"""
        return sqlite3.connect(self.db_path)
    
    def init_database(self):
        """Inicializar la base de datos y crear tablas"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Crear tabla de usuarios
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT,
                    is_admin BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Crear tabla de servicios/productos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    image_url TEXT,
                    category TEXT,
                    stock INTEGER DEFAULT 0,
                    is_promotion BOOLEAN DEFAULT FALSE,
                    promotion_price REAL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Crear tabla de carrito (opcional para futuras funcionalidades)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cart_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    service_id INTEGER,
                    quantity INTEGER DEFAULT 1,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (service_id) REFERENCES services (id)
                )
            """)
            
            conn.commit()
            
            # Insertar datos iniciales si las tablas están vacías
            self._insert_initial_data(cursor)
            conn.commit()
    
    def _insert_initial_data(self, cursor):
        """Insertar datos iniciales en la base de datos"""
        
        # Verificar si ya hay usuarios
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        
        if user_count == 0:
            # Insertar usuario administrador
            cursor.execute("""
                INSERT INTO users (username, password, email, is_admin)
                VALUES (?, ?, ?, ?)
            """, ("admin", "adminpass", "admin@techstore.com", True))
            
            # Insertar usuario normal
            cursor.execute("""
                INSERT INTO users (username, password, email, is_admin)
                VALUES (?, ?, ?, ?)
            """, ("user", "pass", "user@techstore.com", False))
        
        # Verificar si ya hay servicios
        cursor.execute("SELECT COUNT(*) FROM services")
        service_count = cursor.fetchone()[0]
        
        if service_count == 0:
            # Insertar servicios iniciales
            initial_services = [
                ("Teclado Cibernético", "Teclado mecánico con RGB y teclas programables. Experimenta la escritura como nunca antes con retroalimentación táctil y efectos de iluminación personalizables.", 129.99, "https://www.tecnotienda.com.co/wp-content/uploads/2024/11/TECLADO-MECANIGO-GAMER-AL-75-GAMESTOP-GS200-700x700.webp", "Periféricos", 50, False, None),
                ("Ratón Cuántico", "Ratón gaming de alto DPI con diseño ergonómico. Seguimiento de precisión y botones personalizables te dan la ventaja en cualquier juego.", 79.5, "/favicon.ico", "Periféricos", 30, False, None),
                ("Monitor Holográfico", "Monitor 4K con tecnología holográfica. Experiencia visual inmersiva para trabajo y entretenimiento.", 599.99, "/favicon.ico", "Monitores", 15, True, 499.99),
                ("Auriculares Espaciales", "Auriculares con cancelación de ruido y sonido espacial 7.1. Sumérgete en el audio de alta fidelidad.", 199.99, "/favicon.ico", "Audio", 25, False, None),
                ("Placa Base Cuántica", "Placa base de última generación con soporte para procesadores de alta gama y memoria DDR5.", 299.99, "/favicon.ico", "Componentes", 20, False, None),
                ("Procesador Neural", "Procesador de 16 núcleos con inteligencia artificial integrada. Rendimiento excepcional para cualquier tarea.", 799.99, "/favicon.ico", "Componentes", 10, True, 699.99),
                ("Memoria RAM Holográfica", "32GB de memoria RAM con tecnología holográfica para acceso ultra-rápido a datos.", 249.99, "/favicon.ico", "Componentes", 40, False, None),
                ("Disco Duro Cuántico", "SSD de 2TB con tecnología cuántica para velocidades de transferencia nunca vistas.", 399.99, "/favicon.ico", "Almacenamiento", 35, False, None),
                ("Tarjeta Gráfica Espacial", "GPU de última generación con ray tracing y IA para gaming y renderizado profesional.", 1299.99, "/favicon.ico", "Componentes", 8, True, 1099.99),
                ("Fuente de Poder Dimensional", "Fuente de 1000W con eficiencia 80+ Platinum y tecnología de estabilización dimensional.", 199.99, "/favicon.ico", "Componentes", 25, False, None),
                ("Gabinete Futurista", "Gabinete con diseño futurista, iluminación RGB y excelente flujo de aire.", 149.99, "/favicon.ico", "Accesorios", 30, False, None),
                ("Webcam Holográfica", "Cámara web 4K con tecnología holográfica para videollamadas de alta calidad.", 179.99, "/favicon.ico", "Periféricos", 20, False, None),
                ("Micrófono Espacial", "Micrófono de condensador con cancelación de ruido y captura espacial.", 129.99, "/favicon.ico", "Audio", 15, False, None),
                ("Tablet Cuántica", "Tablet de 12 pulgadas con procesador cuántico y pantalla OLED.", 899.99, "/favicon.ico", "Dispositivos", 12, True, 799.99),
                ("Smartwatch Espacial", "Reloj inteligente con GPS espacial, monitoreo de salud y conectividad 5G.", 399.99, "/favicon.ico", "Wearables", 18, False, None),
                ("Router Cuántico", "Router WiFi 6E con tecnología cuántica para velocidades de internet ultrarrápidas.", 299.99, "/favicon.ico", "Redes", 22, False, None),
                ("Impresora 3D Holográfica", "Impresora 3D que crea objetos holográficos con resolución molecular.", 1999.99, "/favicon.ico", "Impresión", 5, True, 1799.99),
                ("Teclado Virtual", "Teclado holográfico que se proyecta en el aire y detecta el tacto.", 499.99, "/favicon.ico", "Periféricos", 8, False, None),
                ("Mouse Pad Cuántico", "Alfombrilla de mouse con superficie cuántica para precisión extrema.", 49.99, "/favicon.ico", "Accesorios", 50, False, None),
                ("Cable USB-C Espacial", "Cable de alta velocidad con tecnología espacial para transferencias ultrarrápidas.", 29.99, "/favicon.ico", "Accesorios", 100, False, None),
                ("Hub USB Cuántico", "Hub USB con 8 puertos y tecnología cuántica para máxima compatibilidad.", 79.99, "/favicon.ico", "Accesorios", 35, False, None),
                ("Lámpara LED Holográfica", "Lámpara LED que proyecta hologramas y cambia de color según el estado de ánimo.", 89.99, "/favicon.ico", "Accesorios", 40, False, None),
                ("Ventilador Cuántico", "Ventilador de CPU con tecnología cuántica para refrigeración silenciosa y eficiente.", 69.99, "/favicon.ico", "Componentes", 60, False, None),
                ("Filtro de Aire Espacial", "Filtro de aire para gabinete que purifica el aire usando tecnología espacial.", 39.99, "/favicon.ico", "Accesorios", 45, False, None),
                ("Cable de Red Cuántico", "Cable Ethernet con tecnología cuántica para velocidades de red ultrarrápidas.", 59.99, "/favicon.ico", "Redes", 30, False, None),
                ("Adaptador WiFi Espacial", "Adaptador WiFi USB con tecnología espacial para conexiones estables.", 49.99, "/favicon.ico", "Redes", 25, False, None)
            ]
            
            cursor.executemany("""
                INSERT INTO services (name, description, price, image_url, category, stock, is_promotion, promotion_price)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, initial_services)
    
    # Métodos para usuarios
    def get_user_by_username(self, username: str) -> Optional[Dict]:
        """Obtener usuario por nombre de usuario"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "username": row[1],
                    "password": row[2],
                    "email": row[3],
                    "is_admin": bool(row[4]),
                    "created_at": row[5],
                    "updated_at": row[6]
                }
            return None
    
    def create_user(self, username: str, password: str, email: str = None, is_admin: bool = False) -> bool:
        """Crear nuevo usuario"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO users (username, password, email, is_admin)
                    VALUES (?, ?, ?, ?)
                """, (username, password, email, is_admin))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False  # Usuario ya existe
    
    # Métodos para servicios
    def get_all_services(self) -> List[Dict]:
        """Obtener todos los servicios"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM services ORDER BY created_at DESC")
            rows = cursor.fetchall()
            return [
                {
                    "id": str(row[0]),
                    "name": row[1],
                    "description": row[2],
                    "price": row[3],
                    "image_url": row[4],
                    "category": row[5],
                    "stock": row[6],
                    "is_promotion": bool(row[7]),
                    "promotion_price": row[8],
                    "created_at": row[9],
                    "updated_at": row[10]
                }
                for row in rows
            ]
    
    def get_service_by_id(self, service_id: str) -> Optional[Dict]:
        """Obtener servicio por ID"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM services WHERE id = ?", (service_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": str(row[0]),
                    "name": row[1],
                    "description": row[2],
                    "price": row[3],
                    "image_url": row[4],
                    "category": row[5],
                    "stock": row[6],
                    "is_promotion": bool(row[7]),
                    "promotion_price": row[8],
                    "created_at": row[9],
                    "updated_at": row[10]
                }
            return None
    
    def create_service(self, name: str, description: str, price: float, image_url: str, 
                      category: str, stock: int, is_promotion: bool = False, 
                      promotion_price: float = None) -> bool:
        """Crear nuevo servicio"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO services (name, description, price, image_url, category, stock, is_promotion, promotion_price)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (name, description, price, image_url, category, stock, is_promotion, promotion_price))
                conn.commit()
                return True
        except Exception as e:
            print(f"Error creating service: {e}")
            return False
    
    def update_service(self, service_id: str, name: str, description: str, price: float, 
                      image_url: str, category: str, stock: int, is_promotion: bool = False, 
                      promotion_price: float = None) -> bool:
        """Actualizar servicio existente"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE services 
                    SET name = ?, description = ?, price = ?, image_url = ?, category = ?, 
                        stock = ?, is_promotion = ?, promotion_price = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (name, description, price, image_url, category, stock, is_promotion, promotion_price, service_id))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating service: {e}")
            return False
    
    def delete_service(self, service_id: str) -> bool:
        """Eliminar servicio"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM services WHERE id = ?", (service_id,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting service: {e}")
            return False


# Instancia global de la base de datos
db = Database()
