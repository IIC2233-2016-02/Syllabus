import socket
from pickle import dumps, loads
from random import randint, random
from sys import exit
from threading import Thread

DEFAULT_HOST = socket.gethostname()
DEFAULT_PORT = 1234


class Client:

    def __init__(self, host=None, port=None):
        """
        Esta clase representa a un cliente, el cual se conecta 
        a un servidor en host:port. Ademas, puede enviar y recibir 
        mensajes del servidor
        """
        host = DEFAULT_HOST if host is None else host
        port = DEFAULT_PORT if port is None else port
        # socket.AF_INET: AddressFamily, indica que usaremos protocolos de internet (TCP o UDP)
        # socket.SOCK_STREAM: SocketKind, indica el tipo de socket (en este caso TCP)
        # Nota: Para UDP es socket.SOCK_DGRAM
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._current_list = list()
        self.is_alive = True
        try:
            # Un cliente puede conectarse (escuchar) solamente a un servidor
            self._socket.connect((host, port))
            # Escuchamos mensajes en un thread aparte para desocupar el principal
            self._receiver = Thread(target=self._hear_message_from_server)
            self._receiver.daemon = True
            self._receiver.start()
        except socket.error:
            print("No fue posible realizar la conexión")
            exit()

    def _hear_message_from_server(self):
        """
        Esta funcion es la que queda en un thread auxiliar 
        recibiendo lo que envie el servidor
        """
        while self.is_alive:
            data = self._socket.recv(1024)
            content = loads(data)
            self._current_list = content
            print("Servidor: {}".format(content))

    def send_message_to_server(self, new_element):
        """
        Esta funcion recibe un mensaje, lo serializa 
        y luego lo envia al servidor
        """
        self._current_list.append(new_element)
        print("Enviando... {}".format(self._current_list))
        final_content = dumps(self._current_list)
        self._socket.send(final_content)

    def disconnect(self):
        """ 
        Esta funcion deberia cerrar la conexion 
        con el servidor
        """
        print("<== Conexión cerrada ==>")
        self.is_alive = False
        self._socket.close()

if __name__ == '__main__':
    client = Client()
    while client.is_alive:
        new_element = input()
        client.send_message_to_server(new_element)
