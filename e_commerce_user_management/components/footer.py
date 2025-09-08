import reflex as rx
from e_commerce_user_management.states.theme_state import ThemeState


def footer() -> rx.Component:
    """Componente footer para la aplicación"""
    
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                # Información de la empresa
                rx.el.div(
                    rx.el.h3(
                        "TechStore",
                        class_name=rx.cond(
                            ThemeState.current_theme == "light",
                            "text-2xl font-bold text-sky-700 mb-4",
                            "text-2xl font-bold text-sky-400 mb-4"
                        )
                    ),
                    rx.el.p(
                        "Tu centro futurista para lo último en tecnología. Ofrecemos los mejores productos tecnológicos con la más alta calidad y el mejor servicio.",
                        class_name=rx.cond(
                            ThemeState.current_theme == "light",
                            "text-sky-600 mb-4 max-w-md",
                            "text-sky-200 mb-4 max-w-md"
                        )
                    ),
                    rx.el.div(
                        rx.el.span(
                            "📧 ",
                            class_name="text-lg"
                        ),
                        rx.el.span(
                            "info@techstore.com",
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-sky-600",
                                "text-sky-200"
                            )
                        ),
                        class_name="mb-2"
                    ),
                    rx.el.div(
                        rx.el.span(
                            "📞 ",
                            class_name="text-lg"
                        ),
                        rx.el.span(
                            "+573123456789",
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-sky-600",
                                "text-sky-200"
                            )
                        ),
                        class_name="mb-2"
                    ),
                    rx.el.div(
                        rx.el.span(
                            "📍 ",
                            class_name="text-lg"
                        ),
                        rx.el.span(
                            " Ubicados en el corazon de los de modalidad virtual del poli",
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-sky-600",
                                "text-sky-200"
                            )
                        )
                    ),
                    class_name="col-span-1 md:col-span-2"
                ),
                
                # Enlaces rápidos
                rx.el.div(
                    rx.el.h4(
                        "Enlaces Rápidos",
                        class_name=rx.cond(
                            ThemeState.current_theme == "light",
                            "text-lg font-semibold text-sky-700 mb-4",
                            "text-lg font-semibold text-sky-400 mb-4"
                        )
                    ),
                    rx.el.ul(
                        rx.el.li(
                            rx.el.a(
                                "Inicio",
                                href="/",
                                class_name=rx.cond(
                                    ThemeState.current_theme == "light",
                                    "text-sky-600 hover:text-sky-800 transition-colors",
                                    "text-sky-200 hover:text-white transition-colors"
                                )
                            ),
                            class_name="mb-2"
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Productos",
                                href="/products",
                                class_name=rx.cond(
                                    ThemeState.current_theme == "light",
                                    "text-sky-600 hover:text-sky-800 transition-colors",
                                    "text-sky-200 hover:text-white transition-colors"
                                )
                            ),
                            class_name="mb-2"
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Contacto",
                                href="/contact",
                                class_name=rx.cond(
                                    ThemeState.current_theme == "light",
                                    "text-sky-600 hover:text-sky-800 transition-colors",
                                    "text-sky-200 hover:text-white transition-colors"
                                )
                            ),
                            class_name="mb-2"
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Iniciar Sesión",
                                href="/sign_in",
                                class_name=rx.cond(
                                    ThemeState.current_theme == "light",
                                    "text-sky-600 hover:text-sky-800 transition-colors",
                                    "text-sky-200 hover:text-white transition-colors"
                                )
                            ),
                            class_name="mb-2"
                        )
                    ),
                    class_name="col-span-1"
                ),
                
                # Redes sociales
                rx.el.div(
                    rx.el.h4(
                        "Síguenos",
                        class_name=rx.cond(
                            ThemeState.current_theme == "light",
                            "text-lg font-semibold text-sky-700 mb-4",
                            "text-lg font-semibold text-sky-400 mb-4"
                        )
                    ),
                    rx.el.div(
                        rx.el.a(
                            "📘 Facebook",
                            href="#",
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-sky-600 hover:text-sky-800 transition-colors mr-4",
                                "text-sky-200 hover:text-white transition-colors mr-4"
                            )
                        ),
                        rx.el.a(
                            "📷 Instagram",
                            href="#",
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-sky-600 hover:text-sky-800 transition-colors mr-4",
                                "text-sky-200 hover:text-white transition-colors mr-4"
                            )
                        ),
                        rx.el.a(
                            "🐦 Twitter",
                            href="#",
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-sky-600 hover:text-sky-800 transition-colors",
                                "text-sky-200 hover:text-white transition-colors"
                            )
                        ),
                        class_name="flex flex-wrap"
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Horario de atención:",
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-sky-600 font-medium mt-4",
                                "text-sky-200 font-medium mt-4"
                            )
                        ),
                        rx.el.p(
                            "Lunes - Viernes: 9:00 AM - 8:00 PM",
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-sky-600",
                                "text-sky-200"
                            )
                        ),
                        rx.el.p(
                            "Sábados: 10:00 AM - 6:00 PM",
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-sky-600",
                                "text-sky-200"
                            )
                        ),
                        rx.el.p(
                            "Domingos: 12:00 PM - 5:00 PM",
                            class_name=rx.cond(
                                ThemeState.current_theme == "light",
                                "text-sky-600",
                                "text-sky-200"
                            )
                        )
                    ),
                    class_name="col-span-1"
                ),
                
                class_name="grid grid-cols-1 md:grid-cols-4 gap-8 max-w-6xl mx-auto"
            ),
            
            # Línea divisoria y copyright
            rx.el.hr(
                class_name=rx.cond(
                    ThemeState.current_theme == "light",
                    "border-sky-200 my-8",
                    "border-gray-600 my-8"
                )
            ),
            
            rx.el.div(
                rx.el.p(
                    "© 2025 TechStore. Todos los derechos reservados.",
                    class_name=rx.cond(
                        ThemeState.current_theme == "light",
                        "text-sky-600 text-center",
                        "text-sky-200 text-center"
                    )
                ),
                rx.el.p(
                    "Desarrollado con ❤️ a punta de aguapanela y python ",
                    class_name=rx.cond(
                        ThemeState.current_theme == "light",
                        "text-sky-500 text-center text-sm mt-2",
                        "text-sky-300 text-center text-sm mt-2"
                    )
                ),
                class_name="text-center"
            ),
            
            class_name="py-12 px-4"
        ),
        class_name=rx.cond(
            ThemeState.current_theme == "light",
            "bg-sky-50 border-t border-sky-200",
            "bg-gray-900 border-t border-gray-700"
        )
    )
