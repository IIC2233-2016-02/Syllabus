from gui import GUI, run


class MiGUI(GUI):
    def on_signin_dialog_signin_button_click(self, username, password):
        """Callback luego de presionar el botón `Ingresar` en diálogo de ingreso.
        Si es que no se está haciendo el BONUS, `password` será un string
        vacío.

        Retorna:
            bool -- si el ingreso es exitoso, es verdadero. En otro caso, falso.
        """
        return True

    def on_signup_dialog_signup_button_click(self, username, password, confirm_password):
        """Callback luego de presionar el botón `Registrarse` en diálogo de registro.
        Si es que no se está haciendo el BONUS, no se muestra el botón `Registrarse`.

        Retorna:
            bool -- si el registro es exitoso, es verdadero. En otro caso, falso.
        """
        return True

    def on_main_window_load(self):
        """Callback luego de cargarse la ventana principal.
        """
        pass

    def on_main_window_inbox_button_click(self):
        """Callback luego de presionar el botón `Buzón de entrada` en ventana
        principal.
        """
        pass

    def on_main_window_outbox_button_click(self):
        """Callback luego de presionar el botón `Buzón de salida` en ventana
        principal.
        """
        pass

    def on_main_window_signout_button_click(self):
        """Callback luego de presionar el botón `Desconectarse` en ventana
        principal.
        """
        pass

    def on_main_window_item_double_click(self, row):
        """Callback luego de hacer click en alguna fila de la tabla de la
        ventana principal.

        Argumentos:
            int row -- el índice de la fila dónde se hizo click.
        """
        pass

    def on_compose_widget_send_button_click(self, recipients, subject, msg):
        """Callback luego de presionar el botón `Enviar` en la ventana de
        redacción de correos.

        Argumentos:
            str recipients -- destinatarios de correo.
            str subject    -- asunto del correo.
            str msg        -- cuerpo del correo.
        Retorna:
            bool           -- si el envío es exitoso, retorna verdadero. En
            otro caso, retorna falso.
        """
        return True

if __name__ == "__main__":
    run(MiGUI)
