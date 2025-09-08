import reflex as rx
import asyncio
from e_commerce_user_management.states.cart_state import CartState


class CheckoutState(rx.State):
    full_name: str = ""
    address: str = ""
    email: str = ""
    card_number: str = ""
    card_expiry: str = ""
    card_cvc: str = ""
    error_message: str = ""
    is_processing: bool = False

    @rx.event
    async def process_payment(self, form_data: dict):
        self.full_name = form_data.get("full_name", "")
        self.address = form_data.get("address", "")
        self.email = form_data.get("email", "")
        self.card_number = form_data.get("card_number", "")
        self.card_expiry = form_data.get("card_expiry", "")
        self.card_cvc = form_data.get("card_cvc", "")
        if not all(
            [
                self.full_name,
                self.address,
                self.email,
                self.card_number,
                self.card_expiry,
                self.card_cvc,
            ]
        ):
            self.error_message = (
                "Todos los campos son obligatorios."
            )
            yield rx.toast(
                self.error_message, duration=3000
            )
            return
        self.is_processing = True
        self.error_message = ""
        yield
        await asyncio.sleep(2)
        if "1234" in self.card_number:
            self.is_processing = False
            yield rx.toast(
                "¡Pago Exitoso! Gracias por tu pedido.",
                duration=5000,
            )
            cart_s = await self.get_state(CartState)
            from e_commerce_user_management.states.admin_stats_state import (
                AdminStatsState,
            )

            admin_stats_s = await self.get_state(
                AdminStatsState
            )
            for item in cart_s.items:
                yield admin_stats_s.record_sale_from_cart_item(
                    item
                )
            yield CartState.clear_cart_after_checkout
            self.full_name = ""
            self.address = ""
            self.email = ""
            self.card_number = ""
            self.card_expiry = ""
            self.card_cvc = ""
            yield rx.redirect("/")
        else:
            self.is_processing = False
            self.error_message = "Pago fallido. Por favor, revisa los detalles de tu tarjeta."
            yield rx.toast(
                self.error_message, duration=4000
            )

    @rx.event
    def set_full_name(self, value: str):
        self.full_name = value

    @rx.event
    def set_address(self, value: str):
        self.address = value

    @rx.event
    def set_email(self, value: str):
        self.email = value

    @rx.event
    def set_card_number(self, value: str):
        self.card_number = value

    @rx.event
    def set_card_expiry(self, value: str):
        self.card_expiry = value

    @rx.event
    def set_card_cvc(self, value: str):
        self.card_cvc = value