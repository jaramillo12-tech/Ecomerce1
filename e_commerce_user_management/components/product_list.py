import reflex as rx
from e_commerce_user_management.states.product_state import ProductState
from e_commerce_user_management.components.product_card import product_card
from e_commerce_user_management.states.theme_state import ThemeState


def product_list_display() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Nuestros Productos",
            class_name=rx.cond(
                ThemeState.current_theme == "light",
                "text-3xl sm:text-4xl font-bold text-center text-sky-800 my-8 sm:my-10 tracking-wide title-bounce",
                "text-3xl sm:text-4xl font-bold text-center text-sky-300 my-8 sm:my-10 tracking-wide title-bounce",
            ),
        ),
        rx.el.input(
            default_value=ProductState.search_query,
            placeholder="Buscar productos por nombre...",
            on_change=ProductState.set_search_query.debounce(
                500
            ),
            class_name=rx.cond(
                ThemeState.current_theme == "light",
                "w-full max-w-md sm:max-w-xl mx-auto p-3 mb-10 bg-sky-50 border border-sky-300 rounded-lg text-sky-800 placeholder-sky-500 focus:ring-2 focus:ring-sky-400 focus:border-sky-400 shadow-md transition-shadow focus:shadow-sky-400/50",
                "w-full max-w-md sm:max-w-xl mx-auto p-3 mb-10 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:ring-2 focus:ring-sky-500 focus:border-sky-500 shadow-lg transition-shadow focus:shadow-sky-500/50",
            ),
        ),
        rx.cond(
            ProductState.filtered_products.length() > 0,
            rx.el.div(
                rx.foreach(
                    ProductState.filtered_products,
                    product_card,
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 md:gap-8 p-4 md:p-6 theme-transition",
            ),
            rx.el.div(
                rx.cond(
                    ProductState.search_query != "",
                    rx.el.p(
                        "No hay productos que coincidan con tu búsqueda.",
                        class_name=rx.cond(
                            ThemeState.current_theme
                            == "light",
                            "text-lg sm:text-xl text-sky-700",
                            "text-lg sm:text-xl text-gray-500",
                        ),
                    ),
                    rx.el.p(
                        "No hay productos disponibles en este momento. ¡Vuelve más tarde!",
                        class_name=rx.cond(
                            ThemeState.current_theme
                            == "light",
                            "text-lg sm:text-xl text-sky-700",
                            "text-lg sm:text-xl text-gray-500",
                        ),
                    ),
                ),
                class_name="text-center py-12",
            ),
        ),
        class_name="container mx-auto px-4",
    )