import reflex as rx
from e_commerce_user_management.models.models import Product
from e_commerce_user_management.database.database import db


class AdminProductState(rx.State):
    is_editing: bool = False
    editing_product_id: str | None = None
    show_product_modal: bool = False
    form_name: str = ""
    form_description: str = ""
    form_price: float = 0.0
    form_image_url: str = "/favicon.ico"
    form_category: str = "General"
    form_stock: int = 0

    @rx.var
    def products_for_admin(self) -> list[Product]:
        from e_commerce_user_management.states.product_state import (
            dummy_products_data,
        )

        return dummy_products_data

    def _clear_form(self):
        self.form_name = ""
        self.form_description = ""
        self.form_price = 0.0
        self.form_image_url = "/favicon.ico"
        self.form_category = "General"
        self.form_stock = 0
        self.editing_product_id = None
        self.is_editing = False

    @rx.event
    def open_add_product_modal(self):
        self._clear_form()
        self.is_editing = False
        self.show_product_modal = True

    @rx.event
    def open_edit_product_modal(self, product: Product):
        self.is_editing = True
        self.editing_product_id = product["id"]
        self.form_name = product["name"]
        self.form_description = product["description"]
        self.form_price = product["price"]
        self.form_image_url = product["image_url"]
        self.form_category = product["category"]
        self.form_stock = product["stock"]
        self.show_product_modal = True

    @rx.event
    def close_product_modal(self):
        self.show_product_modal = False
        self._clear_form()

    @rx.event
    async def handle_product_submit(self, form_data: dict):
        name = form_data.get("product_name", "")
        description = form_data.get(
            "product_description", ""
        )
        price_str = form_data.get("product_price", "0.0")
        try:
            price = float(price_str) if price_str else 0.0
        except ValueError:
            price = 0.0
        image_url = form_data.get(
            "product_image_url", "/favicon.ico"
        )
        category = form_data.get(
            "product_category", "General"
        )
        stock_str = form_data.get("product_stock", "0")
        try:
            stock = int(stock_str) if stock_str else 0
        except ValueError:
            stock = 0
        if not image_url:
            image_url = "/favicon.ico"
        if not category:
            category = "General"
        if not name or price <= 0 or stock < 0:
            yield rx.toast(
                "Nombre, precio positivo y stock no negativo son requeridos.",
                duration=3000,
            )
            return
        from e_commerce_user_management.states.product_state import (
            dummy_products_data,
            ProductState,
        )

        if self.is_editing and self.editing_product_id:
            # Actualizar producto existente en la base de datos
            success = db.update_service(
                self.editing_product_id, name, description, price, 
                image_url, category, stock
            )
            if success:
                yield rx.toast(f"Producto '{name}' actualizado.", duration=2000)
            else:
                yield rx.toast("Error al actualizar el producto.", duration=3000)
                return
        else:
            # Crear nuevo producto en la base de datos
            success = db.create_service(name, description, price, image_url, category, stock)
            if success:
                yield rx.toast(f"Producto '{name}' añadido.", duration=2000)
            else:
                yield rx.toast("Error al crear el producto.", duration=3000)
                return
        self.close_product_modal()
        product_s = await self.get_state(ProductState)
        yield product_s.load_products

    @rx.event
    async def delete_product(self, product_id: str):
        from e_commerce_user_management.states.product_state import (
            dummy_products_data,
            ProductState,
        )

        # Obtener nombre del producto antes de eliminarlo
        product = db.get_service_by_id(product_id)
        product_name = product["name"] if product else "Producto"
        
        # Eliminar de la base de datos
        success = db.delete_service(product_id)
        
        if success:
            yield rx.toast(f"Producto '{product_name}' eliminado.", duration=2000)
        else:
            yield rx.toast(f"Error: No se pudo eliminar el producto.", duration=3000)
        product_s = await self.get_state(ProductState)
        yield product_s.load_products