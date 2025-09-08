import reflex as rx
from e_commerce_user_management.components.navbar import navbar
from e_commerce_user_management.states.auth_state import AuthState
from e_commerce_user_management.states.admin_stats_state import AdminStatsState
from e_commerce_user_management.states.theme_state import ThemeState


def admin_statistics_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.div(
            rx.el.h1(
                "Estadísticas de Productos",
                class_name=rx.cond(
                    ThemeState.current_theme == "light",
                    "text-3xl sm:text-4xl font-bold text-sky-800 mb-10 text-center title-bounce",
                    "text-3xl sm:text-4xl font-bold text-white mb-10 text-center title-bounce",
                ),
            ),
            rx.cond(
                AdminStatsState.product_purchase_summary.length()
                > 0,
                rx.el.div(
                    rx.el.h2(
                        "Productos Más Comprados",
                        class_name=rx.cond(
                            ThemeState.current_theme
                            == "light",
                            "text-2xl font-semibold text-sky-700 mb-6 text-center",
                            "text-2xl font-semibold text-sky-300 mb-6 text-center",
                        ),
                    ),
                    rx.el.div(
                        rx.recharts.bar_chart(
                            rx.recharts.cartesian_grid(
                                stroke_dasharray="3 3",
                                stroke=rx.cond(
                                    ThemeState.current_theme
                                    == "light",
                                    "#e0f2fe",
                                    "#374151",
                                ),
                            ),
                            rx.recharts.x_axis(
                                data_key="name",
                                class_name=rx.cond(
                                    ThemeState.current_theme
                                    == "light",
                                    "text-xs fill-sky-700",
                                    "text-xs fill-gray-300",
                                ),
                            ),
                            rx.recharts.y_axis(
                                allow_decimals=False,
                                class_name=rx.cond(
                                    ThemeState.current_theme
                                    == "light",
                                    "text-xs fill-sky-700",
                                    "text-xs fill-gray-300",
                                ),
                            ),
                            rx.recharts.tooltip(
                                wrapper_style={
                                    "zIndex": 1000
                                },
                                content_style=rx.cond(
                                    ThemeState.current_theme
                                    == "light",
                                    {
                                        "backgroundColor": "white",
                                        "border": "1px solid #e0f2fe",
                                    },
                                    {
                                        "backgroundColor": "#1f2937",
                                        "border": "1px solid #4b5563",
                                    },
                                ),
                            ),
                            rx.recharts.legend(),
                            rx.recharts.bar(
                                data_key="Vendidos",
                                fill=rx.cond(
                                    ThemeState.current_theme
                                    == "light",
                                    "#0ea5e9",
                                    "#38bdf8",
                                ),
                                radius=[4, 4, 0, 0],
                            ),
                            data=AdminStatsState.chart_data,
                            height=400,
                            margin={
                                "top": 5,
                                "right": 30,
                                "left": 20,
                                "bottom": 5,
                            },
                        ),
                        class_name=rx.cond(
                            ThemeState.current_theme
                            == "light",
                            "p-4 sm:p-6 bg-white rounded-xl shadow-xl shadow-sky-200/50",
                            "p-4 sm:p-6 bg-gray-800 rounded-xl shadow-xl",
                        ),
                    ),
                    rx.el.h3(
                        "Resumen Detallado",
                        class_name=rx.cond(
                            ThemeState.current_theme
                            == "light",
                            "text-xl font-semibold text-sky-700 mt-10 mb-4 text-center",
                            "text-xl font-semibold text-sky-300 mt-10 mb-4 text-center",
                        ),
                    ),
                    rx.el.div(
                        rx.el.table(
                            rx.el.thead(
                                rx.el.tr(
                                    rx.el.th(
                                        "Producto",
                                        class_name="py-2 px-4 border-b-2 border-gray-300 dark:border-gray-600 text-left",
                                    ),
                                    rx.el.th(
                                        "Total Vendido",
                                        class_name="py-2 px-4 border-b-2 border-gray-300 dark:border-gray-600 text-left",
                                    ),
                                    rx.el.th(
                                        "Ingresos Totales",
                                        class_name="py-2 px-4 border-b-2 border-gray-300 dark:border-gray-600 text-left",
                                    ),
                                )
                            ),
                            rx.el.tbody(
                                rx.foreach(
                                    AdminStatsState.product_purchase_summary,
                                    lambda item: rx.el.tr(
                                        rx.el.td(
                                            item["name"],
                                            class_name="py-2 px-4 border-b border-gray-200 dark:border-gray-700",
                                        ),
                                        rx.el.td(
                                            item[
                                                "total_sold"
                                            ],
                                            class_name="py-2 px-4 border-b border-gray-200 dark:border-gray-700",
                                        ),
                                        rx.el.td(
                                            f"${item['total_revenue']:.2f}",
                                            class_name="py-2 px-4 border-b border-gray-200 dark:border-gray-700",
                                        ),
                                        class_name=rx.cond(
                                            ThemeState.current_theme
                                            == "light",
                                            "hover:bg-sky-50",
                                            "hover:bg-gray-700",
                                        ),
                                    ),
                                )
                            ),
                            class_name="min-w-full",
                        ),
                        class_name=rx.cond(
                            ThemeState.current_theme
                            == "light",
                            "overflow-x-auto shadow-md rounded-lg mt-4 bg-white p-4",
                            "overflow-x-auto shadow-md rounded-lg mt-4 bg-gray-800 p-4",
                        ),
                    ),
                    class_name="w-full max-w-4xl mx-auto",
                ),
                rx.el.p(
                    "No hay datos de ventas para mostrar estadísticas.",
                    class_name=rx.cond(
                        ThemeState.current_theme == "light",
                        "text-center text-sky-600 text-lg py-10",
                        "text-center text-gray-500 text-lg py-10",
                    ),
                ),
            ),
            class_name=rx.cond(
                ThemeState.current_theme == "light",
                "container mx-auto py-10 px-4 min-h-screen pt-24 bg-white",
                "container mx-auto py-10 px-4 min-h-screen pt-24 bg-slate-900",
            ),
        ),
        on_mount=AuthState.check_admin_session,
        class_name=ThemeState.current_theme,
    )