import reflex as rx
from e_commerce_user_management.models.models import Product, CartItem


class CartState(rx.State):
    items: list[CartItem] = []
    is_cart_open: bool = False

    @rx.event
    def add_item(
        self, product: Product, quantity_to_add: int
    ):
        if quantity_to_add <= 0:
            yield rx.toast(
                "La cantidad debe ser positiva.",
                duration=3000,
            )
            return
        product_total_stock = product["stock"]
        if product_total_stock == 0:
            yield rx.toast(
                f"{product['name']} está agotado.",
                duration=3000,
            )
            return
        item_index_in_cart = -1
        existing_item_quantity = 0
        for i, item_in_cart_loop in enumerate(self.items):
            if (
                item_in_cart_loop["product_id"]
                == product["id"]
            ):
                item_index_in_cart = i
                existing_item_quantity = item_in_cart_loop[
                    "quantity"
                ]
                break
        max_permissible_cart_quantity = product_total_stock
        proposed_new_cart_quantity = (
            existing_item_quantity + quantity_to_add
        )
        final_new_cart_quantity = min(
            proposed_new_cart_quantity,
            max_permissible_cart_quantity,
        )
        quantity_effectively_changed = (
            final_new_cart_quantity - existing_item_quantity
        )
        if (
            quantity_effectively_changed <= 0
            and quantity_to_add > 0
        ):
            yield rx.toast(
                f"No se puede añadir más {product['name']}. Stock máximo ({product_total_stock}) alcanzado o ya en carrito.",
                duration=3000,
            )
            return
        if item_index_in_cart != -1:
            self.items[item_index_in_cart][
                "quantity"
            ] = final_new_cart_quantity
        else:
            self.items.append(
                {
                    "product_id": product["id"],
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": final_new_cart_quantity,
                    "image_url": product["image_url"],
                }
            )
        if (
            final_new_cart_quantity
            == existing_item_quantity + quantity_to_add
        ):
            yield rx.toast(
                f"Añadido {quantity_to_add} {product['name']} al carrito. Total en carrito: {final_new_cart_quantity}.",
                duration=2000,
            )
        elif quantity_effectively_changed > 0:
            yield rx.toast(
                f"Solo se añadieron {quantity_effectively_changed} de {product['name']} debido a límites de stock. Total en carrito: {final_new_cart_quantity}.",
                duration=3000,
            )

    @rx.event
    def remove_item(self, product_id: str):
        item_name_for_toast = ""
        for item in self.items:
            if item["product_id"] == product_id:
                item_name_for_toast = item["name"]
                break
        self.items = [
            item
            for item in self.items
            if item["product_id"] != product_id
        ]
        if item_name_for_toast:
            yield rx.toast(
                f"Eliminado {item_name_for_toast} del carrito.",
                duration=2000,
            )

    @rx.event
    async def update_item_quantity(
        self, product_id: str, change: int
    ):
        from e_commerce_user_management.states.product_state import ProductState

        item_index_to_update = -1
        current_cart_item: CartItem | None = None
        for i, item in enumerate(self.items):
            if item["product_id"] == product_id:
                item_index_to_update = i
                current_cart_item = item
                break
        if (
            item_index_to_update == -1
            or current_cart_item is None
        ):
            yield rx.toast(
                f"Artículo con ID {product_id} no encontrado en el carrito.",
                duration=3000,
            )
            return
        new_quantity = (
            current_cart_item["quantity"] + change
        )
        if new_quantity <= 0:
            yield CartState.remove_item(product_id)
            return
        if change > 0:
            product_state = await self.get_state(
                ProductState
            )
            original_product: Product | None = None
            for p in product_state.products:
                if p["id"] == product_id:
                    original_product = p
                    break
            if original_product:
                if new_quantity > original_product["stock"]:
                    new_quantity = original_product["stock"]
                    yield rx.toast(
                        f"Stock máximo para {original_product['name']} ({original_product['stock']}) alcanzado.",
                        duration=3000,
                    )
            else:
                yield rx.toast(
                    f"Error: Detalles del producto no encontrados para verificar stock (ID: {product_id}). Actualización permitida sin verificar stock.",
                    duration=4000,
                )
        self.items[item_index_to_update][
            "quantity"
        ] = new_quantity
        yield rx.toast(
            f"Actualizada cantidad de {current_cart_item['name']} a {new_quantity}.",
            duration=1500,
        )

    @rx.event
    def clear_cart(self):
        self.items = []
        yield rx.toast("Carrito vaciado.", duration=2000)

    @rx.event
    def clear_cart_after_checkout(self):
        self.items = []

    @rx.event
    def toggle_cart(self):
        self.is_cart_open = not self.is_cart_open

    @rx.var
    def total_items(self) -> int:
        return sum(
            (item["quantity"] for item in self.items)
        )

    @rx.var
    def total_price(self) -> float:
        price = sum(
            (
                item["price"] * item["quantity"]
                for item in self.items
            )
        )
        return round(price, 2)