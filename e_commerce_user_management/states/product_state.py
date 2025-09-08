import reflex as rx
from e_commerce_user_management.models.models import Product
from e_commerce_user_management.states.cart_state import CartState
from e_commerce_user_management.database.database import db

dummy_products_data: list[Product] = [
    {
        "id": "1",
        "name": "Teclado Cibernético",
        "description": "Teclado mecánico con RGB y teclas programables. Experimenta la escritura como nunca antes con retroalimentación táctil y efectos de iluminación personalizables.",
        "price": 129.99,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Mechanical_keyboard.jpg",
        "category": "Periféricos",
        "stock": 50,
    },
    {
        "id": "2",
        "name": "Ratón Cuántico",
        "description": "Ratón gaming de alto DPI con diseño ergonómico. Seguimiento de precisión y botones personalizables te dan la ventaja en cualquier juego.",
        "price": 79.5,
        "image_url": "/favicon.ico",
        "category": "Periféricos",
        "stock": 30,
    },
    {
        "id": "3",
        "name": "Pantalla Holográfica",
        "description": "Pantalla holográfica 4K de 27 pulgadas para experiencias inmersivas. Ve tu contenido cobrar vida con colores vibrantes y una claridad impresionante.",
        "price": 599.0,
        "image_url": "/favicon.ico",
        "category": "Monitores",
        "stock": 15,
    },
    {
        "id": "4",
        "name": "Casco VR Sigiloso",
        "description": "Casco VR de última generación con FOV ultra amplio y pantallas de alta resolución. Sumérgete en mundos virtuales con una inmersión y comodidad incomparables.",
        "price": 349.99,
        "image_url": "/favicon.ico",
        "category": "VR",
        "stock": 0,
    },
    {
        "id": "5",
        "name": "Procesador Núcleo IA",
        "description": "CPU revolucionario impulsado por IA para un rendimiento sin igual en aprendizaje automático y cálculos complejos. Cuenta con unidades de procesamiento neuronal dedicadas.",
        "price": 799.0,
        "image_url": "/favicon.ico",
        "category": "Componentes",
        "stock": 10,
    },
    {
        "id": "6",
        "name": "Fuente de Poder Neutrino",
        "description": "PSU de 1200W con clasificación Titanium, tecnología de ventilador silencioso y cables modulares. Asegura una entrega de energía estable y eficiente.",
        "price": 249.99,
        "image_url": "/favicon.ico",
        "category": "Componentes",
        "stock": 22,
    },
    {
        "id": "7",
        "name": "SSD de Terabyte Nova",
        "description": "Unidad de estado sólido ultrarrápida de 1TB con velocidades de lectura/escritura NVMe. Ideal para sistemas operativos, juegos y aplicaciones exigentes.",
        "price": 149.99,
        "image_url": "/favicon.ico",
        "category": "Almacenamiento",
        "stock": 40,
    },
    {
        "id": "8",
        "name": "RAM DDR5 Hyperion 32GB",
        "description": "Kit de memoria RAM DDR5 de 32GB (2x16GB) a 6000MHz. Overclocking estable y baja latencia para el máximo rendimiento en juegos y multitarea.",
        "price": 199.5,
        "image_url": "/favicon.ico",
        "category": "Componentes",
        "stock": 25,
    },
    {
        "id": "9",
        "name": "Tarjeta Gráfica Nebula RTX 7090",
        "description": "Potente tarjeta gráfica con trazado de rayos en tiempo real y DLSS 3.0. Disfruta de los últimos juegos con la máxima fidelidad visual y fluidez.",
        "price": 1299.0,
        "image_url": "/favicon.ico",
        "category": "Componentes",
        "stock": 8,
    },
    {
        "id": "10",
        "name": "Webcam ProStream 4K",
        "description": "Cámara web 4K con enfoque automático inteligente y micrófono con cancelación de ruido. Perfecta para streaming profesional y videoconferencias.",
        "price": 179.0,
        "image_url": "/favicon.ico",
        "category": "Periféricos",
        "stock": 18,
    },
    {
        "id": "11",
        "name": "Auriculares Inmersivos SonicWave",
        "description": "Auriculares gaming con sonido envolvente 7.1, micrófono desmontable y almohadillas de espuma viscoelástica. Comodidad y audio de alta fidelidad.",
        "price": 99.99,
        "image_url": "/favicon.ico",
        "category": "Audio",
        "stock": 33,
    },
    {
        "id": "12",
        "name": "Router Malla Orion WiFi 6E",
        "description": "Sistema de router de malla WiFi 6E tribanda para cobertura total en el hogar y velocidades gigabit. Conexión estable para múltiples dispositivos.",
        "price": 299.99,
        "image_url": "/favicon.ico",
        "category": "Redes",
        "stock": 12,
    },
    {
        "id": "13",
        "name": "Monitor Curvo Ultrawide Galaxy",
        "description": "Monitor curvo ultrawide de 34 pulgadas QHD (3440x1440) con tasa de refresco de 144Hz. Experiencia visual panorámica para juegos y productividad.",
        "price": 459.0,
        "image_url": "/favicon.ico",
        "category": "Monitores",
        "stock": 20,
    },
    {
        "id": "14",
        "name": "Lector de Huellas Biométrico SecureKey",
        "description": "Lector de huellas USB para inicio de sesión seguro y rápido en Windows Hello. Protege tus datos con autenticación biométrica.",
        "price": 39.95,
        "image_url": "/favicon.ico",
        "category": "Seguridad",
        "stock": 60,
    },
    {
        "id": "15",
        "name": "Alfombrilla Gaming RGB XL Titan",
        "description": "Alfombrilla de ratón extra grande con superficie optimizada para precisión y iluminación RGB personalizable en los bordes. Base antideslizante.",
        "price": 45.0,
        "image_url": "/favicon.ico",
        "category": "Periféricos",
        "stock": 50,
    },
    {
        "id": "16",
        "name": "Silla Gaming ErgoFlex Pro",
        "description": "Silla gaming ergonómica con soporte lumbar ajustable, reposabrazos 4D y cuero sintético transpirable. Diseñada para largas sesiones de juego.",
        "price": 329.99,
        "image_url": "/favicon.ico",
        "category": "Mobiliario",
        "stock": 10,
    },
    {
        "id": "17",
        "name": "Micrófono de Condensador StudioCast",
        "description": "Micrófono de condensador USB con calidad de estudio, patrón polar cardioide y monitoreo de latencia cero. Ideal para podcasts, streaming y grabación.",
        "price": 119.0,
        "image_url": "/favicon.ico",
        "category": "Audio",
        "stock": 28,
    },
    {
        "id": "18",
        "name": "Impresora Multifunción LaserMax",
        "description": "Impresora láser multifunción monocromo con escáner, copiadora y fax. Impresión rápida y eficiente para oficinas pequeñas y hogar.",
        "price": 229.5,
        "image_url": "/favicon.ico",
        "category": "Impresoras",
        "stock": 16,
    },
    {
        "id": "19",
        "name": "Disco Duro Externo TitanShield 4TB",
        "description": "Disco duro externo USB 3.2 de 4TB con carcasa resistente a golpes. Solución de almacenamiento portátil y segura para tus archivos.",
        "price": 109.99,
        "image_url": "/favicon.ico",
        "category": "Almacenamiento",
        "stock": 35,
    },
    {
        "id": "20",
        "name": "Tableta Gráfica DigiSketch Pro",
        "description": "Tableta gráfica profesional con pantalla laminada de 15.6 pulgadas, lápiz sensible a la presión y teclas de acceso rápido programables. Para artistas digitales.",
        "price": 499.0,
        "image_url": "/favicon.ico",
        "category": "Periféricos",
        "stock": 7,
    },
    {
        "id": "21",
        "name": "Proyector LED Nebula Max",
        "description": "Proyector LED Full HD 1080p con Android TV integrado, altavoces estéreo y corrección trapezoidal automática. Cine en casa inteligente.",
        "price": 379.0,
        "image_url": "/favicon.ico",
        "category": "Proyectores",
        "stock": 11,
    },
    {
        "id": "22",
        "name": "Sistema de Refrigeración Líquida HydroChill",
        "description": "Refrigeración líquida AIO para CPU con radiador de 240mm y ventiladores RGB. Mantiene tu procesador fresco bajo cargas intensas.",
        "price": 139.99,
        "image_url": "/favicon.ico",
        "category": "Componentes",
        "stock": 19,
    },
    {
        "id": "23",
        "name": "Docking Station Universal TitanConnect",
        "description": "Estación de acoplamiento USB-C con múltiples puertos: HDMI 4K, Ethernet, USB 3.0, lector de tarjetas SD/MicroSD. Expande la conectividad de tu laptop.",
        "price": 89.9,
        "image_url": "/favicon.ico",
        "category": "Accesorios",
        "stock": 42,
    },
    {
        "id": "24",
        "name": "Gafas de Realidad Aumentada HoloLens Lite",
        "description": "Gafas de RA ligeras para visualización de información superpuesta y aplicaciones interactivas. Ideal para desarrolladores y profesionales.",
        "price": 699.0,
        "image_url": "/favicon.ico",
        "category": "VR/AR",
        "stock": 5,
    },
    {
        "id": "25",
        "name": "Smartwatch Chronos X",
        "description": "Reloj inteligente con GPS, monitor de frecuencia cardíaca, SpO2 y múltiples modos deportivos. Pantalla AMOLED y batería de larga duración.",
        "price": 199.99,
        "image_url": "/favicon.ico",
        "category": "Wearables",
        "stock": 23,
    },
    {
        "id": "26",
        "name": "Altavoz Bluetooth Portátil AuraSound",
        "description": "Altavoz Bluetooth con sonido 360°, resistente al agua (IPX7) y 12 horas de autonomía. Perfecto para llevar tu música a todas partes.",
        "price": 69.5,
        "image_url": "/favicon.ico",
        "category": "Audio",
        "stock": 45,
    },
]


class ProductState(rx.State):
    products: list[Product] = []
    selected_product: Product | None = None
    selected_quantity: int = 1
    is_detail_modal_open: bool = False
    search_query: str = ""

    @rx.event
    def load_products(self):
        """Cargar productos desde la base de datos"""
        try:
            # Cargar desde la base de datos
            db_products = db.get_all_services()
            self.products = db_products
            self.filtered_products = db_products
        except Exception as e:
            print(f"Error loading products from database: {e}")
            # Fallback a datos dummy si hay error
            self.products = dummy_products_data
            self.filtered_products = dummy_products_data

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.var
    def filtered_products(self) -> list[Product]:
        if not self.search_query.strip():
            return self.products
        search_lower = self.search_query.lower()
        return [
            product
            for product in self.products
            if search_lower in product["name"].lower()
        ]

    @rx.event
    def select_product(self, product: Product):
        self.selected_product = product
        self.selected_quantity = (
            1 if product["stock"] > 0 else 0
        )
        self.is_detail_modal_open = True

    @rx.event
    def close_detail_modal(self):
        self.is_detail_modal_open = False
        self.selected_product = None
        self.selected_quantity = 1

    @rx.event
    def increment_quantity(self):
        if (
            self.selected_product
            and self.selected_quantity
            < self.selected_product["stock"]
        ):
            self.selected_quantity += 1
        elif (
            self.selected_product
            and self.selected_quantity
            >= self.selected_product["stock"]
        ):
            yield rx.toast(
                f"Stock máximo ({self.selected_product['stock']}) alcanzado para {self.selected_product['name']}.",
                duration=3000,
            )

    @rx.event
    def decrement_quantity(self):
        if not self.selected_product:
            return
        if self.selected_product["stock"] == 0:
            self.selected_quantity = 0
            return
        if self.selected_quantity > 1:
            self.selected_quantity -= 1

    @rx.event
    def add_selected_to_cart(self):
        if (
            self.selected_product
            and self.selected_quantity > 0
        ):
            yield CartState.add_item(
                self.selected_product,
                self.selected_quantity,
            )
            yield ProductState.close_detail_modal
        elif (
            self.selected_product
            and self.selected_quantity == 0
        ):
            yield rx.toast(
                f"{self.selected_product['name']} está agotado o la cantidad es cero.",
                duration=3000,
            )