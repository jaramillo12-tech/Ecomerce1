import reflex as rx
from e_commerce_user_management.components.navbar import navbar
from e_commerce_user_management.states.auth_state import AuthState
from e_commerce_user_management.states.theme_state import ThemeState


def admin_dashboard_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.div(
            rx.el.h1(
                "Panel de Administración",
                class_name=rx.cond(
                    ThemeState.current_theme == "light",
                    "text-3xl sm:text-4xl font-bold text-sky-800 mb-8 title-bounce",
                    "text-3xl sm:text-4xl font-bold text-white mb-8 title-bounce",
                ),
            ),
            rx.el.div(
                rx.el.a(
                    "Gestionar Productos",
                    href="/admin/manage-products",
                    class_name=rx.cond(
                        ThemeState.current_theme == "light",
                        "block w-full max-w-xs text-center bg-sky-500 hover:bg-sky-600 text-white font-semibold py-3 px-6 rounded-lg text-lg transition-all transform hover:scale-105 button-light-interactive mb-4",
                        "block w-full max-w-xs text-center bg-sky-600 hover:bg-sky-700 text-white font-semibold py-3 px-6 rounded-lg text-lg transition-colors transform hover:scale-105 mb-4",
                    ),
                ),
                rx.el.a(
                    "Ver Estadísticas de Productos",
                    href="/admin/statistics",
                    class_name=rx.cond(
                        ThemeState.current_theme == "light",
                        "block w-full max-w-xs text-center bg-green-500 hover:bg-green-600 text-white font-semibold py-3 px-6 rounded-lg text-lg transition-all transform hover:scale-105 button-light-interactive",
                        "block w-full max-w-xs text-center bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-6 rounded-lg text-lg transition-colors transform hover:scale-105",
                    ),
                ),
                class_name="flex flex-col items-center space-y-4",
            ),
            class_name=rx.cond(
                ThemeState.current_theme == "light",
                "container mx-auto flex flex-col items-center justify-center min-h-screen pt-24 px-4 bg-white",
                "container mx-auto flex flex-col items-center justify-center min-h-screen pt-24 px-4 bg-slate-900",
            ),
        ),
        on_mount=AuthState.check_admin_session,
        class_name=ThemeState.current_theme,
    )