import reflex as rx
from e_commerce_user_management.models.models import Product
from e_commerce_user_management.states.product_state import ProductState
from e_commerce_user_management.states.theme_state import ThemeState


def product_card(product: Product) -> rx.Component:
    return rx.el.div(
        rx.el.img(
            src=product["image_url"],
            alt=product["name"],
            class_name=rx.cond(
                ThemeState.current_theme == "light",
                "w-full h-48 object-cover rounded-t-lg group-hover:opacity-90 group-hover:scale-110 transition-all duration-300 product-card-image-light",
                "w-full h-48 object-cover rounded-t-lg group-hover:opacity-85 group-hover:scale-105 transition-all duration-300",
            ),
        ),
        rx.el.div(
            rx.el.h3(
                product["name"],
                class_name=rx.cond(
                    ThemeState.current_theme == "light",
                    "text-xl font-semibold text-sky-700 mb-1 truncate",
                    "text-xl font-semibold text-sky-400 mb-1 truncate",
                ),
            ),
            rx.el.p(
                f"${product['price']:.2f}",
                class_name="text-lg text-green-600 dark:text-green-400 font-bold mb-2",
            ),
            rx.el.p(
                product["description"],
                class_name=rx.cond(
                    ThemeState.current_theme == "light",
                    "text-sm text-sky-600 mb-3 h-12 overflow-hidden line-clamp-2",
                    "text-sm text-gray-400 mb-3 h-12 overflow-hidden line-clamp-2",
                ),
            ),
            rx.el.button(
                "Ver Detalles",
                on_click=lambda: ProductState.select_product(
                    product
                ),
                class_name=rx.cond(
                    ThemeState.current_theme == "light",
                    "w-full bg-sky-500 hover:bg-sky-600 text-white font-semibold py-2 px-4 rounded-md transition-all duration-200 transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-sky-400 focus:ring-opacity-50 button-light-interactive",
                    "w-full bg-sky-500 hover:bg-sky-600 text-white font-semibold py-2 px-4 rounded-md transition-all duration-200 transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-sky-400 focus:ring-opacity-50",
                ),
                disabled=product["stock"] == 0,
            ),
            rx.cond(
                product["stock"] == 0,
                rx.el.p(
                    "Agotado",
                    class_name="text-center text-red-500 dark:text-red-500 text-sm mt-2",
                ),
                rx.el.div(),
            ),
            class_name="p-4 flex flex-col flex-grow",
        ),
        class_name=rx.cond(
            ThemeState.current_theme == "light",
            "group bg-white rounded-lg overflow-hidden flex flex-col h-full animate-float product-card-light product-card theme-transition shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-2",
            "group bg-gray-800 rounded-lg shadow-xl overflow-hidden transform hover:shadow-sky-500/40 transition-all duration-300 hover:-translate-y-1.5 flex flex-col h-full animate-float product-card theme-transition",
        ),
    )