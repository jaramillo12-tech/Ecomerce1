import reflex as rx
from e_commerce_user_management.components.navbar import navbar
from e_commerce_user_management.components.product_list import product_list_display
from e_commerce_user_management.components.selected_product_view import (
    selected_product_modal,
)
from e_commerce_user_management.components.cart_sidebar import cart_sidebar
from e_commerce_user_management.states.product_state import ProductState
from e_commerce_user_management.states.theme_state import ThemeState


def products_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            product_list_display(),
            selected_product_modal(),
            cart_sidebar(),
            class_name=rx.cond(
                ThemeState.current_theme == "light",
                "min-h-screen text-sky-800 pt-16 sm:pt-20 bg-white theme-transition",
                "min-h-screen text-white pt-16 sm:pt-20 bg-slate-900 theme-transition",
            ),
        ),
        on_mount=ProductState.load_products,
        class_name=ThemeState.current_theme,
        style={
            "min-height": "100vh",
            "background-color": rx.cond(
                ThemeState.current_theme == "light",
                "white",
                "rgb(15, 23, 42)"
            ),
            "color": rx.cond(
                ThemeState.current_theme == "light",
                "rgb(30, 41, 59)",
                "white"
            ),
        },
    )