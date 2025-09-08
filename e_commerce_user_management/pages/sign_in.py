import reflex as rx
from e_commerce_user_management.states.auth_state import AuthState
from e_commerce_user_management.components.navbar import navbar
from e_commerce_user_management.components.auth_cards import sign_in_card
from e_commerce_user_management.states.theme_state import ThemeState


def sign_in_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.div(
            sign_in_card(),
            class_name=rx.cond(
                ThemeState.current_theme == "light",
                "flex flex-col items-center justify-center min-h-screen p-4 pt-20 bg-white",
                "flex flex-col items-center justify-center min-h-screen p-4 pt-20 bg-slate-900",
            ),
        ),
        on_mount=AuthState.check_login_status,
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