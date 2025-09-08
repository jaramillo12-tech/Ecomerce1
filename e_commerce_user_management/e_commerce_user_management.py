import reflex as rx
from e_commerce_user_management.pages.products import products_page
from e_commerce_user_management.pages.contact import contact_page
from e_commerce_user_management.pages.sign_in import sign_in_page
from e_commerce_user_management.pages.sign_up import sign_up_page
from e_commerce_user_management.pages.checkout import checkout_page
from e_commerce_user_management.pages.admin_dashboard import admin_dashboard_page
from e_commerce_user_management.pages.admin_manage_products import (
    admin_manage_products_page,
)
from e_commerce_user_management.pages.admin_statistics import admin_statistics_page
from e_commerce_user_management.pages.forgot_password import forgot_password_page
from e_commerce_user_management.states.theme_state import ThemeState
from e_commerce_user_management.states.auth_state import AuthState


def index() -> rx.Component:
    from e_commerce_user_management.components.navbar import navbar
    from e_commerce_user_management.components.slider import slider
    from e_commerce_user_management.components.footer import footer

    return rx.el.div(
        navbar(),
        # Hero Section
        rx.el.div(
            rx.el.h1(
                "¡Bienvenido a TechStore!",
                class_name=rx.cond(
                    ThemeState.current_theme == "light",
                    "text-4xl sm:text-5xl lg:text-6xl font-bold text-sky-800 mb-6 title-bounce",
                    "text-4xl sm:text-5xl lg:text-6xl font-bold text-white mb-6 title-bounce",
                ),
            ),
            rx.el.p(
                "Tu centro futurista para lo último en tecnología.",
                class_name=rx.cond(
                    ThemeState.current_theme == "light",
                    "text-lg sm:text-xl text-sky-600 mb-8 px-4",
                    "text-lg sm:text-xl text-sky-200 mb-8 px-4",
                ),
            ),
            rx.el.a(
                "Explorar Productos",
                href="/products",
                class_name=rx.cond(
                    ThemeState.current_theme == "light",
                    "bg-sky-500 hover:bg-sky-600 text-white font-bold py-2 px-4 sm:py-3 sm:px-6 rounded-lg text-base sm:text-lg transition-all transform hover:scale-105 button-light-interactive",
                    "bg-sky-500 hover:bg-sky-600 text-white font-bold py-2 px-4 sm:py-3 sm:px-6 rounded-lg text-base sm:text-lg transition-colors transform hover:scale-105",
                ),
            ),
            class_name=rx.cond(
                ThemeState.current_theme == "light",
                "flex flex-col items-center justify-center text-center min-h-screen pt-16 px-4 bg-white theme-transition",
                "flex flex-col items-center justify-center text-center min-h-screen pt-16 px-4 bg-slate-900 theme-transition",
            ),
        ),
        # Slider Section
        slider(),
        # Footer
        footer(),
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


app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css",
        "/animations.css",
    ],
)
app.add_page(index, route="/")
app.add_page(products_page, route="/products")
app.add_page(contact_page, route="/contact")
app.add_page(sign_in_page, route="/sign_in")
app.add_page(sign_up_page, route="/sign_up")
app.add_page(checkout_page, route="/checkout")
app.add_page(forgot_password_page, route="/forgot-password")
app.add_page(
    admin_dashboard_page,
    route="/admin",
    on_load=AuthState.check_admin_session,
)
app.add_page(
    admin_manage_products_page,
    route="/admin/manage-products",
    on_load=AuthState.check_admin_session,
)
app.add_page(
    admin_statistics_page,
    route="/admin/statistics",
    on_load=AuthState.check_admin_session,
)