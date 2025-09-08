import reflex as rx
from e_commerce_user_management.states.product_state import ProductState
from e_commerce_user_management.states.theme_state import ThemeState


def selected_product_modal() -> rx.Component:
    return rx.el.dialog(
        rx.cond(
            ProductState.selected_product,
            rx.el.div(
                rx.el.img(
                    src=ProductState.selected_product[
                        "image_url"
                    ],
                    alt=ProductState.selected_product[
                        "name"
                    ],
                    class_name=rx.cond(
                        ThemeState.current_theme == "light",
                        "w-full h-48 sm:h-64 object-contain rounded-t-lg mb-4 bg-sky-50 p-2 border border-sky-200",
                        "w-full h-48 sm:h-64 object-contain rounded-t-lg mb-4 bg-gray-700 p-2",
                    ),
                ),
                rx.el.h2(
                    ProductState.selected_product["name"],
                    class_name=rx.cond(
                        ThemeState.current_theme == "light",
                        "text-2xl sm:text-3xl font-bold text-sky-700 mb-2",
                        "text-2xl sm:text-3xl font-bold text-sky-300 mb-2",
                    ),
                ),
                rx.el.p(
                    f"${ProductState.selected_product['price']:.2f}",
                    class_name="text-xl sm:text-2xl text-green-600 dark:text-green-400 font-semibold mb-4",
                ),
                rx.el.p(
                    ProductState.selected_product[
                        "description"
                    ],
                    class_name=rx.cond(
                        ThemeState.current_theme == "light",
                        "text-sky-700 mb-6 text-sm leading-relaxed max-h-32 overflow-y-auto",
                        "text-gray-300 mb-6 text-sm leading-relaxed max-h-32 overflow-y-auto",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Cantidad:",
                        class_name=rx.cond(
                            ThemeState.current_theme
                            == "light",
                            "text-sky-700 mr-3 font-medium text-sm sm:text-base",
                            "text-gray-300 mr-3 font-medium text-sm sm:text-base",
                        ),
                    ),
                    rx.el.button(
                        "-",
                        on_click=ProductState.decrement_quantity,
                        class_name=rx.cond(
                            ThemeState.current_theme
                            == "light",
                            "bg-sky-100 hover:bg-sky-200 text-sky-700 font-bold py-2 px-3 sm:px-4 rounded-l transition-colors focus:outline-none focus:ring-2 focus:ring-sky-400 text-sm sm:text-base",
                            "bg-gray-700 hover:bg-gray-600 text-white font-bold py-2 px-3 sm:px-4 rounded-l transition-colors focus:outline-none focus:ring-2 focus:ring-sky-500 text-sm sm:text-base",
                        ),
                        disabled=ProductState.selected_product[
                            "stock"
                        ]
                        == 0,
                    ),
                    rx.el.input(
                        default_value=ProductState.selected_quantity.to_string(),
                        key=ProductState.selected_quantity.to_string(),
                        read_only=True,
                        class_name=rx.cond(
                            ThemeState.current_theme
                            == "light",
                            "w-12 sm:w-16 text-center bg-white text-sky-800 border-y border-sky-300 focus:ring-0 py-2 text-sm sm:text-base",
                            "w-12 sm:w-16 text-center bg-gray-800 text-white border-y border-gray-700 focus:ring-0 py-2 text-sm sm:text-base",
                        ),
                    ),
                    rx.el.button(
                        "+",
                        on_click=ProductState.increment_quantity,
                        class_name=rx.cond(
                            ThemeState.current_theme
                            == "light",
                            "bg-sky-100 hover:bg-sky-200 text-sky-700 font-bold py-2 px-3 sm:px-4 rounded-r transition-colors focus:outline-none focus:ring-2 focus:ring-sky-400 text-sm sm:text-base",
                            "bg-gray-700 hover:bg-gray-600 text-white font-bold py-2 px-3 sm:px-4 rounded-r transition-colors focus:outline-none focus:ring-2 focus:ring-sky-500 text-sm sm:text-base",
                        ),
                        disabled=ProductState.selected_product[
                            "stock"
                        ]
                        == 0,
                    ),
                    class_name="flex items-center mb-6",
                ),
                rx.el.p(
                    f"En Stock: {ProductState.selected_product['stock']}",
                    class_name=rx.cond(
                        ProductState.selected_product[
                            "stock"
                        ]
                        > 0,
                        "text-sm text-green-600 dark:text-green-400 mb-6",
                        "text-sm text-red-500 dark:text-red-500 mb-6 font-semibold",
                    ),
                ),
                rx.el.div(
                    rx.el.button(
                        "Añadir al Carrito",
                        on_click=ProductState.add_selected_to_cart,
                        class_name=rx.cond(
                            ThemeState.current_theme
                            == "light",
                            "w-full bg-green-500 hover:bg-green-600 text-white font-bold py-2 sm:py-3 px-4 rounded-lg transition-all focus:outline-none focus:ring-2 focus:ring-green-400 text-sm sm:text-base button-light-interactive",
                            "w-full bg-green-500 hover:bg-green-600 text-white font-bold py-2 sm:py-3 px-4 rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-green-400 text-sm sm:text-base",
                        ),
                        disabled=(
                            ProductState.selected_quantity
                            == 0
                        )
                        | (
                            ProductState.selected_product[
                                "stock"
                            ]
                            == 0
                        ),
                    ),
                    class_name="mb-4",
                ),
                rx.el.button(
                    "Cerrar",
                    on_click=ProductState.close_detail_modal,
                    class_name=rx.cond(
                        ThemeState.current_theme == "light",
                        "w-full bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-4 rounded-lg transition-all focus:outline-none focus:ring-2 focus:ring-red-400 text-sm sm:text-base button-light-interactive",
                        "w-full bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-4 rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-red-400 text-sm sm:text-base",
                    ),
                ),
                class_name=rx.cond(
                    ThemeState.current_theme == "light",
                    "bg-white p-4 sm:p-6 md:p-8 rounded-xl shadow-2xl shadow-sky-300/60 w-full max-w-md sm:max-w-lg text-sky-800 relative",
                    "bg-gray-800 p-4 sm:p-6 md:p-8 rounded-xl shadow-2xl w-full max-w-md sm:max-w-lg text-white relative",
                ),
            ),
            rx.el.div(),
        ),
        open=ProductState.is_detail_modal_open,
        class_name=rx.cond(
            ThemeState.current_theme == "light",
            "fixed inset-0 bg-sky-700 bg-opacity-30 backdrop-blur-sm open:flex items-center justify-center p-4 z-[100]",
            "fixed inset-0 bg-black bg-opacity-50 dark:bg-opacity-80 backdrop-blur-sm open:flex items-center justify-center p-4 z-[100]",
        ),
    )