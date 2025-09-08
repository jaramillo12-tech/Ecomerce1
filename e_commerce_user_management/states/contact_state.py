import reflex as rx


class ContactState(rx.State):
    name: str = ""
    email: str = ""
    subject: str = ""
    message: str = ""
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        print(
            f"Formulario de contacto enviado: {self.form_data}"
        )
        yield rx.toast(
            f"¡Mensaje enviado de {self.form_data.get('name', 'Usuario')}! Gracias."
        )
        self.name = ""
        self.email = ""
        self.subject = ""
        self.message = ""

    @rx.event
    def set_name(self, name: str):
        self.name = name

    @rx.event
    def set_email(self, email: str):
        self.email = email

    @rx.event
    def set_subject(self, subject: str):
        self.subject = subject

    @rx.event
    def set_message(self, message: str):
        self.message = message