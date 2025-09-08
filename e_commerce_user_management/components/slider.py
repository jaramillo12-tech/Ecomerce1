import reflex as rx
from e_commerce_user_management.states.theme_state import ThemeState


def slider() -> rx.Component:
    """Componente slider/carrusel para el home"""
    
    # Datos del slider - productos destacados
    slides_data = [
        {
            "id": "1",
            "title": "Teclado Cibernético",
            "description": "Experimenta la escritura como nunca antes",
            "price": "$129.99",
            "image": "/favicon.ico",
            "link": "/products"
        },
        {
            "id": "2", 
            "title": "Ratón Cuántico",
            "description": "Precisión y velocidad para gaming",
            "price": "$79.50",
            "image": "/favicon.ico",
            "link": "/products"
        },
        {
            "id": "3",
            "title": "Monitor Holográfico",
            "description": "Resolución 4K con tecnología futurista",
            "price": "$599.99",
            "image": "/favicon.ico",
            "link": "/products"
        }
    ]
    
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Productos Destacados",
                class_name=rx.cond(
                    ThemeState.current_theme == "light",
                    "text-3xl font-bold text-sky-800 mb-8 text-center",
                    "text-3xl font-bold text-white mb-8 text-center"
                )
            ),
            rx.el.div(
                *[
                    rx.el.div(
                        rx.el.img(
                            src=slide["image"],
                            alt=slide["title"],
                            class_name="w-full h-64 object-cover rounded-lg mb-4"
                        ),
                        rx.el.h3(
                            slide["title"],
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-xl font-semibold text-sky-800 mb-2",
                                "text-xl font-semibold text-white mb-2"
                            )
                        ),
                        rx.el.p(
                            slide["description"],
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-sky-600 mb-3",
                                "text-sky-200 mb-3"
                            )
                        ),
                        rx.el.div(
                            rx.el.span(
                                slide["price"],
                                class_name=rx.cond(
                                    ThemeState.current_theme == "light",
                                    "text-2xl font-bold text-green-600",
                                    "text-2xl font-bold text-green-400"
                                )
                            ),
                            rx.el.a(
                                "Ver Detalles",
                                href=slide["link"],
                                class_name="ml-4 bg-sky-500 hover:bg-sky-600 text-white px-4 py-2 rounded-lg transition-colors"
                            ),
                            class_name="flex items-center justify-between"
                        ),
                        class_name=rx.cond(
                            ThemeState.current_theme == "light",
                            "bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow",
                            "bg-gray-800 p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow"
                        )
                    )
                    for slide in slides_data
                ],
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto"
            ),
            class_name="py-16 px-4"
        ),
        class_name=rx.cond(
            ThemeState.current_theme == "light",
            "bg-gray-50",
            "bg-gray-900"
        )
    )
