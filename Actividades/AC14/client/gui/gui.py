from PyQt4 import QtCore, QtGui, uic
import os

BONUS = False

def get_absolute_path(relative_path):
    return os.path.join(os.path.dirname(__file__), relative_path)

splash_dialog_ui    = uic.loadUiType(get_absolute_path("./ui/splash_dialog.ui"))
signin_dialog_ui    = uic.loadUiType(get_absolute_path("./ui/signin_dialog.ui"))
signup_dialog_ui    = uic.loadUiType(get_absolute_path("./ui/signup_dialog.ui"))
main_window_ui      = uic.loadUiType(get_absolute_path("./ui/main_window.ui"))
compose_widget_ui   = uic.loadUiType(get_absolute_path("./ui/compose_widget.ui"))
read_mail_widget_ui = uic.loadUiType(get_absolute_path("./ui/read_mail_widget.ui"))


class GUI:
    def __init__(self):
        self.splash_dialog    = SplashDialog()
        self.signin_dialog    = SignInDialog()
        self.signup_dialog    = SignUpDialog()
        self.main_window      = MainWindow()
        self.compose_widget   = ComposeWidget()
        self.read_mail_widget = ReadMailWidget()

        self.__bind_signals()
        self.splash_dialog.show()
        self.splash_dialog.raise_()

    # MÉTODOS PÚBLICOS
    def add_mail_item(self, row, sender, recipient, subject):
        """Agrega una fila en la ventana principal.
        
        Argumentos:
            int row       -- la posición dónde se va a insertar la fila
            str sender    -- la dirección de quién envió el correo
            str recipient -- la dirección de quiénes reciben el correo
            str subject   -- el asunto del correo
        """
        row_count = self.main_window.mailTable.rowCount()
        self.main_window.mailTable.setRowCount(row_count + 1)
        for col, data in enumerate([sender, recipient, subject]):
            item = QtGui.QTableWidgetItem(data)
            self.main_window.mailTable.setItem(row, col, item)
        self.main_window.mailTable.resizeRowsToContents()

    def open_read_mail_widget(self, from_addr, to_addr, subject, msg):
        """Abre una ventana para visualizar un correo en particular.
        
        Argumentos:
            str from_addr -- dirección del emiso del correo
            str to_addr   -- dirección del receptor del correo
            str subject   -- asunto del correo
            str msg       -- cuerpo del correo
        """
        self.__reset_text_fields(self.read_mail_widget.text_fields)
        self.read_mail_widget.fromLineEdit.setText(from_addr)
        self.read_mail_widget.recipientsLineEdit.setText(to_addr)
        self.read_mail_widget.subjectLineEdit.setText(subject)
        self.read_mail_widget.bodyTextEdit.setText(msg)
        self.read_mail_widget.show()
        self.read_mail_widget.raise_()

    def reset_mail_table(self):
        """Elimina todas las filas de la ventana principal.
        """
        self.main_window.mailTable.clear()
        self.main_window.mailTable.setHorizontalHeaderLabels(
            ["De", "Para", "Asunto"]
        )
        self.main_window.mailTable.setRowCount(0)

    # MÉTODOS QUE DEBEN SER OVERRIDEADOS
    def on_signin_dialog_signin_button_click(self, username, password):
        """Callback luego de presionar el botón `Ingresar` en diálogo de ingreso.

        Retorna:
            bool -- si el ingreso es exitoso, es verdadero. En otro caso, falso.
        """
        return True

    def on_signup_dialog_signup_button_click(self, username, password, confirm_password):
        """Callback luego de presionar el botón `Registrarse` en diálogo de registro.

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

    # MÉTODOS PRIVADOS 
    def __bind_signals(self):
        # SplashDialog signals
        self.splash_dialog.signInButton.clicked.connect(
            self.__on_splash_dialog_signin_button_click
        )
        self.splash_dialog.signUpButton.clicked.connect(
            self.__on_splash_dialog_signup_button_click
        )

        # SignInDialog signals
        self.signin_dialog.signInButton.clicked.connect(
            self.__on_signin_dialog_signin_button_click
        )
        self.signin_dialog.backButton.clicked.connect(
            self.__on_signin_dialog_back_button_click
        )

        # SignUpDialog signals
        self.signup_dialog.signUpButton.clicked.connect(
            self.__on_signup_dialog_signup_button_click
        )
        self.signup_dialog.backButton.clicked.connect(
            self.__on_signup_dialog_back_button_click
        )

        # MainWindow signals
        self.main_window.composeButton.clicked.connect(
            self.__on_main_window_compose_button_click
        )
        self.main_window.inboxButton.clicked.connect(
            self.__on_main_window_inbox_button_click
        )
        self.main_window.outboxButton.clicked.connect(
            self.__on_main_window_outbox_button_click
        )
        self.main_window.signOutButton.clicked.connect(
            self.__on_main_window_signout_button_click
        )
        self.main_window.mailTable.itemDoubleClicked.connect(
            self.__on_main_window_item_double_click
        )
        
        # ComposeWidget signals
        self.compose_widget.sendButton.clicked.connect(
            self.__on_compose_widget_send_button_click
        )
        self.compose_widget.backButton.clicked.connect(
            self.__on_compose_widget_back_button_click
        )

        # ReadMailWidget signals
        self.read_mail_widget.backButton.clicked.connect(
            self.__on_read_mail_widget_back_button_click
        )

    def __on_splash_dialog_signin_button_click(self):
        self.__toggle_windows(self.signin_dialog, self.splash_dialog)

    def __on_splash_dialog_signup_button_click(self):
        self.__toggle_windows(self.signup_dialog, self.splash_dialog)

    def __on_signin_dialog_signin_button_click(self):
        username = self.signin_dialog.usernameLineEdit.text()
        password = self.signin_dialog.passwordLineEdit.text()

        if self.on_signin_dialog_signin_button_click(username, password):
            self.main_window.connectedLabel.setText(
                "Conectado como {}@uc.cl".format(username)
            )
            self.on_main_window_load()
            self.__toggle_windows(self.main_window, self.signin_dialog)
        else:
            self.__show_critical_message_box(
                self.signin_dialog, "Ocurrió un error en el ingreso"
            )

    def __on_signin_dialog_back_button_click(self):
        self.__toggle_windows(self.splash_dialog, self.signin_dialog)

    def __on_signup_dialog_signup_button_click(self):
        username = self.signup_dialog.usernameLineEdit.text()
        password = self.signup_dialog.passwordLineEdit.text()
        confirm_password = self.signup_dialog.confirmPasswordLineEdit.text()

        if self.on_signup_dialog_signup_button_click(username, password, confirm_password):
            self.main_window.connectedLabel.setText(
                "Conectado como {}@uc.cl".format(username)
            )
            self.on_main_window_load()
            self.__toggle_windows(self.main_window, self.signup_dialog)
        else:
            self.__show_critical_message_box(
                self.signup_dialog, "Ocurrió un error en el registro."
            )

    def __on_signup_dialog_back_button_click(self):
        self.__toggle_windows(self.splash_dialog, self.signup_dialog)

    def __on_main_window_compose_button_click(self):
        self.compose_widget.show()
        self.compose_widget.raise_()

    def __on_main_window_inbox_button_click(self):
        self.main_window.boxLabel.setText("Buzón de entrada")
        self.on_main_window_inbox_button_click()

    def __on_main_window_outbox_button_click(self):
        self.main_window.boxLabel.setText("Buzón de salida")
        self.on_main_window_outbox_button_click()

    def __on_main_window_signout_button_click(self):
        self.__toggle_windows(self.splash_dialog, self.main_window)
        self.on_main_window_signout_button_click()

    def __on_main_window_item_double_click(self, item):
        self.on_main_window_item_double_click(item.row())

    def __on_compose_widget_send_button_click(self):
        recipients = self.compose_widget.recipientsLineEdit.text()
        subject    = self.compose_widget.subjectLineEdit.text()
        msg        = self.compose_widget.bodyTextEdit.toPlainText()

        if self.on_compose_widget_send_button_click(recipients, subject, msg):
            self.__show_information_message_box(
                self.compose_widget, "Correo enviado con éxito."
            )
            self.__toggle_windows(self.main_window, self.compose_widget)
        else:
            self.__show_critical_message_box(
                self.compose_widget, "Ocurrió un error enviando el correo."
            )

    def __on_compose_widget_back_button_click(self):
        self.__toggle_windows(self.main_window, self.compose_widget)

    def __on_read_mail_widget_back_button_click(self):
        self.__toggle_windows(self.main_window, self.read_mail_widget)

    def __reset_text_fields(self, text_fields):
        for text_field in text_fields:
            text_field.setText("")

    def __toggle_windows(self, incoming, outgoing):
        outgoing.close()
        text_fields = getattr(outgoing, "text_fields", None)
        if text_fields is not None:
            self.__reset_text_fields(text_fields)
        incoming.show()
        incoming.raise_()

    def __show_critical_message_box(self, parent, msg):
        QtGui.QMessageBox.critical(parent, "Mail UCÉ", msg)

    def __show_information_message_box(self, parent, msg):
        QtGui.QMessageBox.information(parent, "Mail UCÉ", msg)


class SplashDialog(*splash_dialog_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        if not BONUS:
            self.signUpButton.hide()


class SignInDialog(*signin_dialog_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.text_fields = (self.usernameLineEdit, self.passwordLineEdit)

        if not BONUS:
            self.label_4.hide()
            self.passwordLineEdit.hide()


class SignUpDialog(*signup_dialog_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.text_fields = (self.usernameLineEdit, self.passwordLineEdit)


class MainWindow(*main_window_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ComposeWidget(*compose_widget_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.text_fields = (
            self.recipientsLineEdit,
            self.subjectLineEdit,
            self.bodyTextEdit
        )


class ReadMailWidget(*read_mail_widget_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.text_fields = (
            self.fromLineEdit,
            self.recipientsLineEdit,
            self.subjectLineEdit,
            self.bodyTextEdit
        )


if __name__ == "__main__":
    app = QtGui.QApplication([])
    gui = GUI()
    app.exec_()
