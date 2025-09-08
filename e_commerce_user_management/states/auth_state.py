import reflex as rx
import os
from twilio.rest import Client
from e_commerce_user_management.database.database import db

TWILIO_ACCOUNT_SID = os.environ.get(
    "TWILIO_ACCOUNT_SID", "YOUR_TWILIO_ACCOUNT_SID"
)
TWILIO_AUTH_TOKEN = os.environ.get(
    "TWILIO_AUTH_TOKEN", "YOUR_TWILIO_AUTH_TOKEN"
)
TWILIO_PHONE_NUMBER = os.environ.get(
    "TWILIO_PHONE_NUMBER", "YOUR_TWILIO_PHONE_NUMBER"
)


class AuthState(rx.State):
    is_logged_in: bool = False
    username: str = ""
    password: str = ""
    email: str = ""
    error_message: str = ""
    is_admin: bool = False
    recovery_method: str = "email"
    recovery_input: str = ""
    verification_code_sent: str = ""
    reset_code_input: str = ""
    new_password_recovery: str = ""
    confirm_new_password_recovery: str = ""
    recovery_message: str = ""
    recovery_step: str = "request"

    @rx.event
    def login(self, form_data: dict):
        username_from_form = form_data.get("username", "")
        password_from_form = form_data.get("password", "")
        self.username = username_from_form
        # Buscar usuario en la base de datos
        user = db.get_user_by_username(username_from_form)
        
        if user and user["password"] == password_from_form:
            self.is_logged_in = True
            self.is_admin = user["is_admin"]
            self.error_message = ""
            self.password = ""
            
            if self.is_admin:
                yield rx.redirect("/admin")
                yield rx.toast("¡Inicio de sesión de administrador exitoso!")
            else:
                yield rx.redirect("/products")
                yield rx.toast("¡Inicio de sesión exitoso!")
        else:
            self.error_message = "Credenciales incorrectas"
            self.is_logged_in = False
            self.is_admin = False
            self.password = ""
            yield rx.toast(
                self.error_message, duration=3000
            )

    @rx.event
    def logout(self):
        self.is_logged_in = False
        self.is_admin = False
        self.username = ""
        self.email = ""
        self.password = ""
        yield rx.redirect("/")
        yield rx.toast("Sesión cerrada exitosamente.")

    @rx.event
    def signup(self, form_data: dict):
        username_from_form = form_data.get("username", "")
        email_from_form = form_data.get("email", "")
        self.username = username_from_form
        self.email = email_from_form
        self.password = ""
        print(
            f"Usuario registrado: {username_from_form}, Correo: {email_from_form}"
        )
        self.is_logged_in = True
        self.is_admin = False
        self.error_message = ""
        yield rx.redirect("/")
        yield rx.toast(
            "¡Registro exitoso! Ahora has iniciado sesión."
        )

    @rx.event
    def check_login_status(self):
        pass

    @rx.event
    def check_admin_session(self):
        if not self.is_logged_in or not self.is_admin:
            yield rx.toast(
                "Acceso denegado. Debes ser administrador.",
                duration=3000,
            )
            yield rx.redirect("/sign_in")

    @rx.event
    def set_username(self, username: str):
        self.username = username

    @rx.event
    def set_password(self, password: str):
        self.password = password

    @rx.event
    def set_email(self, email: str):
        self.email = email

    @rx.var
    def is_admin_user(self) -> bool:
        return self.is_logged_in and self.is_admin

    @rx.event
    def set_recovery_method(self, method: str):
        self.recovery_method = method
        self.recovery_input = ""
        self.recovery_message = ""

    @rx.event
    def set_recovery_input(self, value: str):
        self.recovery_input = value

    @rx.event
    def set_reset_code_input(self, value: str):
        self.reset_code_input = value

    @rx.event
    def set_new_password_recovery(self, value: str):
        self.new_password_recovery = value

    @rx.event
    def set_confirm_new_password_recovery(self, value: str):
        self.confirm_new_password_recovery = value

    @rx.event
    def request_password_reset(self, form_data: dict):
        self.recovery_method = form_data.get(
            "recovery_method_option", self.recovery_method
        )
        self.recovery_input = form_data.get(
            "recovery_input_field", ""
        )
        if not self.recovery_input:
            self.recovery_message = "Por favor, ingresa tu correo o número de teléfono."
            yield rx.toast(self.recovery_message)
            return
        self.verification_code_sent = "123456"
        self.recovery_message = f"Se ha enviado un código de verificación a {self.recovery_input}."
        self.recovery_step = "verify"
        if self.recovery_method == "phone":
            if (
                TWILIO_ACCOUNT_SID
                == "YOUR_TWILIO_ACCOUNT_SID"
                or TWILIO_AUTH_TOKEN
                == "YOUR_TWILIO_AUTH_TOKEN"
                or TWILIO_PHONE_NUMBER
                == "YOUR_TWILIO_PHONE_NUMBER"
            ):
                print(
                    f"Simulación de SMS: Código {self.verification_code_sent} enviado a {self.recovery_input}. Configure las credenciales de Twilio para enviar SMS reales."
                )
                yield rx.toast(
                    "SMS simulado enviado. Revise la consola."
                )
            else:
                try:
                    client = Client(
                        TWILIO_ACCOUNT_SID,
                        TWILIO_AUTH_TOKEN,
                    )
                    message = client.messages.create(
                        body=f"Tu código de verificación para TechStore es: {self.verification_code_sent}",
                        from_=TWILIO_PHONE_NUMBER,
                        to=self.recovery_input,
                    )
                    print(
                        f"SMS enviado a {self.recovery_input}: SID {message.sid}"
                    )
                    yield rx.toast(
                        f"SMS enviado a {self.recovery_input}."
                    )
                except Exception as e:
                    print(f"Error al enviar SMS: {e}")
                    self.recovery_message = "Error al enviar SMS. Intenta con correo electrónico."
                    yield rx.toast(self.recovery_message)
                    self.recovery_step = "request"
        else:
            print(
                f"Simulación de correo: Código {self.verification_code_sent} enviado a {self.recovery_input}"
            )
            yield rx.toast(
                f"Correo de verificación simulado enviado a {self.recovery_input}. Revisa la consola."
            )
        yield rx.toast(self.recovery_message)

    @rx.event
    def verify_reset_code(self, form_data: dict):
        self.reset_code_input = form_data.get(
            "reset_code_input_field", ""
        )
        if (
            self.reset_code_input
            == self.verification_code_sent
        ):
            self.recovery_message = "Código verificado. Ahora puedes restablecer tu contraseña."
            self.recovery_step = "reset"
            self.reset_code_input = ""
        else:
            self.recovery_message = (
                "Código de verificación incorrecto."
            )
        yield rx.toast(self.recovery_message)

    @rx.event
    def process_password_reset(self, form_data: dict):
        self.new_password_recovery = form_data.get(
            "new_password_field", ""
        )
        self.confirm_new_password_recovery = form_data.get(
            "confirm_new_password_field", ""
        )
        if not self.new_password_recovery:
            self.recovery_message = (
                "La nueva contraseña no puede estar vacía."
            )
            yield rx.toast(self.recovery_message)
            return
        if (
            self.new_password_recovery
            != self.confirm_new_password_recovery
        ):
            self.recovery_message = (
                "Las contraseñas no coinciden."
            )
            yield rx.toast(self.recovery_message)
            return
        print(
            f"Contraseña para {self.recovery_input} (originalmente {self.username or self.email}) ha sido cambiada a: {self.new_password_recovery}"
        )
        self.recovery_message = "¡Contraseña restablecida exitosamente! Ya puedes iniciar sesión con tu nueva contraseña."
        yield rx.toast(self.recovery_message)
        self._clear_recovery_fields()
        yield rx.redirect("/sign_in")

    def _clear_recovery_fields(self):
        self.recovery_method = "email"
        self.recovery_input = ""
        self.verification_code_sent = ""
        self.reset_code_input = ""
        self.new_password_recovery = ""
        self.confirm_new_password_recovery = ""

    @rx.event
    def go_to_request_step(self):
        self._clear_recovery_fields()
        self.recovery_message = ""
        self.recovery_step = "request"