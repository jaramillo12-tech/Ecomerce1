import reflex as rx
from e_commerce_user_management.components.navbar import navbar
from e_commerce_user_management.components.auth_cards import sign_up_card
from e_commerce_user_management.states.theme_state import ThemeState


def sign_up_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.div(
            sign_up_card(),
            class_name=rx.cond(
                ThemeState.current_theme == "light",
                "flex flex-col items-center justify-center min-h-screen p-4 pt-20 bg-white",
                "flex flex-col items-center justify-center min-h-screen p-4 pt-20 bg-slate-900",
            ),
        ),
        class_name=ThemeState.current_theme,
    )